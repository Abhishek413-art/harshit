# bank_loan_approval.py
import streamlit as st
st.text_input("Customer name")

def check_loan_eligibility(salary, age):
    # Simple eligibility criteria
    if salary >= 30000 or age >= 25:
        return True
    else:
        return False

def main():
    st.title("Bank Loan Approval")

    # Input fields for user information
    salary = st.number_input("Enter your salary (Rs)", min_value=0)
    age = st.number_input("Enter your age", min_value=0)

    # Button to check eligibility
    if st.button("Check Eligibility"):
        if check_loan_eligibility(salary, age):
            st.success("Congratulations! Your loan is approved.")
        else:
            st.error("Sorry, your loan cannot be approved based on the provided information.")

if __name__ == "__main__":
    main()
