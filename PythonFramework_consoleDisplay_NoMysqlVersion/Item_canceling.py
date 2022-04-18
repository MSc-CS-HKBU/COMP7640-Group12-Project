import pymysql


# cancel item
def cancel_item(db, cursor):
    # in progress
    option = input("Please enter what you want to search >> ")
    sql = "SELECT Item_Name,Price,Item_qty,Description,Keyword1,Keyword2 FROM items WHERE Item_Name = '%s' OR \
    Keyword1 = '%s' OR Keyword2='%s'" % (option, option, option)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # get data
        data = cursor.fetchall()
        for i in data:
            print(i)

    except pymysql.Error as e:
        print(e.args[0], e.args[1])

    print("1. Search again")
    print("`. Back")
    print("0. Exit")
    option = input("Enter number to select option >> ")
    if option == "0":
        print("See you again!")
        exit()
    elif option == "1":
        search_item(db, cursor)
    elif option == "`":
        return
    else:
        print("\n[!] You've entered invalid character.")


# cancel order
def cancel_order(db, cursor):
    # in progress
    option = input("Please enter what you want to search >> ")
    sql = "SELECT Item_Name,Price,Item_qty,Description,Keyword1,Keyword2 FROM items WHERE Item_Name = '%s' OR \
    Keyword1 = '%s' OR Keyword2='%s'" % (option, option, option)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # get data
        data = cursor.fetchall()
        for i in data:
            print(i)

    except pymysql.Error as e:
        print(e.args[0], e.args[1])

    print("1. Search again")
    print("`. Back")
    print("0. Exit")
    option = input("Enter number to select option >> ")
    if option == "0":
        print("See you again!")
        exit()
    elif option == "1":
        search_item(db, cursor)
    elif option == "`":
        return
    else:
        print("\n[!] You've entered invalid character.")
