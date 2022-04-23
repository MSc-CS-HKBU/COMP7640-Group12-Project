import pymysql
from prettytable import DEFAULT, PrettyTable

def showAddProductPanel(db, cursor, shop_name):
    # print("\n----Products----")

    # print("[1...] Enter product number to add it to the cart")
    # print("`. Back")
    # print("0. Exit")
    # print("\nPlease enter item ID to add it to the cart")

    # print("\n")
    # get_items_in_a_shop(db, cursor, shop_name)

    # while True:
    #     for i in range(len(products)):
    #         print(f'|{i + 1}| {products[i]["name"]} -> {products[i]["price"]}')

    #     option = input("Your choice >> ")
    #     if option == "`":
    #         showProducts()
    #         return
    #     if option == "0":
    #         shutdown()
    #     if int(option) > 0 and int(option) <= len(products):
    #         cartFileReadAndUpdate = open(
    #             path_cartFile, "r+")
    #         cartFileLines = cartFileReadAndUpdate.readlines()
    #         target_product = products[int(option) - 1]
    #         cartFileLines.insert(
    #             0, f'{target_product["id"]}:{target_product["name"]}:{target_product["price"]}\n')
    #         cartFileReadAndUpdate.seek(0)
    #         cartFileReadAndUpdate.writelines(cartFileLines)
    #         cartFileReadAndUpdate.close()

    #         print("\n----------------------------------------")
    #         print("SUCCESS")
    #         print("Product added to the cart")
    #         print("----------------------------------------\n")
    #         showLandingPage()
    #         return
    #     else:
    #         print("\n[!] You've entered wrong character")
    pass

# get all items in a shop
def get_items_in_a_shop(db, cursor, shop_name):
    print("\n")
    sql = "SELECT Item_ID, Item_Name,Price,Item_qty,Classification,Description,Indications FROM items i, shop s where " \
          "i.Shop_ID = s.Shop_ID and s.Shop_Name = '%s'"%(shop_name)

    # sql = "SELECT * FROM items i, shop s where i.Shop_ID = s.Shop_ID and s.Shop_Name = '%s'"%(shop_name)
    # sql = "SELECT * FROM items where Shop_ID =1"
    
    list_result = []

    try:
        # execute sql
        cursor.execute(sql)
        # get data
        data = cursor.fetchall()

        if data is None:
            print("No items found")
            return list_result
        table = PrettyTable(['Item_ID', 'Item_Name', 'Price', 'Item remaining', 'Classification', 'Description', 'Indications'])

        for i in data:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
            list_result.append({
                'Item_ID': i[0],
                'Item_Name': i[1],
                'Price': i[2],
                'Item remaining': i[3],
                'Classification': i[4],
                'Description': i[5],
                'Indications': i[6]                
            })
        table.set_style(DEFAULT)
        print(table)

        # print("\n----Items----")
        # for i in range(0, len(data), 1):
        #     print(data[i])

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        # rollback when wrong happen
        db.rollback()
    return list_result


# insert new item
def insert_item(db, cursor):
    print("\n----Please enter what you want to add----")
    Item_column=(
        'Item_ID','Item_Name','Price','Shop_ID','Item_qty','Classification','Description','Indications')
    item={}
    for i in Item_column:
        if i == 'Item_ID':
            print("please begin form 'p',such as p01")
        content = input('%s='%i,)
        item.update({'%s'%i: content})
    print(item)
    sql = "INSERT INTO items VALUES('%s','%s',%s,'%s', %s, \
    '%s', '%s', '%s')"% \
          (item['Item_ID'], item['Item_Name'], item['Price'], item['Shop_ID'], item['Item_qty'], \
          item['Classification'], item['Description'], item['Indications'])
    print("sql=",sql)

    try:
        # execute sql
        cursor.execute(sql)
        # push to database execute
        db.commit()
        print('insert successfully')

    except pymysql.Error as e:
        if e.args[0] == 1452:
            print("Insert new item failed, could not find the shop for that Shop_id ")
        else:
            print(e.args[0], e.args[1])
        # rollback when wrong happen
        db.rollback()
    return
