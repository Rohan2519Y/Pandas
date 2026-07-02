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
D = pd.DataFrame({'100':{'1':'A', '2':'B'}, '200':{'1':'C', '2':'D'}, '300':{'1':'E', '2':'F'}})
# print(pd.DataFrame(D))
print(D.loc['1'])