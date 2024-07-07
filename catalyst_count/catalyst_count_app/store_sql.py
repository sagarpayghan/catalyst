import pandas as pd
from sqlalchemy import create_engine
import os

def toSQL():
    try:
        engine = create_engine(DATABASE_URL)
        path=os.path.join(os.getcwd(),"catalyst_count\media\data.csv")
        df=pd.read_csv(path)
        with engine.begin() as connection:
            df.to_sql(name='mytable', con=connection, if_exists='append',index=False)
            os.remove(path)
            return True
    except Exception as e:
        print("Exception",e)

toSQL()
