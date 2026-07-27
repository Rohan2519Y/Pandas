import pandas as pd
import matplotlib.pyplot as plt

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
print(Customer_Final.columns)



# 2 - Prepare a summary report for the merged data set. 
#      A -  Get the column names and their corresponding data types
# print("Customer Final")
# print(Customer_Final.dtypes, '\n\n')


#      B -  Top/Bottom 10 observations
# print("Top")
# print(Customer_Final.head(5))
# print("\n\n\nBottom\n\n\n")
# print(Customer_Final.tail(5))


#       C - “Five-number summary” for continuous variables (min, Q1, median, Q3 and max)
# print("Min : \n", Customer_Final['total_amt'].min, '\n\n')
# print("Max : \n", Customer_Final['total_amt'].max, '\n\n')
# print("Median  : \n", Customer_Final['total_amt'].median, '\n\n')
# print(Customer_Final.describe())


#       D - Frequency tables for all the categorical variables
# print("City_Code\n\n", pd.crosstab(index = Customer_Final['Gender'], columns=Customer_Final['city_code']))
# print("\n\n\nProd_Cat\n\n", pd.crosstab(index = Customer_Final['Gender'], columns=Customer_Final['prod_cat']))
# print("\n\n\nProd_Subcat\n\n", pd.crosstab(index = Customer_Final['Gender'], columns=Customer_Final['prod_subcat']))
# print("\n\n\nStore_type\n\n", pd.crosstab(index = Customer_Final['Gender'], columns=Customer_Final['Store_type']))




# 3 - Generate histograms for all continuous variables and frequency bars for categorical variables.
# Customer_Final['city_code'].hist()
# plt.title("City Code")
# plt.show()
# Customer_Final['city_code'].value_counts().plot(kind='bar')
# plt.show()


# Customer_Final['prod_cat'].hist()
# plt.title("Product Category")
# plt.show()
# Customer_Final['prod_cat'].value_counts().plot(kind='bar')
# plt.show()


# Customer_Final['prod_subcat'].hist()
# plt.title("Product SubCategory")
# plt.show()
# Customer_Final['prod_subcat'].value_counts().plot(kind='bar')
# plt.show()


# Customer_Final['Store_type'].hist()
# plt.title("Store Type")
# plt.show()
# Customer_Final['Store_type'].value_counts().plot(kind='bar')
# plt.show()





# 4 - Calculate the following information using the merged dataset :
#       A - Time period of the available transaction data
# Customer_Final['Time_Peroid'] = pd.Timestamp.now() - pd.to_datetime(Customer_Final['tran_date'], dayfirst=True, format='mixed')
# print(Customer_Final['Time_Period])


#       B - Count of transactions where the total amount of transaction was negative
# print("Count", Customer_Final.loc[(Customer_Final['total_amt']) < 0,'total_amt'].count())




# 5 - Analyze which product categories are more popular among females vs male customers.
# print(pd.crosstab(index=Customer_Final['Gender'], columns=Customer_Final['prod_cat']).idxmax(axis=1))




# 6 - Which City code has the maximum customers and what was the percentage of customers from that city?
# city = Customer_Final.groupby("city_code")["cust_id"].nunique()

# print("City Code:", city.idxmax())
# print("Percentage:", (city.max() / city.sum()) * 100)




# 7 - Which store type sells the maximum products by value and by quantity?
# print(Customer_Final.groupby("Store_type")['Qty'].sum().idxmax())




# 8 - What was the total amount earned from the "Electronics" and "Clothing" categories from Flagship Stores
# FS = Customer_Final.loc[(Customer_Final['Store_type'] == 'Flagship store' ) & ((Customer_Final['prod_cat'] == 'Electronics') | (Customer_Final['prod_cat'] == 'Clothing'))]
# print(FS['total_amt'].max())




# 9 - What was the total amount earned from "Male" customers under the "Electronics" category?
# ME = Customer_Final.loc[(Customer_Final['Gender'] == 'M') & (Customer_Final['prod_cat'] == 'Electronics')]
# print(ME['total_amt'].sum())




# 10 - How many customers have more than 10 unique transactions, after removing all transactions which have any negative amounts?
# CT = Customer_Final.loc[Customer_Final['total_amt'] > 0].groupby('cust_id')['transaction_id'].nunique()
# print(CT[CT > 10])
# print(CT[CT > 10].count())




# 11 - For all customers aged between 25 - 35, find out:
Customer_Final["DOB"] = pd.to_datetime(Customer_Final["DOB"], format="mixed", dayfirst=True, errors="coerce")
Customer_Final['Age'] = (pd.Timestamp.today().year - Customer_Final['DOB'].dt.year)
Cust_age = Customer_Final.loc[Customer_Final['Age'].between(25, 35)]
# print(Cust_age)


#       A - What was the total amount spent for “Electronics” and “Books” product categories?
# print(Cust_age.loc[(Cust_age['prod_cat'] == 'Electronics') | (Cust_age['prod_cat'] == 'Books')]['total_amt'].sum())


#       B - What was the total amount spent by these customers between 1st Jan, 2014 to 1st Mar, 2014?
Cust_age['tran_date'] = pd.to_datetime(Cust_age['tran_date'], format='mixed', dayfirst=True, errors='coerce')
print(Cust_age[(Cust_age['tran_date'] > '2014-01-01') & (Cust_age['tran_date'] < '2014-03-01') & ((Cust_age['prod_cat'] == 'Electronics') | (Cust_age['prod_cat'] == 'Books'))]['total_amt'].sum())