import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)

Customer_Acquisition = pd.read_csv('F:/Pandas/casestudy2/Customer Acqusition.csv')
Spend = pd.read_csv('F:/Pandas/casestudy2/spend.csv')
Repayment = pd.read_csv('F:/Pandas/casestudy2/Repayment.csv')

Full_Merge = pd.merge(Repayment, (pd.merge(Customer_Acquisition, Spend, on=['Customer'])), on=['Customer'], suffixes=('_Repay', '_Spend'))


# print(Customer_Acquisition)
# print(Spend)
# print(Repayment)

print(Full_Merge)

# 1. In the above dataset
#           A - In case age is less than 18, replace it with mean of age values

# MeanAge = Customer_Acquisition.loc[Customer_Acquisition['Age'] < 18, 'Age'].mean()
# Customer_Acquisition.loc[Customer_Acquisition['Age'] < 18, 'Age'] = int(MeanAge)
# print(Customer_Acquisition)


#           B - In case spend amount is more than the limit, replace it with 50% of that customer’s limit.  
#           (customer’s limit provided in acquisition table is the per transaction limit on his card)

# Full_Merge.loc[Full_Merge['Amount_Spend'] > Full_Merge['Limit'], 'Amount_Spend']= Full_Merge['Limit'] * 0.5
# print(Full_Merge.loc[ :,['Limit', 'Amount_Spend']])


#           C - Incase the repayment amount is more than the limit, replace the repayment with the limit.

# Full_Merge.loc[Full_Merge['Amount_Repay'] > Full_Merge['Limit'], 'Amount_Repay'] = Full_Merge['Limit']
# print(Full_Merge.loc[:,['Limit', 'Amount_Repay']])