import pymysql


# search items
def search_item(db, cursor):
    option = input("Please enter what you want to search >> ")
    sql = "SELECT Item_Name,Price,Item_qty,Classification,Description,Indications FROM items WHERE Item_Name = '%s' OR \
    Classification = '%s' OR Indications='%s'"%(option,option,option)
    try:
        # execute sql
        cursor.execute(sql)
        # get data
        data = cursor.fetchall()
        if len(data) == 0:
            print("Sorry, we do not have this item now, try another like Nin Jiom?")
            return
        for i in data:
            print(i)

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
    return