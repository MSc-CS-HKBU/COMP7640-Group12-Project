import pymysql
from prettytable import DEFAULT, PrettyTable

import Item_search

# get items of an order
def get_items_of_order(db, cursor, user_id, order_id):
    sql = "SELECT Item_ID, Item_Name, Item_qty, Price FROM orders WHERE Customer_ID='%s' AND Order_ID='%s'" % (user_id, order_id)
    data = []
    try:
        # execute sql
        cursor.execute(sql)
        # get data
        data = cursor.fetchall()

        if len(data) == 0:
            return data


        table = PrettyTable(['Item_ID', 'Item_Name', 'Item_qty', 'Price'])

        for i in data:
            table.add_row([i[0], i[1], i[2], i[3]])

        table.set_style(DEFAULT)
        print(table)



    except pymysql.Error as e:
        print(e.args[0], e.args[1])

    return data


# get order list
def get_orders(db, cursor, user_id):
    sql = "SELECT DISTINCT Order_ID FROM orders WHERE Customer_ID='%s'" % (user_id)
    try:
        # execute sql
        cursor.execute(sql)
        # get data
        data = cursor.fetchall()

        if len(data) == 0:
            return


        table = PrettyTable(['Order_ID'])

        for i in data:
            table.add_row([i[0]])

        table.set_style(DEFAULT)
        print(table)



    except pymysql.Error as e:
        print(e.args[0], e.args[1])

    return


# cancel single item in an order
def cancel_order_single_item(db, cursor, user_id, order_id, item_id):
    sql = "DELETE FROM orders WHERE Customer_ID = %s AND Order_ID = '%s' AND Item_ID = '%s'" % (user_id, order_id, item_id)
    try:
        # execute sql command
        cursor.execute(sql)
        # push to database execute
        db.commit()

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    print("\nOrder's item cancelled if exists")
    # come back to first page
    return

# cancel single order
def cancel_user_single_order(db, cursor, user_id, order_id):
    sql = "DELETE FROM orders WHERE Customer_ID = %s AND Order_ID = '%s'" % (user_id, order_id)
    try:
        # execute sql command
        cursor.execute(sql)
        # push to database execute
        db.commit()

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    print("\nOrder cancelled if exists")
    # come back to first page
    return

# cancel all orders of a user
def cancel_user_all_orders(db, cursor, user_id):
    sql = "DELETE FROM orders WHERE Customer_ID = '%s'" % user_id
    try:
        # execute sql command
        cursor.execute(sql)
        # push to database execute
        db.commit()

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    print("\nAll current user order cancelled, if exists")
    # come back to first page
    return
