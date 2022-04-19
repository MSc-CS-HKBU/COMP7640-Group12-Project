import pymysql
import Item_search

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
        Item_search.search_item(db, cursor)
    elif option == "`":
        return
    else:
        print("\n[!] You've entered invalid character.")


# cancel entire order
def cancel_order(db, cursor, user_id):
    # still need a little optimize after purchase function finish
    option = input("Are you sure to cancel the entire order?(y/n)")
    if option == "y":
        sql = "DELETE FROM orders WHERE Customer_ID = %s"%user_id
        try:
            # 执行sql语句
            cursor.execute(sql)
            # push to database execute
            db.commit()


        except pymysql.Error as e:
            print(e.args[0], e.args[1])
            db.rollback()
        print("order cancel")
        # come back to first page
        return
    elif option == "n":
        # come back to shopping cart
        return
    else:
        print("\n[!] You've entered invalid character.")
        cancel_order(db, cursor, user_id)

