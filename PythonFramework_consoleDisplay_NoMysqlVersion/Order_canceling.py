import pymysql

import Item_search


# cancel order item
# def cancel_order_single_item(db, cursor, user_id):
#     # in progress
#     option = input("Please enter what you want to search >> ")
#     sql = "SELECT Item_Name,Price,Item_qty,Description,Keyword1,Keyword2 FROM items WHERE Item_Name = '%s' OR \
#     Keyword1 = '%s' OR Keyword2='%s'" % (option, option, option)
#     try:
#         # execute sql command
#         cursor.execute(sql)
#         # get data
#         data = cursor.fetchall()
#         for i in data:
#             print(i)

#     except pymysql.Error as e:
#         print(e.args[0], e.args[1])

#     print("1. Search again")
#     print("`. Back")
#     print("0. Exit")
#     option = input("Enter number to select option >> ")
#     if option == "0":
#         print("See you again!")
#         exit()
#     elif option == "1":
#         Item_search.search_item(db, cursor)
#     elif option == "`":
#         return
#     else:
#         print("\n[!] You've entered invalid character.")


# cancel single item in an order
def cancel_order_single_item(db, cursor, user_id, order_id, item_id):
    sql = "DELETE FROM orders WHERE Customer_ID = %s AND Order_ID = %s AND Item_ID = %s" % (user_id, order_id, item_id)
    try:
        # execute sql command
        cursor.execute(sql)
        # push to database execute
        db.commit()

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    print("Order cancel, get something!")
    # come back to first page
    return

# cancel single order
def cancel_user_single_order(db, cursor, user_id, order_id):
    sql = "DELETE FROM orders WHERE Customer_ID = %s AND Order_ID = %s" % (user_id, order_id)
    try:
        # execute sql command
        cursor.execute(sql)
        # push to database execute
        db.commit()

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    print("Order cancel, get something!")
    # come back to first page
    return

# cancel all orders of a user
def cancel_user_all_orders(db, cursor, user_id):
    sql = "DELETE FROM orders WHERE Customer_ID = %s" % user_id
    try:
        # execute sql command
        cursor.execute(sql)
        # push to database execute
        db.commit()

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    print("Order cancel, get something!")
    # come back to first page
    return
