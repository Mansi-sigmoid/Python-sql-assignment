import pandas as pd
from sqlalchemy import create_engine
import logging

engine = create_engine("postgresql+psycopg2://mansigupta:1234@localhost:5432/test")


def read_sheets(data, file):
    try:
        if (data == 'Query2'):
            df = pd.read_excel(file, 'Query2')
            df.to_sql(name='emp_compensation', con=engine, if_exists='append', index=False)

    except:
        print("Execution is unsuccessful. Exception occurred.")
        logging.error("There is an error...")
    finally:
        print("Execution Successful.....")
        logging.info("I have no issues..")


with pd.ExcelFile('Excel_file_Q2.xlsx') as xls:
    for sheet_name in xls.sheet_names:
        read_sheets(sheet_name, xls)