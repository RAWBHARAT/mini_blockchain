# Mini Blockchain Project (Python)

## 🚀 Mini Blockchain Project (Python)

This project is a **simple educational blockchain implementation**
written in Python.\
It simulates key blockchain concepts such as:

-   Block creation\
-   SHA-256 hashing\
-   Linking blocks with previous hashes\
-   Proof-of-Work mining\
-   Transactions\
-   **Digital signatures using `cryptography` library (RSA keys)**\
-   Chain validation

This project is designed for learning and demonstration purposes, not
for production use.

## 📦 Features

### 🔗 Blockchain

-   Creates new blocks
-   Links blocks using previous block hash
-   Calculates SHA-256 hash for each block
-   Implements simple Proof-of-Work (difficulty based)
-   Full chain validation

### 💸 Transactions

-   A `Transaction` class supports:
    -   Sender
    -   Receiver
    -   Amount
    -   Timestamp

### 🔐 Digital Signatures

Using the **`cryptography`** library: - Generate RSA private/public
keys - Sign transactions - Verify transaction authenticity before adding
to a block

### 🛡 Verification

-   Rejects tampered or unsigned transactions
-   Ensures block integrity
-   Verifies the entire chain

## 🛠 Requirements

Install Python 3.8+ and the dependencies:

``` bash
pip install cryptography
```

If you're using a virtual environment:

``` bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
pip install cryptography
```

## 📁 Project Structure

    blockchain/
    │
    ├── blockchain.py     # Main Python script
    └── README.md         # Project documentation

## ▶️ How to Run

1.  Clone or download your repository.
2.  Navigate to the folder:

``` bash
cd blockchain
```

3.  Run the Python script:

``` bash
python blockchain.py
```

You should see output like:

    Transaction valid? True
    Block mined: 000abc4f3a9...
    Chain valid? True

## 🔧 How It Works

1️⃣ Generate RSA keys\
Users generate private & public keys.

2️⃣ Create a transaction\
A transaction is signed using the private key.

3️⃣ Verify signature\
The blockchain checks the signature using the sender's public key.

4️⃣ Mine a block\
A valid transaction is added to a block after Proof-of-Work.

5️⃣ Add block to chain\
The block is linked using the previous block's hash.

## 📚 Technologies Used

-   Python 3
-   SHA-256 (`hashlib`)
-   RSA Digital Signatures (`cryptography`)
-   Virtual Environment (optional)

## ⚠️ Disclaimer

This is a simplified educational blockchain, not intended for real
financial use.\
It does not include networking, distributed consensus, wallets, or
security hardened code.

## ⭐ Future Improvements

-   Wallet system with stored key pairs\
-   Multiple transactions per block\
-   Flask/REST API for interacting with the chain\
-   Peer-to-peer network simulation\
-   SQLite or file-based block storage

## 📌 Author

**Bharat Vishwakarma**\
Python \| Blockchain Enthusiast
