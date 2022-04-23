import pymysql, random, globals

def write_cart(item_ID, target_product):
    cartFileReadAndUpdate = open(
        globals.path_cartFile, "r+")
    cartFileLines = cartFileReadAndUpdate.readlines()
    cartFileLines.insert(
        0, f'{item_ID}:{target_product["Item_Name"]}:${target_product["Price"]}\n')
    cartFileReadAndUpdate.seek(0)
    cartFileReadAndUpdate.writelines(cartFileLines)
    cartFileReadAndUpdate.close()
 
    

def load_cart(path_cartFile):
    cart_items = [x.strip() for x in open(globals.path_cartFile)] # read all lines in txt into list, e.g. P005:Kobayashi antipyretic patch:$20

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
    return dict_cart_items 


# purchase items in cart
def purchase_item_in_cart(db, cursor, customer_id):
    order_id = f"A{str(random.getrandbits(20))}" # generate A<number>, <number> is 20-bit integer (i.e. max 2^20 - 1)

    dict_cart_items = load_cart(globals.path_cartFile)

    # insert to db table "orders"
    for item_id in dict_cart_items:
        sql = f"INSERT INTO orders (Order_ID, Customer_ID, Item_ID, Item_Name, Item_qty, Price) VALUES ('{order_id}', {customer_id}, '{item_id}', '{dict_cart_items[item_id]['name']}', {dict_cart_items[item_id]['count']}, {dict_cart_items[item_id]['total_price']})"
        # print(sql)
        try:
            # execute SQL
            cursor.execute(sql)
            # push to database execute
            db.commit()
        except pymysql.Error as e:
            print(e.args[0], e.args[1])

    # clear cart
    open(globals.path_cartFile, 'w').close()
