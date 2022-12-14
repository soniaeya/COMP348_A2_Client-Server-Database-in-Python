# echo-client.py

import socket
import sys

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 9999  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    exit_bool = False
    while not exit_bool:
        select = input(
            """Python DB Menu
1. Find customer
2. Add customer
3. Delete customer
4. Update customer age
5. Update customer address
6. Update customer phone
7. Print report
8. Exit
Select: """)
        send = ""

        if not select.isdigit():
            print("Please enter an integer!")
            continue
        select = int(select)


        if select == 1:
            name = input("Please enter a name: ")  # Get user input

            send = str(select) + "&" + name
            s.send(bytes(send, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))
        elif select == 2:

            new_customer_str = ""
            new_customer_name_str = input("Enter the name: ")
            new_customer_str += new_customer_name_str + "|"

            new_customer_age_str = input("Enter the age of the new customer: ")
            new_customer_str += (str(new_customer_age_str) + "|")

            new_customer_address_str = input("Enter the address of the new customer: ")
            new_customer_str += (new_customer_address_str + "|")

            new_customer_phone_num_str = input("Enter the phone number of the new customer: ")
            new_customer_str += new_customer_phone_num_str

            send = str(select) + "&" + new_customer_str
            s.send(bytes(send, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))

        elif select == 3:

            name_3 = input("Please enter the name you wish to remove from the database: ")
            send = str(select) + "&" + name_3
            s.send(bytes(send, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))

        elif select == 4:
            name_4 = input("Please enter the name of the person whose information you want to update from the "
                           "database: ")
            new_age = input("Please enter the age you wish to change to: ")

            send = str(select) + "&" + name_4 + "&" + new_age
            s.send(bytes(send, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))

        elif select == 5:
            name_5 = input("Please enter the name of the person whose information you want to update from the "
                           "database: ")
            new_address = input("Please enter the address you wish to change to: ")

            send = str(select) + "&" + name_5 + "&" + new_address
            s.send(bytes(send, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))
        elif select == 6:
            name_6 = input("Please enter the name of the person whose information you want to update from the "
                           "database: ")
            new_phone_num = input("Please enter the phone number you wish to change to: ")

            send = str(select) + "&" + name_6 + "&" + new_phone_num
            s.send(bytes(send, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))

        elif select == 7:
            send = str(select)
            s.send(bytes(send, 'utf-8'))
            response = s.recv(1024)
            print(response.decode("utf-8"))

        elif select == 8:
            print("Goodbye!")
            exit_bool = True
            s.close()

        else:
            print("Please enter a valid input!")


