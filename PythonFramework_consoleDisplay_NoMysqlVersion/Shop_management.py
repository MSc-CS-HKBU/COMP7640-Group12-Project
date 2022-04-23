import pymysql
import random


def showShops(db, cursor):
    sql = 'SELECT Shop_Name, Shop_Address, Rating FROM shop'
    cursor.execute(sql)
    results = cursor.fetchall()
    # print("\n----Items----")
    # print("`. Back")
    # print("0. Exit")    
    for row in results:
        sname = row[0]
        saddr = row[1]
        rating = row[2]

        print(f'|<>| {sname} ({rating}/10) - {saddr}')
    # option = input("Enter number to select option >> ")
    # if option == "0":
    #     print("See you again!")
    #     exit()
    # elif option == "`":
    #     # showLandingPage()
    #     return
    # else:
    #     print("\n[!] You've entered invalid character.")   

def insert_shop(name, addr, rating, db, cursor):
    # print("\n----Please enter shop you want to add----")
    
    key = ''+str(random.getrandbits(20))

    sql = "INSERT INTO shop VALUES('%s','%s','%s',%s)" % \
          (key, name, addr, rating)
    print("sql=",sql)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # push to database execute
        db.commit()
        print('insert successfully')

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        # rollback when wrong happen
        db.rollback()

    # print("`. Back")
    # print("0. Exit")
    # option = input("Enter number to select option >> ")
    # if option == "0":
    #     print("See you again!")
    #     exit()
    # elif option == "`":
    #     return
    # else:
    #     print("\n[!] You've entered invalid character.")


