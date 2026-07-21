import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

DF = pd.read_csv('F:\Pandas\world_population.csv')
# print(DF)
# engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/world_population')
# DF.to_sql('wp', con=engine, if_exists='replace', index=True)
# print("Table Created")


# conn = engine.connect()
# Q = text('select * from wp')
# DF1 = pd.read_sql_query(Q, conn)
# print(DF1)