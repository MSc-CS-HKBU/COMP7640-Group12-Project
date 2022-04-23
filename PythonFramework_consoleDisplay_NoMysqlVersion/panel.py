from numpy import isin

import customer_operation
import globals
import Item_management
import Item_purchase
import Item_search
import Order_canceling
import Shop_management
from connector import connetSql

cursor, sqlConnect = connetSql('7640_proj')
# Initialize user_name and user_id for tourists
user_name = ''
user_id = 0
# Define the path for shopping cart
# path_cartFile = r"./cart.txt" # r"./PythonFramework_consoleDisplay_NoMysqlVersion/cart.txt"

# ---</MAINPAGE>---
def showLandingPage(user_name):
    while True:
        # CART
        cartFileReadAndUpdate = open(
            globals.path_cartFile, "r+")

        productsInCartQuantity = len(cartFileReadAndUpdate.readlines())

        # Landing Page
        print("\n|================|                 |================|\n|================| Online-Shopping |================|\n|================|                 |================|")
        if user_name != '':
            print("\nWelcome %s!"%user_name)
        else:
            print("Welcome!")
        print("Select option:")            
        print("1. Registration")
        print("2. Login")
        print("3. Show All The Shops")
        print("4. Show Items By Shops")
        print("5. Search Items")

        if productsInCartQuantity == 0:
            print("6. Cart")
        else:
            print(f"6. Cart [{productsInCartQuantity}]")

        print("7. Order")
        print("8. Cancle order")
        print("9. Logout")
        print("m. Management(Shop/Item)")
        print("*. Delete Account")
        print("0. Exit")
        option = input("Your choice >> ")
        if option == "1":
            RegistrationPanel()
        elif option == "2":
            loginPanel()
        elif option == "3":
            showShopPanel(user_name)
        elif option == "4":
            showItempanel(user_name)
        elif option == "5":
            searchItemsPanel(user_name)
        # cart place in here 6
        elif option == "7":
            purchaseOrderCartPanel(user_name)
        elif option == "8":
            cancelOrderPanel(user_name)
        elif option == "9":
            logoutPanel(user_name)
        elif option == "m":
            managementPanel(user_name)
        elif option == "*":
            deleteAccountPanel(user_name)
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.")
            continue

        break        
# ---</MAINPAGE>---

# ---</Exit>---
def closeShop(user_name):
    print("\n----------------------------------------")
    print("\nSee you again %s!"%user_name)
    print("----------------------------------------\n")
    exit()
# ---</Exit>---

# ---</Registration>---
def RegistrationPanel():
    print("\n-------Registration-------")
    print("1. Register")
    print("`. back")
    print("0. Exit")
    option = input("Enter number to select option >> ")
    while True:
        if option == "1":
            print("\n----Please follow the registration rule----")
            customer_operation.register(sqlConnect, cursor)
            showLandingPage(user_name)
            break
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.")
            continue
# ---</Registration>---

# ---</Login>---
def loginPanel():
    while True:
        print("\n-------Login-------")
        print("1. Log in with Name amd Password")
        print("`. back")
        print("0. Exit")
        option = input("Enter number to select option >> ")
        if option == "1":
            print("\n-------Login-------")
            user_id, user_name =customer_operation.log_in(sqlConnect, cursor)
            showLandingPage(user_name)
            break
        elif option == "`":
            showLandingPage()
            break
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.")
            continue
# ---</Login>---

# ---</All Shop>---
def showShopPanel(user_name):
    while True:
        print("\n-------All Shops-------")
        print("1. Shop all the shops")
        print("`. back")
        print("0. Exit")
        option = input("Enter number to select option >> ")
        if option == "1":
            print("\n-------All Shops-------")
            Shop_management.showShops(sqlConnect, cursor)
            continue
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.")
            continue
# ---</All Shop>---

# ---</Show Items By Shops>---
def showItempanel(user_name):
    while True:
        print("\n-------Searching-------")
        print("1. Show all the shop")
        print("2. Enter Shop name")
        print("`. Back")
        print("0. Exit")
        option = input("Enter number to select option >> ")
        if option == "1":
            print("\n-------All Shops-------")
            Shop_management.showShops(sqlConnect, cursor)
            print("\n-------All Shops-------")
            continue
        elif option == "2":    # still need to be modified purchase function after show all the items in a shop
            print("\n-------Items-------")
            print("1. Search")
            print("`. Back")
            print("0. Exit")
            option = input("Enter number to select option >> ")
            if option == "1":
                
                shop_name = input("Please input the shop name which you want to search: ")  

                print("\n-------Items-------")
                shop_items = Item_management.get_items_in_a_shop(sqlConnect, cursor, shop_name)

                while True:
                    # show options
                    print("\n\n-------Options-------")
                    print("1. Add item to cart")
                    # print("2. Enter Shop name")
                    print("`. Back")
                    print("0. Exit")                    
                        
                    option2 = input("Enter number to select option >> ")         
                    if option2 == "1":
                        while True: # To ensure item ID be valid
                            item_id = input("Enter item ID >> ")
                            if item_id in shop_items:
                                break
                            else:
                                print("Please input valid item ID.")
                        while True: # To ensure number of item being int
                            item_qty = input("Enter number of item >> ")
                            if item_qty.isdigit() and int(item_qty)>=0:
                                item_qty = int(item_qty)
                                cart = Item_purchase.load_cart(globals.path_cartFile)
                                cart_item_qty = cart[item_id]['count'] if item_id in cart else 0
                                if (cart_item_qty+item_qty) <= shop_items[item_id]['Item remaining']:
                                    # save to cart.txt
                                    for i in range(item_qty):
                                        Item_purchase.write_cart(item_id, shop_items[item_id])  
                                
                                    shop_items = Item_management.get_items_in_a_shop(sqlConnect, cursor, shop_name)

                                    if item_qty > 0:
                                        print("\n Added to cart!")   
                                    break                                     
                                else:
                                    print("Number of the requested item is more than that in stock of shop, please request fewer number of the item")                              
                            else:
                                print("Invalid input for number of item (should be 0 or positive integer), please input again.")
                        


                        continue
                    elif option2 == "`":
                        showLandingPage(user_name)
                        break
                    elif option2 == "0": 
                        closeShop(user_name)    
                    else:
                        print("\n[!] You've entered invalid character.")
                        continue


                continue 
            elif option == "`":
                showLandingPage(user_name)
                break
            elif option == "0": 
                closeShop(user_name)
            else:
                print("\n[!] You've entered invalid character.")
                continue
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0": 
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.")
            continue
# ---</Show Items By Shops>---

# ---</Search Items>---
def searchItemsPanel(user_name):
    while True:
        print("\n-------Searching Items-------")
        print("1. Search items")
        print("`. Back")
        print("0. Exit")
        option = input("Enter number to select option >> ")
        if option == "1":
            print("\n-------Searching Result-------")
            Item_search.search_item(sqlConnect, cursor)
            continue
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.\n")
            continue
# ---</Search Items>---

# ---</Order>---
def purchaseOrderCartPanel(user_name):
    while True:
        print("-------Purchase cart items-------")
        print("y. Yes")
        print("n. No")
        print("`. Back")
        print("0. Exit")
        option = input("Confirm to place order [y/n]>> ") 
        if option == "y":
            Item_purchase.purchase_item_in_cart(sqlConnect, cursor, 1)
            print("\n------------------------------")
            print("Orders have been confirmed")
            print("------------------------------")
            print("Thank you very much for shopping in our shop.\nYour items will be delivered in up to 3 days.")
            print("------------------------------\n")
            showLandingPage(user_name)
            continue
        elif option == "n":
            showLandingPage(user_name)
            continue
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.")
            continue
# ---</Order>---

# ---</Cancel order>---
def cancelOrderPanel(user_name):
    while True:
        print("-------Cancle orders-------")
        print("y. Yes")
        print("n. No")
        print("`. Back")
        print("0. Exit")
        option = input("Confirm to cancle order [y/n]>> ") 
        if option == "y":
            print("\n-------Orders canceling-------")
            Order_canceling.cancel_whole_order(sqlConnect, cursor,user_id)
            showLandingPage(user_name)
            continue
        elif option == "n":
            showLandingPage(user_name)
            continue
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.")
            continue
# ---</Cancel order>---

# ---</Logout>---
def logoutPanel(user_name):
    while True:
        print("\n-------Log out-------")
        print("y. Yes")
        print("n. No")
        print("`. Back")
        print("0. Exit")
        option = input("Confirm to log out [y/n]>> ")
        if option == "y":
            print("\n-------Log in again to confirm-------")
            user_id, user_name = customer_operation.log_out(user_name)
            showLandingPage(user_name)
            continue
        elif option == "n":
            showLandingPage(user_name)
            break
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.")
            continue
# ---</Logout>---

# ---</Management(Shop/Item)>---
def managementPanel(user_name):
    while True:
        print("\n-------Management System-------")
        print("1. Add Shop")
        print("2. Insert New Item")
        print("`. back")
        print("0. Exit")
        option = input("Enter number to select option >> ")
        if option == "1":
            print("\n-------Adding new shop-------")
            print("+. Add a new shop")
            print("`. Back")
            print("0. Exit")
            option = input("Enter number to select option >> ")
            if option == "+":
                print("\n-------Please enter info of shop for shop adding-------")
                name = input("Enter shop name >> ")
                addr = input("Enter shop address >> ")
                Shop_management.insert_shop(name, addr, 0, sqlConnect, cursor)
                continue
            elif option == "`":
                continue
            elif option == "0":
                closeShop(user_name)
            else:
                print("\n[!] You've entered invalid character.")
                continue
        elif option == "2":
            print("-------Adding new item-------")
            print("+. Add new item")
            print("`. Back")
            print("0. Exit")
            option = input("Enter number to select option >> ")
            if option == "+":
                print("\n----Please enter what you want to add----")
                Item_management.insert_item(sqlConnect, cursor)
                continue
            elif option == "`":
                continue
            elif option == "0":
                closeShop(user_name)
            else:
                print("\n[!] You've entered invalid character.")
                continue
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.")
            continue
# ---</Management(Shop/Item)>---

# ---</Delete Account>---
def deleteAccountPanel(user_name):
    while True:
        print("\n-------Delete Account-------")
        print("1. Delete Account(Be careful!)")
        print("`. back")
        print("0. Exit")
        option = input("Enter number to select option >> ")
        if option == "1":
            print("\n----Hope to see you in the future!----")
            customer_operation.close_account(sqlConnect, cursor)
            print("\n----Hope to see you in the future!----")
            user_name = ""
            showLandingPage(user_name)
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0":
            closeShop()
        else:
            print("\n[!] You've entered invalid character.")
            continue
# ---</Delete Account>---









            

        