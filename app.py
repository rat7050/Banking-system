import streamlit as st

from banking import (
    create_account,
    login,
    get_balance,
    deposit,
    withdraw,
    transfer,
    get_history,
    change_pin
)


st.title("Banking System")


if "login" not in st.session_state:
    st.session_state.login = False

if "account" not in st.session_state:
    st.session_state.account = None


if not st.session_state.login:

    st.subheader("Login")

    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Login"):

        if acc_no.isdigit():

            if login(int(acc_no), pin):
                st.session_state.login = True
                st.session_state.account = int(acc_no)
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Wrong account number or PIN")

        else:
            st.error("Enter a valid account number")

    st.divider()

    st.subheader("Create Account")

    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    new_pin = st.text_input("Create 4 Digit PIN", type="password")

    if st.button("Create Account"):

        acc = create_account(name, phone, new_pin)

        if acc is not None:
            st.success("Account created successfully")
            st.info("Your account number is: " + str(acc))
        else:
            st.error("PIN should contain 4 digits")


else:

    acc_no = st.session_state.account

    st.sidebar.title("Banking System")

    option = st.sidebar.selectbox(
        "Choose option",
        [
            "Dashboard",
            "Deposit",
            "Withdraw",
            "Transfer",
            "Transaction History",
            "Change PIN",
            "Logout"
        ]
    )

    if option == "Dashboard":

        st.header("Dashboard")
        st.write("Account Number:", acc_no)

        balance = get_balance(acc_no)

        st.metric("Current Balance", "₹ " + str(balance))


    elif option == "Deposit":

        st.header("Deposit Money")

        amount = st.number_input("Enter amount", min_value=1)

        if st.button("Deposit"):

            if deposit(acc_no, amount):
                st.success("Money deposited successfully")


    elif option == "Withdraw":

        st.header("Withdraw Money")

        amount = st.number_input("Enter amount", min_value=1)

        if st.button("Withdraw"):

            if withdraw(acc_no, amount):
                st.success("Money withdrawn successfully")
            else:
                st.error("Not enough balance")


    elif option == "Transfer":

        st.header("Transfer Money")

        receiver = st.number_input(
            "Receiver Account Number",
            min_value=1000,
            step=1
        )

        amount = st.number_input("Amount", min_value=1)

        if st.button("Transfer"):

            if transfer(acc_no, receiver, amount):
                st.success("Money transferred successfully")
            else:
                st.error("Transfer failed")


    elif option == "Transaction History":

        st.header("Transaction History")

        history = get_history(acc_no)

        if len(history) == 0:
            st.write("No transactions yet")
        else:
            for item in history:
                st.write(item)


    elif option == "Change PIN":

        st.header("Change PIN")

        old_pin = st.text_input("Old PIN", type="password")
        new_pin = st.text_input("New PIN", type="password")

        if st.button("Change PIN"):

            if change_pin(acc_no, old_pin, new_pin):
                st.success("PIN changed successfully")
            else:
                st.error("PIN change failed")


    elif option == "Logout":

        st.session_state.login = False
        st.session_state.account = None

        st.success("Logged out")
        st.rerun()
