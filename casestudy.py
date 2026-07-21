import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

Customers = pd.DataFrame(pd.read_csv('F:\Pandas\Customer.csv'))
Product_Hierarchy = pd.DataFrame(pd.read_csv('F:\Pandas\prod_cat_info.csv'))
Customer_Final = pd.DataFrame(pd.read_csv('F:\Pandas\Transactions.csv'))


print(Customers.columns)
print(Product_Hierarchy.columns)
print(Customer_Final.columns)