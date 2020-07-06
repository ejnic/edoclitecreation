import pandas as pd
import sqlalchemy
import datetime
import private as pr
import myfunctions as mf

engine = sqlalchemy.create_engine(pr.strengine)

df = pd.read_sql_query(pr.sqlprograms, engine)
# get just Bloomington programs
dfbl = df[df.institution == 'IUBLA']

#take the number off the end if it exists
dfbl['cleanedprogramcd'] = dfbl['acad_prog']
dfbl['cleanedprogramcd'] = dfbl['cleanedprogramcd'].apply(mf.cleanprogramcd)
print(dfbl.head(10))
