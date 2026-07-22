import pandas as pd

# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

Customers = pd.DataFrame(pd.read_csv('F:\Pandas\Customer.csv'))
Product_Hierarchy = pd.DataFrame(pd.read_csv('F:\Pandas\prod_cat_info.csv'))
Transaction = pd.DataFrame(pd.read_csv('F:\Pandas\Transactions.csv'))


# print(Customers.columns, '\n')
# print(Product_Hierarchy.columns, '\n')
# print(Transaction.columns, '\n')


# 1 - Merge the datasets Customers, Product Hierarchy and Transactions as Customer_Final. Ensure tokeep all customers who have done transactions with us and select the join type accordingly. 

Temp_Merge = pd.merge(Transaction, Customers, how='inner', left_on=['cust_id'], right_on=['customer_Id'])
Customer_Final = pd.merge(Product_Hierarchy, Temp_Merge, how='inner', left_on=['prod_cat_code'], right_on=['prod_cat_code'])
# print(Customer_Final)



# 2 - Prepare a summary report for the merged data set. 
#      A -  Get the column names and their corresponding data types
print("Customer Final")
print(Customer_Final.dtypes, '\n\n')


#      B -  Top/Bottom 10 observations
print("Top")
print(Customer_Final.head(5))
print("\n\n\nBottom\n\n\n")
print(Customer_Final.tail(5))