import pymysql, random, globals

def load_cart(path_cartFile):
    # in progress
    cart_items = [x.strip() for x in open(globals.path_cartFile)] # read all lines in txt into list, e.g. P005:Kobayashi antipyretic patch:$20

    order_id = f"A{str(random.getrandbits(20))}" # generate A<number>, <number> is 20-bit integer (i.e. max 2^20 - 1)
    customer_id = 1 # hard coded, should change to dynamic with db later

    dict_cart_items = dict()
    for item in cart_items:
        splitted_item = item.split(":")
        item_id = splitted_item[0]
        item_name = splitted_item[1]
        item_price = float(splitted_item[2].replace('$',''))
        if item_id in dict_cart_items:
            dict_cart_items[item_id]["count"] += 1
            dict_cart_items[item_id]["total_price"] += item_price
        else:
            dict_cart_items[item_id] = {
                "name": item_name,
                "count": 1,
                "total_price": item_price
            }    



# purchase items in cart
def purchase_item_in_cart(db, cursor):
    # in progress
    # print("y. Yes")
    # print("n. No")
    # print("`. Back")
    # print("0. Exit")
    # option = input("Confirm to place order [y/n]>> ")
    # if option == "0":
    #     print("See you again!")
    #     exit()    
    # if option == "y":
        # INSERT INTO orders (Order_ID, Customer_ID, Shop_ID, Item_ID, Item_Name, Item_qty, Price) VALUES (%s, %s, %s, %s, %s, %s, %s)
        # sql = "SELECT Item_Name,Price,Item_qty,Description,Keyword1,Keyword2 FROM items WHERE Item_Name = '%s' OR \
        # Keyword1 = '%s' OR Keyword2='%s'"%(option,option,option)

        # './PythonFramework_consoleDisplay_NoMysqlVersion/cart.txt'

        cart_items = [x.strip() for x in open(globals.path_cartFile)] # read all lines in txt into list, e.g. P005:Kobayashi antipyretic patch:$20

        order_id = f"A{str(random.getrandbits(20))}" # generate A<number>, <number> is 20-bit integer (i.e. max 2^20 - 1)
        customer_id = 1 # hard coded, should change to dynamic with db later

        dict_cart_items = dict()
        for item in cart_items:
            splitted_item = item.split(":")
            item_id = splitted_item[0]
            item_name = splitted_item[1]
            item_price = float(splitted_item[2].replace('$',''))
            if item_id in dict_cart_items:
                dict_cart_items[item_id]["count"] += 1
                dict_cart_items[item_id]["total_price"] += item_price
            else:
                dict_cart_items[item_id] = {
                    "name": item_name,
                    "count": 1,
                    "total_price": item_price
                }

        # print(order_id)
        # print(dict_cart_items)



        # insert to db table "orders"
        for item_id in dict_cart_items:
            sql = f"INSERT INTO orders (Order_ID, Customer_ID, Item_ID, Item_Name, Item_qty, Price) VALUES ('{order_id}', {customer_id}, '{item_id}', '{dict_cart_items[item_id]['name']}', {dict_cart_items[item_id]['count']}, {dict_cart_items[item_id]['total_price']})"
            # print(sql)
            try:
                # 执行sql语句
                cursor.execute(sql)
                # push to database execute
                db.commit()
            except pymysql.Error as e:
                print(e.args[0], e.args[1])

        # clear cart
        open('./PythonFramework_consoleDisplay_NoMysqlVersion/cart.txt', 'w').close()


    # elif option == "n":
    #     showLandingPage()
    # elif option == "`":
    #     showLandingPage()
    # else:
    #     print("\n[!] You've entered invalid character.")