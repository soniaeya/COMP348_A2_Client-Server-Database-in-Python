
file = open("data.txt", "r")
database = []
counter = 0

# User Prompt String


for i in file:
    # i: raw string from file
    i = "".join(i.split())  # Deletes all whitespace, tabs, and spaces
    # i: string with | as delimiter
    split = i.split("|")  # Creates a list from the "|" separator
    database.append(split)  # Puts all the lists into a database list of lists

file.close()

exit_bool = False
while not exit_bool:

    select = int(input("""
Python DB Menu
1. Find customer
2. Add customer
3. Delete customer
4. Update customer age
5. Update customer address
6. Update customer phone
7. Print report
8. Exit
Select: """))

    if select == 1:
        name = input("Please enter a name: ") # Get user input

        # name = "Joh"
        name_bool = False
        for i in database:
            if name == i[0]:
                name_bool = True
                print(i)
                # ['John', '43', '123\tApple\tstreet', '514\t428-3452\n']

        if not name_bool:
            print(name + " not found in database")

    elif select == 2:
        new_customer_list = []
        new_customer_str = ""
        new_customer_name_str = input("Enter the name: ")
        new_customer_list.append(new_customer_name_str)

        name_bool = False

        for i in database:
            if new_customer_name_str == i[0]:
                name_bool = True

        if name_bool:
            print("Customer already in database")
            continue

        else:
            new_customer_str += new_customer_name_str + "|"

            new_customer_age_str = input("Enter the age of the new customer: ")
            new_customer_list.append(new_customer_age_str)
            new_customer_str += (new_customer_age_str + "|")

            new_customer_address_str = input("Enter the address of the new customer: ")
            new_customer_list.append(new_customer_address_str)
            new_customer_str += (new_customer_address_str + "|")

            new_customer_phone_num_str = input("Enter the phone number of the new customer: ")
            new_customer_str += new_customer_phone_num_str
            new_customer_list.append(new_customer_phone_num_str)

            database.append(new_customer_list)

            print(new_customer_str)

            file_append = open("data.txt", "a")
            file_append.write(new_customer_str+"\n")
            file_append.close()

            print("You have successfully entered " + new_customer_name_str + " into the database!")




    elif select == 3:
        print("Delete a customer: ")

    elif select == 4:
        print("Update customer age: ")

    elif select == 5:
        print("Update customer address: ")
    elif select == 6:
        print("Update customer phone: ")
    elif select == 7:
        print("Print Report: ")
    elif select == 8:
        print("You have exited the database!")
        exit_bool = True
    else:
        print("Please choose a valid option!")
