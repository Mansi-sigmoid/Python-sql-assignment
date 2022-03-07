import psycopg2
import xlsxwriter
import pandas as pd
import logging

def execute_query(query):
    try:
        connection = psycopg2.connect(database="test", user="mansigupta", password="1234", host="localhost", port=5432)
        print("Database Connected....")
        logging.info("Database Connected....")
        cur = connection.cursor()
        # Query 1...
        # Take the self join of emp table

        cur.execute("UPDATE jobhist SET enddate=CURRENT_DATE WHERE enddate IS NULL;")
        data = cur.execute(query)
        rows = cur.fetchall()
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        c5 = []
        c6 = []

        for row in rows:
            temp_list = list(row)
            c1.append(temp_list[0])
            c2.append(temp_list[1])
            c3.append(temp_list[2])
            c4.append(temp_list[3])
            c5.append(temp_list[4])
            c6.append(temp_list[5])
            # print(temp_list)
        # print(c1)
        # print(c2)
        # print(c3)
        df = pd.DataFrame({'Employee Name': c1, 'Employee No': c2, 'Dept Name': c3, 'Dept Number': c4, 'Total Compensation': c5, 'Months Spent': c6})
        writer = pd.ExcelWriter('/Users/mansigupta/Desktop/PyCharm/pythonProjects/py-sql(Postgre)/Codes/Excel_file_Q2.xlsx')
        df.to_excel(writer, sheet_name='Query2', index=False)
        writer.save()
        print("Executed")

    except:
        print("There is an error...")
        logging.error("Error")

    finally:
        print("I have no issues..")
        logging.info("No issues")

        connection.close()

if __name__=="__main__":
    query="SELECT emp.ename, "\
            "jh.empno, dept.dname, jh.deptno, "\
            "ROUND((jh.enddate-jh.startdate)/30*jh.sal,0) "\
            "AS total_compensation, ROUND((jh.enddate-jh.startdate)/30,0) as months_spent FROM "\
            "jobhist as jh INNER JOIN dept ON jh.deptno=dept.deptno INNER JOIN emp ON jh.empno=emp.empno;"
    execute_query(query)
    print("This is successfull.....")