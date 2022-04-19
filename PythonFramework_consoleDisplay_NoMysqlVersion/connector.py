import pymysql

def connetSql(databaseName):
    sqlConnect = pymysql.connect(  # connect mysql server
        user="root",
        password="7640pwd",
        host="rubyubuntu.ddns.net",  # IPaddress
        port=3306,
        database=databaseName,
        charset="utf8"
    )
    conn = sqlConnect.cursor()  # Create an operational cursor
    return conn, sqlConnect

database_name = '7640_proj2'
conn, sqlConnect = connetSql(database_name)
