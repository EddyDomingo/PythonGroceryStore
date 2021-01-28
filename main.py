import functions

print(functions.intro())
functions.create_connection()

loop = 0
while loop == 0:
    print("\tMain Menu")
    print("\t01. Register New Customer")
    print("\t02. Choose Products")
    print("\t03. Modify Cart")
    print("\t04. Delete Cart")
    print("\t05. Checkout")
    print("\t06. Exit")
    ch = input("\tPlease Select Your Options (1-6): ")
    print("\tYou selected option number: " + ch)
    print(" ")

    if int(ch) == 1:
        print('\tLets register you as a client')
        fname = input('\tPlease enter your first name: ')
        lname = input('\tPlease enter your last name: ')
        email = input('\tPlease enter your email: ')
        functions.createClient(fname, lname, email)

    elif int(ch) == 2:
        print('\tAvailable Products')
        products = ["Eggs", "Bread", "Milk",
                    "Cheese", "Juice", "Chicken", "Rice"]
        counters = 1
        for i in products:

            print("\t0" + str(counters) + ". " + i)
            counters = counters + 1
        print("\t08. Add to Cart")
        secondLoop = 0
        while secondLoop == 0:
            cartEmail = input('\tEnter client email: ')
            productNumber = input('\tEnter product to purchase: ')
            productAmount = input('\tEnter product amount: ')
            orderOption = input('\tSelect Y or N to add to cart: ')
            if orderOption == "Y":
                secondLoop = 1
                functions.createCart(
                    cartEmail, products[int(productNumber)-1], int(productAmount))
                print("\tAdded to Cart")
                print("  ")
                break

            print('\t', products[int(productNumber)-1], productAmount)

    elif int(ch) == 3:
        thirdLoop = 0
        while thirdLoop == 0:
            modifyEmail = input('\tEnter client email: ')
            functions.queryDB(modifyEmail)
            productName = input(
                '\tEnter product name to modify the amount: ')
            amount = input("\tEnter new amount: ")
            functions.updateDB(int(amount), productName)
            thirdLoop = 1
    elif int(ch) == 4:
        fourthLoop = 0
        while fourthLoop == 0:
            modifyEmail = input('\tEnter client email cart to delete: ')
            functions.deleteDB(modifyEmail)

            fourthLoop = 1

    elif int(ch) == 5:
        fifthhLoop = 0
        while fifthhLoop == 0:
            modifyEmail = input('\tEnter client email cart to purchase: ')
            functions.purchaseCart(modifyEmail)

            fifthhLoop = 1

    elif int(ch) == 6:
        loop = 1

    else:
        print("\tIncorrect Input")


else:
    print("\tExiting program....")
