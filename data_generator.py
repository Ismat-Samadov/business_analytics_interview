import pandas as pd
import random
num_cardholders = 1000
average_spending = 200
percentage_utilization = 0.5
cashback_rate = 0.05
cost_of_cashback_program = 10000
cardholder_ids = list(range(1, num_cardholders + 1))
supermarket_spending = [random.randint(150, 250) for _ in range(num_cardholders)]
cashback_earned = [spending * percentage_utilization * cashback_rate for spending in supermarket_spending]
total_cashback_expenses = [cashback * percentage_utilization for cashback in cashback_earned]
net_profit_loss = [cashback - cost_of_cashback_program for cashback in total_cashback_expenses]
data = {
    "Cardholder ID": cardholder_ids,
    "Supermarket Spending": supermarket_spending,
    "Cashback Earned": cashback_earned,
    "Total Cashback Expenses": total_cashback_expenses,
    "Net Profit/Loss": net_profit_loss
}
df = pd.DataFrame(data)
totals = pd.DataFrame({
    "Cardholder ID": ["Totals"],
    "Supermarket Spending": [df["Supermarket Spending"].sum()],
    "Cashback Earned": [df["Cashback Earned"].sum()],
    "Total Cashback Expenses": [df["Total Cashback Expenses"].sum()],
    "Net Profit/Loss": [df["Net Profit/Loss"].sum()]
})
df = pd.concat([df, totals], ignore_index=True)
df.to_excel("cashback_analysis.xlsx", index=False)