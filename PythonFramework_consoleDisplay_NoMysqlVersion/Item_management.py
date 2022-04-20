import pymysql


# get all items in a shop
def get_items_in_a_shop(db, cursor):
    shop_name = input("please input the shop name which you want to search: ")
    sql = "SELECT * FROM items i, shop s where i.Shop_ID = s.Shop_ID and s.Shop_Name = '%s'"%(shop_name)
    # sql = "SELECT * FROM items where Shop_ID =1"
    try:
        # execute sql
        cursor.execute(sql)
        # get data
        data = cursor.fetchall()
        print("\n----Items----")
        for i in range(0, len(data), 1):
            print(data[i])

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        # rollback when wrong happen
        db.rollback()
    return


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
