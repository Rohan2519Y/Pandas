import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)


# 1 -   Import claims_data.csv and cust_data.csv which is provided to you and 
#       combine the two datasets appropriately to create a 360-degree view of 
#       the data. Use the same for the subsequent questions. 

Claim = pd.read_csv('F:/Pandas/casestudy3/claims.csv')
Customer = pd.read_csv('F:/Pandas/casestudy3/cust_demographics.csv')
Claim_Cust = pd.merge(Claim, Customer, left_on=['customer_id'], right_on=['CUST_ID'])

# print(Claim)
# print(Customer)
# print(Claim_Cust)




# 2 -   Perform a data audit for the datatypes and find out if there are any 
#       mismatch within the current datatypes of the columns and their 
#       business significance.

Claim_Cust['claim_date'] = pd.to_datetime(Claim_Cust['claim_date'])
Claim_Cust['DateOfBirth'] = pd.to_datetime(Claim_Cust['DateOfBirth'])
# print(Claim_Cust.dtypes)




# 3 -   Convert the column claim_amount to numeric. Use the appropriate 
#       modules/attributes to remove the $ sign.

Claim_Cust['claim_amount'] = pd.to_numeric(Claim_Cust['claim_amount'].str.replace('$', '', regex=False))
# print(Claim_Cust['claim_amount'])




# 4 -   Of all the injury claims, some of them have gone unreported with the 
#       police. Create an alert flag (1,0) for all such claims.

