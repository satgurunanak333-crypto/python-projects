import pandas as pd

def personal_finance_summary(file_name):
    try:
        df = pd.read_csv(file_name)

        print("CSV File Loaded Successfully!\n")

        total_income = df[df["type"] == "income"]["amount"].sum()
        total_expense = df[df["type"] == "expense"]["amount"].sum()
        savings = total_income - total_expense

        print(f"Total Income: ₹{total_income}")
        print(f"Total Expenses: ₹{total_expense}")
        print(f"Savings: ₹{savings}\n")

        print("Category-wise Expenses:")
        category_expense = df[df["type"] == "expense"].groupby("category")["amount"].sum()
        print(category_expense)

    except FileNotFoundError:
        print("CSV file not found. Please check the file name.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    file_name = "expenses.csv"   # make sure this file exists
    personal_finance_summary(file_name)
