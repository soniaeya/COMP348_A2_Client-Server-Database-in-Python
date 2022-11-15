# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 9999  # Port to listen on (non-privileged ports are > 1023)

file = open("data.txt", "r")
database = []
counter = 0

# User Prompt String


for i in file:
    # i: raw string from file
    # i = "".join(i.split())  # Deletes all whitespace, tabs, and spaces

    #i = i.replace("\t", "")
    i = i.replace("\n", "")

    # i: string with | as delimiter
    split = i.split("|")  # Creates a list from the "|" separator
    database.append(tuple(split))  # Puts all the lists into a database list of lists

file.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        while True:
            request = conn.recv(1024)
            request = request.decode("utf-8")

            if request == "":
                select = 0
            else:
                request_list = request.split("&")
                select = int(request_list[0])



            break_out_flag = False

            if select == 1:
                input_str = str(request_list[1])

                name_bool = False
                for i in database:
                    if input_str == i[0]:
                        name_bool = True
                        customer_info = ""
                        for j in i:
                            customer_info += j + "|"

                        customer_info = "Server Response: " + str(customer_info[:len(customer_info) - 1]) + "\n"
                        conn.send(bytes(customer_info, 'utf-8'))

                if not name_bool:
                    name_exist = bytes("Server Response: " + input_str + " not found in database", 'utf-8')
                    conn.send(name_exist)
                not_stopping = False

            elif select == 2:
                input_str = str(request_list[1])
                new_customer_info = input_str.split("|")
                name_bool = False
                for i in database:
                    if new_customer_info[0] == i[0]:
                        name_bool = True

                if name_bool:
                    response_2_bad = "Customer already exists\n"
                    conn.send(bytes(response_2_bad, 'utf-8'))

                else:
                    database.append(tuple(new_customer_info))
                    file_append = open("data.txt", "a")
                    file_append.write("\n" + input_str)
                    file_append.close()
                    response_2_good = "You have successfully entered information into the database!"
                    conn.send(bytes(response_2_good, 'utf-8'))

            elif select == 3:
                input_str = str(request_list[1])
                for i in database:
                    if input_str == i[0]:
                        database.remove(i)

                        replacement_file_text = ""

                        with open("data.txt", "r") as input:
                            # iterate all lines from file
                            for line in input:
                                # if substring contain in a line then don't write it
                                if input_str not in line.strip("\n"):
                                    replacement_file_text += line
                            input.close()
                        with open("data.txt", "w") as file_rewrite:
                            file_rewrite.truncate
                            file_rewrite.write(replacement_file_text)

                        response_3_good = "You have successfully removed " + input_str
                        conn.send(bytes(response_3_good, 'utf-8'))
                        break_out_flag = True
                        break
                    if break_out_flag:
                        break

                if counter == len(database) - 1:
                    response = "Customer does not exist"
                    conn.send(bytes(response, 'utf-8'))

            elif select == 4:
                input_str = str(request_list[1])
                age = request_list[2]
                counter = -1
                for i in database:
                    counter += 1
                    if input_str == str(i[0]):
                        info_as_list = list(database[counter])
                        info_as_list[1] = age
                        info_as_tuple = tuple(info_as_list)

                        database[counter] = info_as_tuple
                        new_info_str = ""

                        for j in info_as_tuple:
                            new_info_str += j + "|"

                        new_info_str = new_info_str[:len(new_info_str) - 1]
                        #new_info_str += "\n"

                        replacement_file_text = ""

                        with open("data.txt", "r") as input:
                            # iterate all lines from file
                            for line in input:
                                # if substring contain in a line then don't write it

                                if input_str in line.strip("\n"):
                                    replacement_file_text += new_info_str
                                    continue
                                replacement_file_text += line
                            input.close()
                        with open("data.txt", "w") as file_rewrite:
                            file_rewrite.truncate
                            file_rewrite.write(replacement_file_text)

                        response = "The database has been updated!"
                        conn.send(bytes(response, 'utf-8'))
                        break_out_flag = True
                        break
                    if break_out_flag:
                        break

                if counter == len(database) - 1:
                    response = "Customer not found"
                    conn.send(bytes(response, 'utf-8'))

            elif select == 5:
                input_str = str(request_list[1])

                new_address = request_list[2]
                counter = -1
                for i in database:
                    counter += 1
                    if input_str == str(i[0]):
                        info_as_list = list(database[counter])
                        info_as_list[2] = new_address
                        info_as_tuple = tuple(info_as_list)

                        database[counter] = info_as_tuple
                        new_info_str = ""

                        for j in info_as_tuple:
                            new_info_str += j + "|"

                        new_info_str = new_info_str[:len(new_info_str) - 1]
                        #if counter != len(database)-1:
                         #   new_info_str += "\n"

                        replacement_file_text = ""

                        with open("data.txt", "r") as input:
                            # iterate all lines from file
                            for line in input:
                                # if substring contained in a line then don't write it

                                if input_str in line.strip("\n"):
                                    replacement_file_text += new_info_str
                                    continue
                                replacement_file_text += line
                            input.close()
                        with open("data.txt", "w") as file_rewrite:
                            file_rewrite.truncate
                            file_rewrite.write(replacement_file_text)

                        response = "The database has been updated!"
                        conn.send(bytes(response, 'utf-8'))
                        break_out_flag = True
                        break
                    if break_out_flag:
                        break

                if counter == len(database) - 1:
                    response = "Customer not found"
                    conn.send(bytes(response, 'utf-8'))

            elif select == 6:
                input_str = str(request_list[1])
                new_phone_num = str(request_list[2])
                counter = -1

                for i in database:
                    counter += 1
                    if input_str == str(i[0]):
                        info_as_list = list(database[counter])
                        info_as_list[3] = new_phone_num
                        info_as_tuple = tuple(info_as_list)

                        database[counter] = info_as_tuple
                        new_info_str = ""

                        for j in info_as_tuple:
                            new_info_str += j + "|"

                        new_info_str = new_info_str[:len(new_info_str) - 1]
                        new_info_str += "\n"
                        replacement_file_text = ""

                        with open("data.txt", "r") as input:
                            # iterate all lines from file
                            for line in input:
                                # if substring contain in a line then don't write it

                                if input_str in line.strip("\n"):
                                    replacement_file_text += new_info_str
                                    continue
                                replacement_file_text += line
                            input.close()
                        with open("data.txt", "w") as file_rewrite:
                            file_rewrite.truncate
                            file_rewrite.write(replacement_file_text)
                            print("Option 6")
                            print(database)
                        response = "The database has been updated!"
                        conn.send(bytes(response, 'utf-8'))
                        break_out_flag = True
                        break
                    if break_out_flag:
                        break

                if counter == len(database)-1:
                    response = "Customer not found"
                    conn.send(bytes(response, 'utf-8'))

            elif select == 7:

                sort_database = sorted(database)
                txt = "** Python DB contents **+\n"
                for i in sort_database:
                    for j in i:
                        txt += j + "|"
                    txt = txt[:len(txt) - 1]
                    txt += "\n"

                conn.send(bytes(txt, 'utf-8'))

            elif select == 8:
                print()
