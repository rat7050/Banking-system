import random
from datetime import datetime
from data import accounts


def create_account(name, phone, pin):
    if len(pin) != 4 or not pin.isdigit():
        return None

    acc_no = random.randint(1000, 9999)

    while acc_no in accounts:
        acc_no = random.randint(1000, 9999)

    accounts[acc_no] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0,
        "history": []
    }

    return acc_no


def login(acc_no, pin):
    if acc_no in accounts:
        if accounts[acc_no]["pin"] == pin:
            return True

    return False


def get_balance(acc_no):
    return accounts[acc_no]["balance"]


def deposit(acc_no, amount):
    if amount <= 0:
        return False

    accounts[acc_no]["balance"] += amount

    time = datetime.now().strftime("%d-%m-%Y %H:%M")

    accounts[acc_no]["history"].append(
        "Deposited " + str(amount) + " on " + time
    )

    return True


def withdraw(acc_no, amount):
    if amount <= 0:
        return False

    if amount > accounts[acc_no]["balance"]:
        return False

    accounts[acc_no]["balance"] -= amount

    time = datetime.now().strftime("%d-%m-%Y %H:%M")

    accounts[acc_no]["history"].append(
        "Withdraw " + str(amount) + " on " + time
    )

    return True


def transfer(acc_no, receiver, amount):
    if receiver not in accounts:
        return False

    if receiver == acc_no:
        return False

    if amount <= 0:
        return False

    if amount > accounts[acc_no]["balance"]:
        return False

    accounts[acc_no]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    time = datetime.now().strftime("%d-%m-%Y %H:%M")

    accounts[acc_no]["history"].append(
        "Transferred " + str(amount) +
        " to " + str(receiver) +
        " on " + time
    )

    accounts[receiver]["history"].append(
        "Received " + str(amount) +
        " from " + str(acc_no) +
        " on " + time
    )

    return True


def get_history(acc_no):
    return accounts[acc_no]["history"]


def change_pin(acc_no, old_pin, new_pin):
    if accounts[acc_no]["pin"] != old_pin:
        return False

    if len(new_pin) != 4 or not new_pin.isdigit():
        return False

    accounts[acc_no]["pin"] = new_pin

    return True
