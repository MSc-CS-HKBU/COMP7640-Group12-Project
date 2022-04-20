import pymysql


def regiter(db, cursor):
    Name = input("Please enter your Name >> ")
    Password = input("Please enter your Password (at less 6 chars or number) >> ")
    Phone = input("Please enter your Phone number >> ")
    Email = input("Please enter your Email >> ")
    Address = input("Please enter your Address >> ")

    sql = "SELECT * FROM customer WHERE Name = '%s'" % (Name)

    try:
        # execute sql
        cursor.execute(sql)
        # get data
        data = cursor.fetchone()
        if data is not None:
            print('User existed')
            return

    except pymysql.Error as e:
        print(e.args[0], e.args[1])

    if len(Password) < 6:
        print('Password to short!')
        return
    elif "@" not in Email:
        print('invalid Email address!')
        return


    sql = "INSERT INTO customer(Name, Password, Phone, Email, Address) VALUES('%s','%s','%s','%s','%s')" % \
          (Name, Password, Phone, Email, Address)
    try:
        # execute sql
        cursor.execute(sql)
        # push to database execute
        db.commit()
        print('insert successfully')

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        # rollback when wrong happen
        db.rollback()
    return

def log_in(db, cursor):
    Name = input("Please enter your Name >> ")
    Password = input("Please enter your Password >> ")

    sql = "SELECT * FROM customer WHERE Name = '%s' AND Password = '%s'" % (Name, Password)
    try:
        # execute sql
        cursor.execute(sql)
        # get data
        data = cursor.fetchone()
        if data is None:
            print('login failed')
            return 0, ''
        else:
            print('login successful')

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        return
    return data[0], data[1]


def log_out(username):
    print("Account %s have logged out"%username)


def close_account(db, cursor):
    Name = input("Please enter the Name >> ")
    Password = input("Please enter the Password >> ")

    sql = "DELETE FROM customer WHERE Name = '%s' AND Password = '%s'" % (Name, Password)
    try:
        # execute sql
        cursor.execute(sql)
        # push to database execute
        db.commit()
        print('delete account successfully')

    except pymysql.Error as e:
        print(e.args[0], e.args[1])
    return