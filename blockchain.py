import json
import time
import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
 
def generate_rsa_keypair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def sign_data(private_key, data_bytes):
    return private_key.sign(
        data_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def verify_signature(public_key, signature, data_bytes):
    try:
        public_key.verify(
            signature,
            data_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False

class Transaction:
    def __init__(self, sender_pubkey, receiver, amount, message=""):
        self.sender_pubkey = sender_pubkey
        self.receiver = receiver
        self.amount = amount
        self.message = message
        self.signature = None

    def serialize(self):
        return json.dumps({
            "sender": self.sender_pubkey.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode(),
            "receiver": self.receiver,
            "amount": self.amount,
            "message": self.message
        }, sort_keys=True).encode()

    def sign(self, private_key):
        self.signature = sign_data(private_key, self.serialize())

    def verify(self):
        return verify_signature(
            self.sender_pubkey,
            self.signature,
            self.serialize()
        )

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": [
                {
                    "data": t.serialize().decode(),
                    "signature": t.signature.hex() if t.signature else None
                } for t in self.transactions
            ],
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    def mine(self, difficulty=3):
        prefix = "0" * difficulty
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    def __init__(self, difficulty=3):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        block = Block(0, [], "0")
        block.mine(self.difficulty)
        return block

    def add_block(self, transactions):
        # verify transaction signatures
        for t in transactions:
            if not t.verify():
                raise ValueError("Invalid transaction signature!")

        new_block = Block(
            len(self.chain),
            transactions,
            self.chain[-1].hash
        )
        new_block.mine(self.difficulty)
        self.chain.append(new_block)
        return new_block

if __name__ == "__main__":
    # create blockchain
    chain = Blockchain()

    # 2 users
    alice_priv, alice_pub = generate_rsa_keypair()
    bob_priv, bob_pub = generate_rsa_keypair()

    # create a transaction
    tx = Transaction(alice_pub, "Bob", 50, "Payment for services")
    tx.sign(alice_priv)

    print("Transaction valid?", tx.verify())

    # add to blockchain
    block = chain.add_block([tx])
    print("Block mined:", block.hash)
