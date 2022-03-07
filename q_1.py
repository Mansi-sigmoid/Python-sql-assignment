import psycopg2
import xlsxwriter
import pandas as pd
import logging

def execute_query(query):
    try:
        connection =psycopg2.connect(database="test",user="mansigupta",password="1234",host="localhost",port=5432)
        logging.info("Database Connected....")
        print("Connected")
        cur=connection.cursor()
        # Query 1...
        # Take the self join of emp table
        data=cur.execute(query)
        rows = cur.fetchall()
        c1=[]
        c2=[]
        c3=[]

        for row in rows:
            temp_list=list(row)
            c1.append(temp_list[0])
            c2.append(temp_list[1])
            c3.append(temp_list[2])
            # print(temp_list)
        # print(c1)
        # print(c2)
        # print(c3)
        df =pd.DataFrame({'Number':c1,'Name':c2,'Manager':c3})
        writer = pd.ExcelWriter('/Users/mansigupta/Desktop/PyCharm/pythonProjects/py-sql(Postgre)/Codes/Excel_file_Q1.xlsx')
        df.to_excel(writer,sheet_name='Query1',index=False)
        writer.save()

    except:
        logging.error("There is an error...")

    finally:
        logging.info("I have no issues..")
        connection.close()


if __name__=="__main__":
    query="SELECT t1.empno as EmployeeNumber, t1.ename as EmployeeName, t2.ename as Manager FROM emp t1, emp t2 WHERE t1.mgr=t2.empno;"
    execute_query(query)