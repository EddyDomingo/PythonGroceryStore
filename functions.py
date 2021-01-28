import sqlite3
from sqlite3 import Error


def intro():
    a = """
        Welcome to the Grocery Buying System
        Author: Eddy Alvarado
        Written: Python
        """
    return a


def create_connection():
    try:
        # Create database with this name and saved
        conn = sqlite3.connect('GroceryDB.db')
        c = conn.cursor()

        # Create tables - User
        # c.execute(('''CREATE TABLE CLIENTS
        #       ([generated_id] INTEGER PRIMARY KEY,[First_Name] text, [Last_Name] text, [Email] text)'''))

        c.execute(('''CREATE TABLE CART
                ([Email] text,[Products] text)'''))

        c.execute(('''CREATE TABLE PURCHASE
                ([Email] text,[Products] text)'''))

        conn.commit()
    except:
        print("\tDatabases Created and Ready")


def createClient(fname, lname, email):
    try:
        conn = sqlite3.connect('GroceryDB.db')
        cursor = conn.cursor()

        cursor.execute(
            '''INSERT INTO CLIENTS (First_Name, Last_Name, Email)
            VALUES(?,?,?)''', (fname, lname, email))

        conn.commit()
        print("\tClient created succesfully!")
        # cursor.close()
        # conn.close()

    except:
        print("\tClient not created!")


def createCart(email, product, amount):
    try:
        conn = sqlite3.connect('GroceryDB.db')
        cursor = conn.cursor()

        cursor.execute(
            '''INSERT INTO CART (Email, Products, Amount)
            VALUES(?,?,?)''', (email, product, amount))

        conn.commit()
        print("\tCart created succesfully!")
        # cursor.close()
        # conn.close()

    except:
        print("\tCart not created!")


def queryDB(email):

    try:
        conn = sqlite3.connect('GroceryDB.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM CART WHERE Email=?""", (email,))

        rows = cursor.fetchall()

        for row in rows:
            print("\tProduct :", row[1])
            print("\tAmount :", row[2])
            print(" ")
        conn.commit()
    except:
        print("\tDid not find email")


def updateDB(amount, product):

    try:
        conn = sqlite3.connect('GroceryDB.db')
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE CART SET Amount = ? WHERE Products=?""", (amount, product))
        conn.commit()
        print("\tRecord Updated successfully ")
        print(" ")
        cursor.close()
    except:
        print("\tRecord Failed to Update ")


def deleteDB(email):

    try:
        conn = sqlite3.connect('GroceryDB.db')
        cursor = conn.cursor()

        cursor.execute(
            """DELETE FROM CART WHERE Email=?""", (email,))
        conn.commit()
        print("\tRecord deleted successfully ")
        print(" ")
        cursor.close()
    except:
        print("\tRecord Failed to delete! ")


def purchaseCart(email):

    try:
        conn = sqlite3.connect('GroceryDB.db')
        cursor = conn.cursor()

        cursor.execute(
            """SELECT * FROM CART WHERE Email=?""", (email,))

        rows = cursor.fetchall()

        for row in rows:
            print("\tProduct :", row[1])
            print("\tAmount :", row[2])
            print(" ")

        cursor.execute(
            '''INSERT INTO PURCHASE (Email, Products, Amount)
            VALUES(?,?,?)''', (row[0], row[1], row[2]))

        conn.commit()
        print("\tPurchase completed! ")
        print(" ")
        cursor.close()
    except:
        print("\tPurchase not completed! ")
