import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# S = pd.Series([1, 2, 3, 4, 5])
# S = pd.Series(['A', 'B', 'C', 'D'], index = [100, 200, 300, 400])
# A = np.array(['Ha', 'Pe', 'Th', 'Vi'])
# A = {'100':'Tanmay', '200':'Bhagel', '300':'Saksham', '400':'Harsh'}
# S = pd.Series(A)
# S.index = (1, 2, 3, 4)
# S.name = 'People'
# print(S)
# print(S.values)
# print(S.index)
# print(S.size)
# print(S.empty)
# print(S.head(2))
# print(S.tail(2))
# print(S.count())
# print(S[['100', '200']])

# S1 = pd.Series([1, 2, 3, 4])
# S2 = pd.Series([5, 6, 7, 8])
# S1 = pd.Series([1, 2, 3, 4], index = ['A', 'B', 'C', 'D'])
# S2 = pd.Series([5, 6, 7, 8], index = ['A', 'C', 'F', 'G'])
# print(S1+S2)
# print(S1.add(S2, fill_value=0))
# print(S1.sub(S2, fill_value=0))

# L1 = [1, 2, 3, 4, 5]
# L2 = [10, 2, 3, 4, 5]
# L3 = [100, 2, 3, 4, 5]
# D = pd.DataFrame([L1, L2, L3], columns=['A', 'B', 'C', 'D', 'E'], index=[2000, 3000, 4000])
# print(D)

# D = [{'1':'A', '2':'B'}, {'1':'C', '2':'D'}, {'1':'E', '2':'F'}]
# D = pd.DataFrame({'100':{'1':'A', '2':'B'}, '200':{'1':'C', '2':'D'}, '300':{'1':'E', '2':'F'}})
# print(pd.DataFrame(D))
dictForest = {'State': ['Assam', 'Delhi', 'Kerala'], 'GArea': [78438, 1483, 38852] ,'VDF' : [2797, 6.72,1663]}
# D = pd.DataFrame(dictForest)
# D = pd.DataFrame(dictForest, columns = ['State','VDF', 'GArea'])

ResultSheet={'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96],index=['Maths','Science','Hindi']), 
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, 71, 67],index=['Maths','Science','Hindi']), 
'Mallika': pd.Series([94, 95, 99],index=['Maths','Science','Hindi'])}

ResultDF = pd.DataFrame(ResultSheet)
# ResultDF.loc['English'] = [85, 86, 83, 80, 90]
# ResultDF.loc['Maths'] = 0
# print(ResultDF)
# print(ResultDF.loc['Maths'] > 90)
# print(ResultDF.loc['Maths':'Science', 'Arnab'])
# print(ResultDF.T) # Transpose
# print(ResultDF.head(2))
# print(ResultDF.tail(2))
# print(ResultDF.info())
# print(ResultDF.describe())
# print(ResultDF.iloc[0:3, [0, 2]])
# print(ResultDF.axes)
# print(ResultDF.rank())
# print(ResultDF.rank(ascending=False))
# print(ResultDF.sort_values(by=['Arnab']))
# print(ResultDF.sort_values(by=['Maths'], ascending=False, axis=1))
# print(ResultDF.sort_index())
# for V in ResultDF.items():
#     print(V)
# for V in ResultDF.iterrows():
#     print(V)
# print(ResultDF.count())
# print(ResultDF.cumsum(axis=1))
# print(ResultDF.cummax())
# print(ResultDF.cummin())
# print(ResultDF.diff())
# print(ResultDF.div(10))
# ResultDF.loc['Total'] = ResultDF.sum()
# print(ResultDF)
# print(ResultDF.where(ResultDF > 50, other = 0))



dFrame10Mu1tip1es = pd.DataFrame([10, 20, 30 , 40, 50])
# print(dFrame10Mu1tip1es.loc[2])
# print(ResultDF.loc[:, 'Arnab'])
# print(ResultDF.loc[['Science', 'Maths']])


ResultSheet1=pd.DataFrame({'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96],index=['Maths','Science','Hindi']), 
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, 71, 67],index=['Maths','Science','Hindi']), 
'Mallika': pd.Series([94, 95, 99],index=['Maths','Science','Hindi'])})

ResultSheet2=pd.DataFrame({'Arnab': pd.Series([90, 91, 97], index=['Maths','Science','Hindi']),
'Ramit': pd.Series([92, 81, 96],index=['Maths','Science','Hindi']), 
'Samridhi': pd.Series([89, 91, 88], index=['Maths','Science','Hindi']),
'Riya': pd.Series([81, 71, 67],index=['Maths','Science','Hindi']), 
'Mallika': pd.Series([94, 95, 99],index=['Maths','Science','Hindi'])})

# L = pd.concat([ResultSheet1, ResultSheet2])
# print(L)
# print(ResultSheet1.dot(ResultSheet2.T))
# print(ResultSheet1.mul(ResultSheet2))

# People = {
#     'A':{'first':'Peter', 'last':'Thomas', 'email':'peter@gmail.com'},
#     'B':{'first':'Tanmay', 'last':'Agarwal', 'email':'tanman@gmail.com'},
#     'C':{'first':'Sakhsham', 'last':'Agarwal', 'email':'sak@gmail.com'}
# }

People = [
    {'first':'Peter', 'last':'Thomas', 'email':'peter@gmail.com'},
    {'first':'Tanmay', 'last':'Agarwal', 'email':'tanman@gmail.com'},
    {'first':'Sakhsham', 'last':'Agarwal', 'email':'sak@gmail.com'}
]
DF1 = pd.DataFrame(People)
# print(DF1, '\n\n')
# print(DF1.loc[(DF1['last'] == 'Agarwal') & (DF1['email'] == 'tanman@gmail.com')])
# print(DF1.loc[~(DF1['last'] == 'Agarwal') & (DF1['email'] == 'tanman@gmail.com')]) # not
# print(DF1.loc[DF1['first'].str.contains('er')])
# print(DF1.loc[DF1['last'].str.contains('ar')])
# print(DF1.filter(items=[0, 1], axis = 0))
# print(DF1.query('first == "Peter"'))

# DF = pd.DataFrame({
#     'Year':[2000, 2000, 2000, 2001, 2001, 2002, 2003, 2003],
#     'Production' : [23, 78, 38, 97, 84, 17, 67, 48]
# })
# G = DF.groupby('Year')['Production'].sum()
# print(G)



# raw_data_1 = {'subject_id': ['1', '2', '3', '4', '5'],'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
# raw_data_2 = {'subject_id': ['4', '5', '6', '7', '8'],'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
# raw_data_3 = {'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

# Data1=pd.DataFrame(raw_data_1)
# Data2=pd.DataFrame(raw_data_2)
# Data3=pd.DataFrame(raw_data_3)


# print(pd.merge(Data1, Data2))
# print(pd.merge(Data1, Data2, left_on=['subject_id'], right_on=['subject_id']))
# print(pd.merge(Data1, Data2, left_index=True, right_index=True))
# print(pd.merge(Data1, Data2, how='left'))
# print(Data1.join(Data3, lsuffix='A', rsuffix='B'))


Data1={'productid':[100,200,300,400,500], 'productname':['Amul Ghee','Pepsi','Real Juice','Dawat Rice','Dove Shampoo'], 'rate':[700,20,120,700,300], 'offer':[600,18,110,300,100], }
Data2={'productid':[200,500,200,100,400,200,0],'qtysale':[3,7,2,1,10,8,0]}
Data3={'productid':[600,700], 'productname':['Amul Butter','Parle G'], 'rate':[700,20], 'offer':[300,18], }


product1 = pd.DataFrame(Data1)
product2 = pd.DataFrame(Data3)
sales = pd.DataFrame(Data2)

# DF3 = pd.merge(product1[["productid", "productname", "rate"]], sales, indicator=True)
# DF3['amount'] = DF3['qtysale'] * DF3['rate']
# print(DF3)

# DF4 = pd.concat([product1, product2], ignore_index=True)
# print(DF4)

df = pd.DataFrame({
    'gender': ['male', 'male', 'female', 'female', 'male', 'female', 'male', 'female'],
    'education_level': ['high school', 'college', 'college', 'graduate', 'high school', 'graduate', 'college', 'graduate'],
    'score': [75, 82, 88, 95, 69, 92, 78, 85]
})
# print(df)

ct = pd.crosstab(df['gender'], df['education_level'], margins=True)
# ct = pd.crosstab(df['gender'], df['education_level'], values=df['score'], aggfunc='sum')
# print(ct)


DF = pd.DataFrame({
    'Name' : ['Rahul', 'Pankaj', 'Mohan', 'Peter'], 'DOB':['11-07-2000', '11-02-2004', '17-11-2006', '10-04-2005']
})
DF['DOB'] = pd.to_datetime(DF['DOB'], dayfirst=True)
DF['Month'] = pd.to_datetime(DF['DOB'], dayfirst=True).dt.month_name()
DF['Week'] = pd.to_datetime(DF['DOB'], dayfirst=True).dt.strftime("%A")
print(DF)