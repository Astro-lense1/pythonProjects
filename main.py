import pandas as pd


#load the sales data from a CSV file
sales_data = pd.read_csv('sales_data.csv')


def analyze_sales_data(data):
 #Calculate total sales_data
 total_sales = data ['Revenue'].sum()

 #Calculate average sells on products
 average_sales = data ['Revenue'].mean

   #Calculate highest selling product
 best_selling_product = data ['Product'].value_counts().idxmax()

 month_highest_sales = data.groupby('Month')['Revenue'].sum().idxmax()



 print("sales Data Analysis")
 print("-------------------")
 print(f"Total Sales ${total_sales}")
 print(f"Average sells per month ${average_sales}")
 print(f"best selling products ${best_selling_product}")
 print(f"Month highest sales: ${month_highest_sales}")

analyze_sales_data(sales_data)
