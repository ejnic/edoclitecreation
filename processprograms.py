import pandas as pd
import sqlalchemy
import datetime
import private as pr
import myfunctions as mf

engine = sqlalchemy.create_engine(pr.strengine)

df = pd.read_sql_query(pr.sqlprograms, engine)
print(df.shape)
# get just Bloomington programs
dfbl = df[df.institution == 'IUBLA']
print(dfbl.shape)
dfbl['cleanedprogramcd'] = dfbl['acad_prog']
dfbl['cleanedprogramcd'] = dfbl['cleanedprogramcd'].apply(mf.cleanprogramcd)
print(dfbl.head(10))
#dfbl['cleanedprogramcd']=dfbl['cleanedprogramcd'].apply(cleanprogramcd(dfbl[['acad_prog']]))
#dfbl['cleanedprogramcd'] = mf.cleanprogramcd(dfbl[['acad_prog']])
#for index, row in dfbl.iterrows():
    #programcd = ProgramCode(dfbl.iloc[index]['acad_prog']).cleancd
#    print(classprocess.cleanprogramcd(dfbl.iloc[index]['acad_prog']))