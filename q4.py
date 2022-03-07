import pandas as pd
from sqlalchemy import create_engine
import logging

engine = create_engine("postgresql+psycopg2://mansigupta:1234@localhost:5432/test")


def read_sheets(data, file):
    try:
        if data == 'Query2':
            df = pd.read_excel(file, 'Query2')
            return df

    except:
        print("Execution unsuccessful. Exception occurred.")
        logging.error("Error")
    finally:
        print("Execution Successful.")
        logging.info("no issues")


with pd.ExcelFile('Excel_file_Q2.xlsx') as xls:
    for sheet_name in xls.sheet_names:
        new_df = read_sheets(sheet_name, xls)

# temp1_df = new_df[['Dept']].groupby('Dept Name')['Total Compensation'].sum()
temp1_df = new_df.groupby(['Dept Name', 'Dept Number']).agg(
    Total_Compensation=pd.NamedAgg(column='Total Compensation', aggfunc="sum")
).reset_index()


# print(temp1_df)
writer = pd.ExcelWriter('/Users/mansigupta/Desktop/PyCharm/pythonProjects/py-sql(Postgre)/Codes/Excel_file_Q4.xlsx')
temp1_df.to_excel(writer, sheet_name='Excel_file_Q4', index=False)
writer.save()