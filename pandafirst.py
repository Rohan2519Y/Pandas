import pandas as pd
import numpy as np
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

DF = pd.DataFrame({
    'Year':[2000, 2000, 2000, 2001, 2001, 2002, 2003, 2003],
    'Production' : [23, 78, 38, 97, 84, 17, 67, 48]
})
G = DF.groupby('Year')['Production'].sum()
print(G)