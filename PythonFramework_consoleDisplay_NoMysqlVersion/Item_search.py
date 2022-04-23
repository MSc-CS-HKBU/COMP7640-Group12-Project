import pymysql

from prettytable import PrettyTable
from prettytable import DEFAULT


# search items
def search_item(db, cursor, item):
    # option = input("Please enter what you want to search >> ")
    sql = "SELECT Item_ID, Item_Name,Price,Item_qty,Classification,Description,Indications FROM items WHERE Item_Name = '%s' OR \
    Classification = '%s' OR Indications='%s'"%(item,item,item)

    dict_result = dict()

    try:
        # execute sql
        cursor.execute(sql)
        # get data
        data = cursor.fetchall()
        if len(data) == 0:
            print("Sorry, we do not have this item now, try another like Nin Jiom?")
            return dict_result
        print("\n-------Searching Result-------")
        table = PrettyTable(['Item_ID','Item_Name','Price','Item remaining','Classification','Description','Indications'])

        for i in data:
            table.add_row([i[0], i[1], i[2], i[3],i[4],i[5],i[6]])

            dict_result[i[0]] = {
                'Item_Name': i[1],
                'Price': i[2],
                'Item remaining': i[3],
                'Classification': i[4],
                'Description': i[5],
                'Indications': i[6]
            }

        table.set_style(DEFAULT)
        print(table)
        return dict_result


    except pymysql.Error as e:
        print(e.args[0], e.args[1])
    return