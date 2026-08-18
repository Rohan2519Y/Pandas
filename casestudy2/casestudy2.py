import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)

Customer_Acquisition = pd.read_csv('F:/Pandas/casestudy2/Customer Acqusition.csv')
Spend = pd.read_csv('F:/Pandas/casestudy2/spend.csv')
Repayment = pd.read_csv('F:/Pandas/casestudy2/Repayment.csv')

Full_Merge = pd.merge(Repayment, (pd.merge(Customer_Acquisition, Spend, on=['Customer'])), on=['Customer'], suffixes=('_Repay', '_Spend'))
Full_Merge['SpendMonthname'] = pd.to_datetime(Spend['Month'], dayfirst=True, format='mixed').dt.month_name()
Full_Merge['RepayMonthname'] = pd.to_datetime(Repayment['Month'], dayfirst=True, format='mixed').dt.month_name()
Full_Merge['SpendYear'] = pd.to_datetime(Spend['Month'], dayfirst=True, format='mixed').dt.year.astype(int)
Full_Merge['RepayYear'] = pd.to_datetime(Repayment['Month'], dayfirst=True, format='mixed').dt.year.astype(int)

# print(Customer_Acquisition)
# print(Spend)
# print(Repayment)

# print(Full_Merge)

# 1. In the above dataset
#           A - In case age is less than 18, replace it with mean of age values

# MeanAge = Customer_Acquisition.loc[Customer_Acquisition['Age'] < 18, 'Age'].mean()
# Customer_Acquisition.loc[Customer_Acquisition['Age'] < 18, 'Age'] = int(MeanAge)
# print(Customer_Acquisition)


#           B - In case spend amount is more than the limit, replace it with 50% of that customer’s limit.  
#           (customer’s limit provided in acquisition table is the per transaction limit on his card)

# Full_Merge.loc[Full_Merge['Amount_Spend'] > Full_Merge['Limit'], 'Amount_Spend'] = Full_Merge['Limit'] * 0.5
# print(Full_Merge.loc[ :,['Limit', 'Amount_Spend']])


#           C - Incase the repayment amount is more than the limit, replace the repayment with the limit.

# Full_Merge.loc[Full_Merge['Amount_Repay'] > Full_Merge['Limit'], 'Amount_Repay'] = Full_Merge['Limit']
# print(Full_Merge.loc[:,['Limit', 'Amount_Repay']])




# 2. From the above dataset create the following summaries: 
#           A - How many distinct customers exist?
# print(Customer_Acquisition.groupby('Customer').size().count())




#           B - How many distinct categories exist?
# print(Customer_Acquisition.groupby('Segment').size().count())




#           C - What is the average monthly spend by customers?
Spend['Monthname'] = pd.to_datetime(Spend['Month'], dayfirst=True, format='mixed').dt.month_name()
# print(Spend.groupby(['Monthname'])['Amount'].mean())




#           D - What is the average monthly repayment by customers? 
Repayment['Monthname'] = pd.to_datetime(Spend['Month'], dayfirst=True, format='mixed').dt.month_name()
# print(Repayment.groupby(['Monthname'])['Amount'].mean())




#           E - If the monthly rate of interest is 2.9%, what is the profit for the bank for each month? 
#           (Profit is defined as interest earned on Monthly Profit. Monthly Profit = Monthly 
#           repayment  – Monthly spend. Interest is earned only on positive profits and not on negative amounts) 
SpendMonthProfit = Full_Merge.groupby(['SpendMonthname'])['Amount_Spend'].sum()
RepayMonthProfit = Full_Merge.groupby(['RepayMonthname'])['Amount_Repay'].sum()
# print(SpendMonthProfit)
# print(RepayMonthProfit)
# print((RepayMonthProfit - SpendMonthProfit)[(RepayMonthProfit - SpendMonthProfit) > 0] * 0.029)




#              F - What are the top 5 product types? 
# print(Spend.groupby(['Type']).count().nlargest(5, 'Customer').iloc[:, 0])




#              G - Which city is having maximum spend?
# print(Full_Merge.groupby(['City'])['Amount_Spend'].sum().nlargest(1)) 




#              H - Which age group is spending more money?
# print(Full_Merge.groupby(['Age'])['Amount_Spend'].sum().nlargest(1))




#              I - Who are the top 10 customers in terms of repayment?
# print(Full_Merge.groupby(['Customer'])['Amount_Spend'].sum().nlargest(10))




# 3 - Calculate the city wise spend on each product on yearly basis. Also include a graphical representation for the same.
Spend_Prdt = Full_Merge.groupby(['City', 'Type', 'SpendYear'])['Amount_Spend'].sum().reset_index()
# print(Spend_Prdt)
# for city in Spend_Prdt['City'].unique():
#     data = Spend_Prdt[Spend_Prdt['City'] == city]

#     plt.bar(
#         data['SpendYear'].astype(str) + '-' + data['Type'],
#         data['Amount_Spend']
#     )

# plt.title(f'Yearly Spend by Product - {city}')
# plt.xlabel('Year - Product')
# plt.ylabel('Amount Spend')
# plt.xticks(rotation=45)
# plt.show()




#  4 - Create Graph for
#               A - Monthly comparison of total spends, city wise
# Chart = Full_Merge.groupby(['City'])['Amount_Spend'].sum()
# plt.bar(Chart.index, Chart.values)
# plt.show()
# print(Chart.index)




#               B - Comparison of yearly spend on air tickets
Spend['Year'] = pd.to_datetime(Spend['Month'], dayfirst=True, format='mixed').dt.year.astype(int)
Chart = Spend.loc[Spend['Type'] == 'AIR TICKET'].groupby(['Year']).count()
plt.bar(Chart.index.astype(str), Chart['Month'])
plt.show()
# print(Chart.index)