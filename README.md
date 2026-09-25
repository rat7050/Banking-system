# 🏦 Banking System

A simple **Banking Management System** built with **Python and Streamlit**.

This project simulates common banking operations through an interactive web interface, including account creation, PIN-based login, balance checking, deposits, withdrawals, money transfers, transaction history, PIN changes, and logout.

> **Note:** This project is designed for learning and demonstration purposes. It is not intended for real-world banking or financial transactions.

---

# ✨ Features

* 👤 Create a new bank account
* 🔐 4-digit PIN-based login
* 💰 Check account balance
* ➕ Deposit money
* ➖ Withdraw money
* 🔄 Transfer money between accounts
* 📜 View transaction history
* 🔑 Change account PIN
* 🚪 Logout
* 🎨 Simple Streamlit interface
* 🧩 Modular Python backend

---

# 🏗️ Application Architecture

```text
                    ┌────────────────────┐
                    │       User         │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │    Streamlit UI    │
                    │      app.py        │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Banking Functions  │
                    │    banking.py      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Account Data       │
                    │     data.py        │
                    └────────────────────┘
```

---

# 📁 Project Structure

```text
Banking-system/
│
├── app.py
├── banking.py
├── data.py
├── requirements.txt
└── README.md
```

### File Description

| File               | Purpose                                 |
| ------------------ | --------------------------------------- |
| `app.py`           | Streamlit frontend and application flow |
| `banking.py`       | Banking operations and business logic   |
| `data.py`          | Stores account data                     |
| `requirements.txt` | Project dependency                      |
| `README.md`        | Project documentation                   |

The current repository contains these files on the `main` branch.

---

# 🛠️ Tech Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| 🐍 Python    | Core programming          |
| 🎈 Streamlit | Web interface             |
| 🎲 Random    | Account number generation |
| 🕒 Datetime  | Transaction timestamps    |

The project currently requires Streamlit only.

---

# 🔄 Banking Workflow

```text
Start Application
       ↓
Create Account / Login
       ↓
     Login
       ↓
   Dashboard
       │
       ├── Check Balance
       │
       ├── Deposit
       │
       ├── Withdraw
       │
       ├── Transfer
       │
       ├── Transaction History
       │
       ├── Change PIN
       │
       └── Logout
```

---

# 👤 Create Account

Users can create a new account by entering:

* Name
* Phone number
* 4-digit PIN

The system validates that the PIN contains exactly four digits. It then generates a unique 4-digit account number and initializes the account with a zero balance and empty transaction history.

Example:

```text
Name: Ratnesh
Phone: 9876543210
PIN: 1234

Account created successfully

Account Number: 5821
```

---

# 🔐 Login

Users log in using:

```text
Account Number
+
PIN
```

The system checks the account number and corresponding PIN before allowing access to the banking dashboard.

---

# 💰 Dashboard

After successful login, the dashboard displays:

```text
Account Number
Current Balance
```

The sidebar provides access to all banking operations.

---

# ➕ Deposit Money

Users can deposit money into their account.

Example:

```text
Deposit: ₹5,000
```

The amount is added to the current balance and a transaction entry is added to the account history.

---

# ➖ Withdraw Money

Users can withdraw money from their account.

The system checks:

```text
Amount > 0
AND
Amount <= Current Balance
```

A withdrawal is rejected when the requested amount is greater than the available balance.

---

# 🔄 Transfer Money

Users can transfer money to another account.

The system validates that:

* Receiver account exists
* Receiver is not the same as sender
* Transfer amount is greater than zero
* Sender has sufficient balance

Both accounts receive transaction-history entries after a successful transfer.

Example:

```text
Sender:   1234
Receiver: 5678
Amount:   ₹2,000
```

Result:

```text
₹2,000 deducted from account 1234
₹2,000 added to account 5678
```

---

# 📜 Transaction History

Each account maintains a list of transaction messages.

Example:

```text
Deposited 5000 on 25-09-2026 21:30

Withdraw 1000 on 25-09-2026 21:45

Transferred 500 to 5678 on 25-09-2026 22:00
```

The application displays the stored transaction history for the logged-in account.

---

# 🔑 Change PIN

Users can change their existing PIN by providing:

```text
Old PIN
New PIN
```

The new PIN must contain exactly four digits.

---

# 🚪 Logout

The logout option clears the current login state and returns the user to the login screen.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/rat7050/Banking-system.git
```

```bash
cd Banking-system
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local Streamlit URL, usually:

```text
http://localhost:8501
```

---

# 🧠 Core Logic

The backend logic is separated into `banking.py`.

The main functions are:

```python
create_account()
login()
get_balance()
deposit()
withdraw()
transfer()
get_history()
change_pin()
```

This separation keeps the Streamlit interface in `app.py` and the banking operations in `banking.py`.

---

# 🗂️ Data Storage

The current project stores accounts in a Python dictionary imported from `data.py`.

Each account follows a structure similar to:

```python
{
    "name": "Ratnesh",
    "phone": "9876543210",
    "pin": "1234",
    "balance": 5000,
    "history": []
}
```

Account numbers are generated randomly and checked to avoid duplicates.

---

# 📊 Example Use Case

Suppose a user creates an account:

```text
Account Number: 4521
Initial Balance: ₹0
```

Then performs:

```text
Deposit ₹10,000
       ↓
Balance = ₹10,000

Withdraw ₹2,000
       ↓
Balance = ₹8,000

Transfer ₹3,000
       ↓
Balance = ₹5,000
```

The system records these operations in the transaction history.

---

# 🎯 Project Objective

The objective of this project is to understand how a basic banking application can be built using:

```text
Python
   +
Functions
   +
Data Structures
   +
Streamlit
   ↓
Interactive Banking System
```

It provides practical experience with application flow, user input validation, state management, modular programming, and transaction logic.

---

# 🔒 Current Limitations

This is a learning/demo project and currently has several limitations:

* Data is stored in memory
* Accounts are not persisted in a database
* PINs are stored directly in application data
* Account numbers are only 4 digits
* No real banking authentication
* No transaction database
* No multi-user security layer
* No audit logging
* No real financial processing

Because account information is maintained in a Python dictionary, restarting the application clears the in-memory account data.

---

# 🚧 Future Improvements

Possible upgrades:

* [ ] 🗄️ SQLite/MySQL database
* [ ] 🔐 Password/PIN hashing
* [ ] 👤 User authentication
* [ ] 🧾 Permanent transaction records
* [ ] 💳 Account types
* [ ] 📅 Transaction dates and filtering
* [ ] 📊 Banking analytics dashboard
* [ ] 🔍 Transaction search
* [ ] 📥 Download account statement
* [ ] 🏦 Multiple account support
* [ ] 🔒 Better security controls
* [ ] 🧪 Automated testing
* [ ] ☁️ Cloud deployment
* [ ] 📱 Improved responsive UI

---

# 🎓 Learning Outcomes

This project helps demonstrate knowledge of:

* Python programming
* Functions and modular programming
* Dictionaries and lists
* Input validation
* Conditional logic
* State management
* Streamlit
* Transaction processing
* Basic authentication concepts
* Application design

---

# 📸 Application Modules

```text
┌──────────────────────────────────┐
│         🏦 Banking System        │
├──────────────────────────────────┤
│                                  │
│  🔐 Login                        │
│  👤 Create Account               │
│                                  │
└──────────────────────────────────┘

After Login:

┌──────────────────────────────────┐
│        Banking Dashboard         │
├──────────────────────────────────┤
│                                  │
│  💰 Dashboard                    │
│  ➕ Deposit                      │
│  ➖ Withdraw                     │
│  🔄 Transfer                     │
│  📜 Transaction History          │
│  🔑 Change PIN                   │
│  🚪 Logout                       │
│                                  │
└──────────────────────────────────┘
```

---

# 👨‍💻 Author

## Ratnesh Kumar

**B.Tech — Artificial Intelligence & Data Science**

GitHub: [@rat7050](https://github.com/rat7050)

---

# ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for educational and learning purposes.
