import pymysql

# get all items
def get_all_items(db, cursor):
    sql = "SELECT * FROM items"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # get data
        data = cursor.fetchall()
        print("\n----Items----")
        print("`. Back")
        print("0. Exit")
        for i in range(0, len(data), 1):
            print(data[i])

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        # rollback when wrong happen
        db.rollback()

    option = input("Enter number to select option >> ")
    if option == "0":
        print("See you again!")
        exit()
    elif option == "`":
    #     showLandingPage()
        return
    else:
        print("\n[!] You've entered invalid character.")


# insert new item
def insert_item(db, cursor):
    print("\n----Please enter what you want to add----")
    Item_column=(
        'Item_ID','Item_Name','Price','Shop_ID','Item_qty','Classification','Description','Keyword1','Keyword2')
    # Item_column = (
    # 'Item_ID', 'Item_Name')
    item={}
    for i in Item_column:
        content = input('%s='%i,)
        print(content)
        item.update({'%s'%i: content})
        # item=kwargs
    print(item)
    sql = "INSERT INTO items VALUES('%s','%s',%s,'%s', %s, \
    '%s', '%s', '%s', '%s')"% \
          (item['Item_ID'], item['Item_Name'], item['Price'], item['Shop_ID'], item['Item_qty'], \
          item['Classification'], item['Description'], item['Keyword1'], item['Keyword2'])
    print("sql=",sql)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # push to database execute
        db.commit()
        print('insert successfully')

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        # rollback when wrong happen
        db.rollback()

    print("`. Back")
    print("0. Exit")
    option = input("Enter number to select option >> ")
    if option == "0":
        print("See you again!")
        exit()
    elif option == "`":
        return
    else:
        print("\n[!] You've entered invalid character.")

# def connetSql(databaseName):
#     sqlConnect = pymysql.connect(  # connect mysql server
#         user="root",
#         password="7640pwd",
#         host="rubyubuntu.ddns.net",  # IPaddress
#         port=3306,
#         database=databaseName,
#         charset="utf8"
#     )
#     conn = sqlConnect.cursor()  # Create an operational cursor
#     return conn, sqlConnect
#
# database_name = '7640_proj'
# conn, sqlConnect = connetSql(database_name)
# db = pymysql.connect(host='rubyubuntu.ddns.net',
#                      port= 3306,
#                      user='root',
#                      password='7640pwd',
#                      database='7640_proj')
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # list all items
# # get_all_items(cursor)
#
# # insert new item
# new_item={'Item_ID':'P992','Item_Name':'psyduck','Price':20,'Shop_ID':'S999','Item_qty':100, 'Classification':'Food',\
#           'Description':'orginal:china', 'Keyword1':'duck', 'Keyword2':'yellow'}
# insert_item(db, cursor, **new_item)
# # 使用 fetchone() 方法获取单条数据.
# # data = cursor.fetchone()
# #
# # print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()