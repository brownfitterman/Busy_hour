import pyodbc

cnxn_str = ("Driver={SQL Server};"
            "Server=103.212.120.142;"
            "Database=scouter;"
            "UID=krishna;"
            "PWD=Sa@123,.;")
cnxn = pyodbc.connect(cnxn_str)
print(cnxn)