from prettytable import DEFAULT, PrettyTable

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
        print(
            "\n|================|                 |================|\n|================| Online-Shopping |================|\n|================|                 |================|")
        if user_name != '':
            print("\nWelcome %s!" % user_name)
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

        print("7. Place order")
        print("8. Cancel order")

        if user_name != '': # ie logged in
            print("9. Logout")
                
        print("m. Management(Shop/Item)")
        print("*. Delete Account")
        print("0. Exit")
        option = input("Your choice >> ")
        if option == "1":
            RegistrationPanel()
        elif option == "2":
            user_id, user_name=loginPanel()
        elif option == "3":
            showShopPanel(user_name)
        elif option == "4":
            showItempanel(user_name)
        elif option == "5":
            searchItemsPanel(user_name)
        elif option == "6":
            # cart place in here 6
            cartPanel(user_name)        
        elif option == "7":
            if user_name != '':                
                purchaseOrderCartPanel(user_name)
            else:
                print("\n[!] Please login before placing order")
            continue
        elif option == "8":
            if user_name != '':
                cancelOrderPanel(user_name)
            else:
                print("\n[!] Please login before placing order")
            continue            
        elif option == "9":
            if user_name != '':
                logoutPanel(user_name)
        elif option == "m":
            managementPanel(user_name)
        elif option == "*":
            deleteAccountPanel(user_name)
        elif option == "0":
            # clear cart
            open(globals.path_cartFile, 'w').close()            
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.")
            continue

        break


# ---</MAINPAGE>---

# ---</Exit>---
def closeShop(user_name):
    print("\n----------------------------------------")
    print("\nSee you again %s!" % user_name)
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
    global user_id
    while True:
        print("\n-------Login-------")
        print("1. Log in with Name amd Password")
        print("`. back")
        print("0. Exit")
        option = input("Enter number to select option >> ")
        if option == "1":
            print("\n-------Login-------")
            user_id, user_name = customer_operation.log_in(sqlConnect, cursor)
            showLandingPage(user_name)
            # add return values user_id and user_name
            return user_id, user_name
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
        elif option == "2":  # still need to be modified purchase function after show all the items in a shop
            print("\n-------Items-------")
            print("1. Search")
            print("`. Back")
            print("0. Exit")
            option = input("Enter number to select option >> ")
            if option == "1":

                shop_name = input("Please input the shop name which you want to search: ")

                # print("\n-------Items in Shop-------")
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
                        while True:  # To ensure item ID be valid
                            item_id = input("Enter item ID >> ")
                            if item_id in shop_items:
                                break
                            else:
                                print("Please input valid item ID.")
                                # if input wrong, can let customer select whether continue to input'''
                                print("\n\n-------Options-------")
                                print("1. Add again")
                                print("`. Back")
                                option3 = input("Enter number to select option >> ")
                                if option3 == "1":
                                    continue
                                elif option3 == "`":
                                    showLandingPage(user_name)
                                else:
                                    print("\n[!] You've entered invalid character.\n")
                                    continue
                        while True:  # To ensure number of item being int
                            item_qty = input("Enter number of item >> ")
                            if item_qty.isdigit() and int(item_qty) >= 0:
                                item_qty = int(item_qty)
                                cart = Item_purchase.load_cart(globals.path_cartFile)
                                cart_item_qty = cart[item_id]['count'] if item_id in cart else 0
                                if (cart_item_qty + item_qty) <= shop_items[item_id]['Item remaining']:
                                    # save to cart.txt
                                    for i in range(item_qty):
                                        Item_purchase.write_cart(item_id, shop_items[item_id])

                                    shop_items = Item_management.get_items_in_a_shop(sqlConnect, cursor, shop_name)

                                    if item_qty > 0:
                                        print("\n Added to cart!")
                                    break
                                else:
                                    print(
                                        "Number of the requested item (%s) plus existing shopping cart items (%s) "
                                        "is more than that of remaining in shop stock (%s)\n"
                                        "Please request fewer number of the item" % (
                                            item_qty, cart_item_qty, shop_items[item_id]['Item remaining'],))
                            else:
                                print(
                                    "Invalid input for number of item (should be 0 or positive integer), please input again.")

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
            item_keyword = input("Please input the item name or keywords which you want to search: ")
            search_item_result = Item_search.search_item(sqlConnect, cursor, item_keyword)
            if len(search_item_result) == 0:
                continue
            while True:
                # show options
                print("\n\n-------Options-------")
                print("1. Add item to cart")
                print("`. Back")
                print("0. Exit")

                option2 = input("Enter number to select option >> ")
                if option2 == "1":
                    while True:  # To ensure item ID be valid
                        item_id = input("Enter item ID >> ")
                        if item_id in search_item_result:
                            break
                        else:
                            print("Please input valid item ID.")
                            # if input wrong, can let customer select whether continue to input'''
                            print("\n\n-------Options-------")
                            print("1. Add again")
                            # print("2. Enter Shop name")
                            print("`. Back")
                            option3 = input("Enter number to select option >> ")
                            if option3 == "1":
                                continue
                            elif option3 == "`":
                                showLandingPage(user_name)
                            else:
                                print("\n[!] You've entered invalid character.\n")
                                continue

                    while True:  # To ensure number of item being int
                        item_qty = input("Enter number of item >> ")
                        if item_qty.isdigit() and int(item_qty) >= 0:
                            item_qty = int(item_qty)
                            cart = Item_purchase.load_cart(globals.path_cartFile)
                            cart_item_qty = cart[item_id]['count'] if item_id in cart else 0
                            if (cart_item_qty + item_qty) <= search_item_result[item_id]['Item remaining']:
                                # save to cart.txt
                                for i in range(item_qty):
                                    Item_purchase.write_cart(item_id, search_item_result[item_id])

                                search_item_result = Item_search.search_item(sqlConnect, cursor, item_keyword)

                                if item_qty > 0:
                                    print("\n Added to cart!")
                                break
                            else:
                                print(
                                    "Number of the requested item (%s) plus existing shopping cart items (%s) "
                                    "is more than that of remaining in shop stock (%s)\n"
                                    "Please request fewer number of the item" % (
                                        item_qty, cart_item_qty, search_item_result[item_id]['Item remaining'],))
                        else:
                            print(
                                "Invalid input for number of item (should be 0 or positive integer), please input again.")
                # continue
                elif option2 == "`":
                    showLandingPage(user_name)
                    break
                elif option2 == "0":
                    closeShop(user_name)
                else:
                    print("\n[!] You've entered invalid character.\n")
                    continue
        # continue
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.\n")
            continue
# ---</Search Items>---

# ---</Cart>---
def showRemoveProductPanel(dict_cart_items, user_name):
    while True:
        cartFileReadAndUpdate = open(
            globals.path_cartFile, "r+")
        cartFileLines = cartFileReadAndUpdate.readlines()
        cartFileLinesLength = len(cartFileLines)

        print("\n-----Remove Item(s) from Cart-----")

        print("Please select option or enter item ID to remove it from the cart")
        print('`. Back')
        print("0. Exit")

        # for i in range(cartFileLinesLength):
        #     print(f'{i + 1} - {cartFileLines[i].rstrip()}')

        option = input("Enter specific character to select option or enter item ID >> ")


        if option in dict_cart_items:

            # cartFileLinesUpdated = cartFileLines[:int(
            #     option) - 1] + cartFileLines[int(option):]
            
            cartFileLines_copied = cartFileLines.copy()
            # print((cartFileLines_copied))
            i = 0
            while i < len(cartFileLines_copied):
                if cartFileLines_copied[i].startswith(option):
                    del cartFileLines_copied[i]
                    i -= 1
                i += 1

            cartFileWrite = open(
                globals.path_cartFile, "w")
            cartFileWrite.writelines(cartFileLines_copied)
            cartFileWrite.close()

            print("\n----------------------------------------")
            print("SUCCESS")
            print("Item(s) removed")
            print("----------------------------------------\n")
        elif option == "`":
            showLandingPage(user_name)
            return
        elif option == "0":
            closeShop(user_name) 
        else:
            print("\n[!] You've entered invalid character.")
            continue

def cartPanel(user_name):
    # while True:
    #     print("\n-------Searching Items-------")
    #     print("1. Search items")
    #     print("`. Back")
    #     print("0. Exit")
    #     option = input("Enter number to select option >> ")
    #     if option == "1":
    #         print("\n-------Searching Result-------")
    #         Item_search.search_item(sqlConnect, cursor)
    #         continue
    #     elif option == "`":
    #         showLandingPage(user_name)
    #         break
    #     elif option == "0":
    #         closeShop(user_name)
    #     else:
    #         print("\n[!] You've entered invalid character.\n")
    #         continue

    while True:
        cartFileReadAndUpdate = open(
            globals.path_cartFile, "r+")
        cartFileLines = cartFileReadAndUpdate.readlines()
        cartFileLinesLength = len(cartFileLines)

        dict_cart_items = Item_purchase.load_cart(globals.path_cartFile)

        print("\n-----Cart-----")
        # if cartFileLinesLength != 0:
        #     print('1. Order')
        #     print('-. Remove product')
        # print('`. Back')
        # print('0. Exit')

        print("<>---Item(s) in Cart---<>")
        if cartFileLinesLength == 0:
            print("No item found.")
        elif cartFileLinesLength != 0:
            # for i in range(cartFileLinesLength):
            #     cart_item = cartFileLines[i].rstrip()
            #     # Latest version of cart file
            #     splitted = cart_item.split(":")
            #     item_id = splitted[0]
            #     cart_item = splitted[1]
            #     item_price = splitted[2].replace('$','')
            #     print(f'<> {cart_item}')

            # "name": item_name,
            # "count": 1,
            # "total_price": item_price       
            #      
            table = PrettyTable(['Item_ID', 'Item_Name', 'Quantity', 'Price'])

            for key in dict_cart_items:
                table.add_row([key, dict_cart_items[key]['name'], dict_cart_items[key]['count'], dict_cart_items[key]['total_price']])

            table.set_style(DEFAULT)
            print(table)                

            print(f"<>---Total Price: ${Item_purchase.checkTotalAmountOfProductsInCart()}---<>")

        print("\n\n-------Options-------")
        if cartFileLinesLength != 0:
            print('1. Order')
            print('-. Remove item(s)')
        print('`. Back')
        print('0. Exit')            

        option = input("Your choice >> ")
        if option == "0":
            closeShop(user_name)            
        elif option == "`":
            showLandingPage(user_name)
            return
        elif option == "1" and cartFileLinesLength != 0:
            # showOrderPanel("cart")
            if user_name != '':
                purchaseOrderCartPanel(user_name) #user_name
                return
            else:
                print("\n[!] Please login before placing order")
                showLandingPage(user_name)
                return
        elif option == "-" and cartFileLinesLength != 0:
            showRemoveProductPanel(dict_cart_items, user_name)
            return
        else:
            print("\n[!] You've entered invalid character.")        
# ---</Cart>---

# ---</Order>---
def purchaseOrderCartPanel(user_name):

    while True:
        print("-------Purchase cart items-------")
        cart_not_empty = len([x.strip() for x in open(globals.path_cartFile)])>0 

        if cart_not_empty:
            print("y. Yes")
            print("n. No")
        else:
            print("Cart is empty, please add item(s) to cart before purchasing")

        print("`. Back")
        print("0. Exit")
        
        if cart_not_empty:
            option = input("Confirm to place order [y/n]>> ")
        else:
            option = input("Enter character to select option>> ")
        
        if option == "y":
            if cart_not_empty:
                Item_purchase.purchase_items_in_cart(sqlConnect, cursor, user_id) #user_name
                print("\n------------------------------")
                print("Orders have been confirmed")
                print("------------------------------")
                print("Thank you very much for shopping in our shop.\nYour items will be delivered in up to 3 days.")
                print("------------------------------\n")
                showLandingPage(user_name)
            else:
                print("\n[!] You've entered invalid character.\n")

            continue
        elif option == "n":
            if cart_not_empty:
                showLandingPage(user_name)
            else:
                print("\n[!] You've entered invalid character.\n")
            
            continue
        elif option == "`":
            showLandingPage(user_name)
            break
        elif option == "0":
            closeShop(user_name)
        else:
            print("\n[!] You've entered invalid character.\n")
            continue


# ---</Order>---

# ---</Cancel order>---
def cancelOrderPanel(user_name):
    while True:
        print("\n-------Cancel orders-------")

        # Show order list
        Order_canceling.get_orders(sqlConnect, cursor, user_id)#user_name


        print("1. Cancel order")
        print("2. Cancel item(s) in order")
        print("`. Back")
        print("0. Exit")
        option = input("Enter number to select option >> ")
        if option == "1":
            print("\n-------Orders canceling-------")
            print("\n-------Options-------")
            print("`. Back")
            order_id = input("Enter character to select option or input order ID >> ")
            if order_id != '`':
                Order_canceling.cancel_user_single_order(sqlConnect, cursor, user_id, order_id)#user_name
            # showLandingPage(user_name)
            continue
        elif option == "2":
            print("\n-------Order item(s) canceling-------")

            back_pressed = False
            while True:
                print("\n-------Options-------")
                print("`. Back")
                order_id = input("Enter character to select option or input order ID to view content of order >> ")
                if order_id == '`':
                    back_pressed = True
                    break

                # Show order content
                items_order = Order_canceling.get_items_of_order(sqlConnect, cursor, user_id, order_id)#user_name

                if len(items_order) > 0:
                    break
                else:
                    print("\nInvalid order ID, please try again.")
            
            if back_pressed:
                continue
            
            print("\n-------Options-------")
            print("`. Back")            
            item_id = input("Enter character to select option or input item ID going to be removed >> ")
            if order_id != '`':
                Order_canceling.cancel_order_single_item(sqlConnect, cursor, user_id, order_id, item_id)#user_name

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
    global user_id
    while True:
        print("\n-------Log out-------")
        print("y. Yes ([!] CART WILL BE EMPTIED)")
        print("n. No")
        print("`. Back")
        print("0. Exit")
        option = input("Confirm to log out [y/n]>> ")
        if option == "y":
            print("\n-------Log in again to confirm-------")
            user_id, user_name = customer_operation.log_out(user_name)
            # clear cart
            open(globals.path_cartFile, 'w').close()
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
                shop_id = input("Enter shop ID >> ")
                name = input("Enter shop name >> ")
                addr = input("Enter shop address >> ")
                Shop_management.insert_shop(shop_id, name, addr, 0, sqlConnect, cursor)
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
