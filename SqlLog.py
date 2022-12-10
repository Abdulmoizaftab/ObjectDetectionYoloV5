from unittest import result
import pyodbc
import pandas as pd
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=192.168.1.100;"
            "Database=RTODE;"
            "UID=sa;"
            "PWD=Dev@2022;")
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()
#cursor.execute("insert into ObjectDetection values('2 person')")
# cnxn.commit()
# data = pd.read_sql("insert into ObjectDetection values('2 person')", cnxn)