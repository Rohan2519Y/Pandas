import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)


# 1 -   Import claims_data.csv and cust_data.csv which is provided to you and 
#       combine the two datasets appropriately to create a 360-degree view of 
#       the data. Use the same for the subsequent questions. 

Claim = pd.read_csv('F:/Pandas/casestudy3/claims.csv')
Customer = pd.read_csv('F:/Pandas/casestudy3/cust_demographics.csv')
Claim_Cust = pd.merge(Claim, Customer, left_on=['customer_id'], right_on=['CUST_ID'])

# print(Claim)
# print(Customer)
# print(Claim_Cust)
Customer['DateOfBirth'] = pd.to_datetime(Customer['DateOfBirth'], format='mixed')




# 2 -   Perform a data audit for the datatypes and find out if there are any 
#       mismatch within the current datatypes of the columns and their 
#       business significance.

Claim_Cust['claim_date'] = pd.to_datetime(Claim_Cust['claim_date'], format='mixed')
Claim_Cust['DateOfBirth'] = pd.to_datetime(Claim_Cust['DateOfBirth'], format='mixed')
# print(Claim_Cust.dtypes)




# 3 -   Convert the column claim_amount to numeric. Use the appropriate 
#       modules/attributes to remove the $ sign.

Claim_Cust['claim_amount'] = pd.to_numeric(Claim_Cust['claim_amount'].str.replace('$', '', regex=False))
# print(Claim_Cust['claim_amount'])




# 4 -   Of all the injury claims, some of them have gone unreported with the 
#       police. Create an alert flag (1,0) for all such claims.

Claim['Flag'] = 0
Claim.loc[Claim['police_report'] == 'No', 'Flag'] = 1
# print(Claim)




# 5 -   One customer can claim for insurance more than once and in each 
#       claim, multiple categories of claims can be involved. However, customer 
#       ID should remain unique.  
#       Retain the most recent observation and delete any duplicated records in 
#       the data based on the customer ID column.

# print(Claim_Cust.sort_values(by='claim_date', ascending=False).groupby(['customer_id']).first())




# 6 -   Check for missing values and impute the missing values with an 
#       appropriate value. (mean for continuous and mode for categorical)

Claim['claim_amount'] = Claim['claim_amount'].str.replace('$', '', regex=False)
Claim['claim_amount'] = Claim['claim_amount'].astype(float)
Claim_Cust['claim_amount'] = Claim_Cust['claim_amount'].replace('$', '', regex=False)
Claim_Cust['claim_amount'] = Claim_Cust['claim_amount'].astype(float)
Claim['claim_amount'] = Claim['claim_amount'].fillna(Claim['claim_amount'].mean())

Claim['total_policy_claims'] = Claim['total_policy_claims'].fillna(Claim['total_policy_claims'].mean())
# print(Claim)




# 7 -   Calculate the age of customers in years. Based on the age, categorize 
#       the customers according to the below criteria 
#       Children < 18 
#       Youth     18-30 
#       Adult     30-60 
#       Senior   > 60

Customer.loc[
    Customer['DateOfBirth'].dt.year > 2026,
    'DateOfBirth'
] -= pd.DateOffset(years=100)
Customer['Age'] = pd.Timestamp.today().year - Customer['DateOfBirth'].dt.year
Customer['AgeGroup'] = pd.cut(Customer['Age'], bins=[0, 18, 30, 60, float('inf')], labels=['Children', 'Youth', 'Adult', 'Senior'], right=False)
Claim_Cust['Age'] = pd.Timestamp.today().year -Claim_Cust['DateOfBirth'].dt.year
Claim_Cust['AgeGroup'] = pd.cut(Claim_Cust['Age'], bins=[0, 18, 30, 60, float('inf')], labels=['Children', 'Youth', 'Adult', 'Senior'], right=False)
# print(Customer['AgeGroup'])




# 8 -   What is the average amount claimed by the customers from various segments?
# print(Claim_Cust.groupby(['Segment'])['claim_amount'].mean())




# 9 -   What is the total claim amount based on incident cause for all the 
#       claims that have been done at least 20 days prior to 1st of October, 2018.

Claim['claim_date'] = pd.to_datetime(Claim['claim_date'])
filteredDate = pd.to_datetime('10/01/2018') - pd.Timedelta(days=20)
# print(Claim[Claim['claim_date'] <= filteredDate].groupby('incident_cause')['claim_amount'].sum())




# 10 -  How many adults from TX, DE and AK claimed insurance for driver related issues and causes?

# print(Claim_Cust.query('AgeGroup == "Adult" and State in ("TX", "DE", "AK") and incident_cause in ("Driver error", "Other driver error")'))




# 11 -  Draw a pie chart between the aggregated value of claim amount based on gender and segment. 
#       Represent the claim amount as a percentage on the pie chart. 

GenderPie = Claim_Cust.groupby(['gender', 'Segment'])['claim_amount'].sum()
# print(Pie)

# plt.pie(GenderPie, labels=[f'{gender} - {segment}' for gender, segment in GenderPie.index])
# plt.title("Gender and Segment Pie Chart")
# plt.legend()
# plt.show()




# 12 -  Among males and females, which gender had claimed the most for any type of driver related issues? 
#       E.g. This metric can be compared using a bar chart

ClaimGender = Claim_Cust.query('incident_cause in ("Driver error", "Other driver error")').groupby(['gender'])['claim_amount'].sum()
# plt.bar(ClaimGender.index, ClaimGender)
# plt.title("Gender Claim Amount Bar Chart")
# plt.show()




# 13 -  Which age group had the maximum fraudulent policy claims? Visualize it on a bar chart.

# AgeGroupClaims = Claim_Cust.query('fraudulent == "Yes"').groupby(['AgeGroup'])['fraudulent'].count()
# plt.bar(AgeGroupClaims.index, AgeGroupClaims)
# plt.title('Fraudulent Policy Claims')
# plt.show()




# 14 -  Visualize the monthly trend of the total amount that has been claimed by the customers. 
#       Ensure that on the “month” axis, the month is in a chronological order not alphabetical order.

Claim_Cust['claim_month']= pd.to_datetime(Claim_Cust['claim_date']).dt.month_name()
Claim_Cust['claim_month_no']= pd.to_datetime(Claim_Cust['claim_date']).dt.month
# MonthlyTrend = Claim_Cust.groupby(['claim_month_no', 'claim_month'])['claim_amount'].sum().sort_index()
# print(MonthlyTrend.index.get_level_values(1))

# plt.plot(MonthlyTrend.index.get_level_values(1), MonthlyTrend.index.get_level_values(0), marker='o', linewidth=2)
# plt.show()




# 15 -  What is the average claim amount for gender and age categories and suitably represent the above using a facetted bar chart, 
#       one facet that represents fraudulent claims and the other for non-fraudulent claims.

# Facetted = Claim_Cust.groupby(['gender', 'AgeGroup', 'fraudulent'])['claim_amount'].mean().unstack()
# Facetted.plot(kind='bar', figsize=(10, 6), stacked=True)
# plt.show()