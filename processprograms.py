import pandas as pd
import sqlalchemy
import datetime
import private as pr

engine = sqlalchemy.create_engine(pr.strengine)

df = pd.read_sql_query(pr.sqlprograms, engine)

print(df.head(5))