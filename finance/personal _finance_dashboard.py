import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("finance_data.csv", parse_dates=["Date"])

st.title("Personal Finance Dashboard")

# Show raw data
st.subheader("Transactions")
st.dataframe(df)

# Calculate totals
total_income = df[df['Type']=='Income']['Amount'].sum()
total_expense = df[df['Type']=='Expense']['Amount'].sum()
balance = total_income - total_expense

st.subheader("Summary")
st.write(f"Total Income: ₹{total_income}")
st.write(f"Total Expenses: ₹{total_expense}")
st.write(f"Balance: ₹{balance}")

# Expenses by Category
st.subheader("Expenses by Category")
expense_data = df[df['Type']=='Expense'].groupby('Category')['Amount'].sum()
fig, ax = plt.subplots()
expense_data.plot(kind='bar', ax=ax, color='tomato')
plt.ylabel("Amount (₹)")
st.pyplot(fig)
