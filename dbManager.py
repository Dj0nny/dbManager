import mysql.connector
from mysql.connector import errorcode
 
def menu():
    print("Select an option:\n")
    print("\t 1 - Insert Data")
    print("\t 2 - Print Database")
    print("\t-1 - For aborting the program\n")
    prompt = "Insert option's number: "
    ch = input(prompt)
    return ch

try:
  connection = mysql.connector.connect(user = '....', password = '....', database = '.....') # Your data
  if(connection):
      print("Connection enstablished!\n")
except mysql.connector.Error as err:
 if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
   print("The username or the password is wrong")
 elif err.errno == errorcode.ER_BAD_DB_ERROR:
   print("Database doesn't exist")
 else:
   print(err)



# main
while(exit != -1):
    choice = menu()
    choice = int(choice)
    if(choice == 1):
        cursor1 = connection.cursor()
        name = input("Insert name: \n")
        surname = input("Insert surname: \n")
        cursor1.execute("INSERT INTO `myDb`(`name`, `surname`) VALUES (%s, %s)", (name, surname)) # Change this query with your data
        connection.commit()
        cursor1.close()
    elif(choice == 2):
        cursor2 = connection.cursor()
        cursor2.execute("SELECT * FROM myDB") # Change this query with your data
        print("\n")
        if not cursor2.rowcount:
            print("The database is empty\n")
        else:
            for (name, surname) in cursor2: # Change "name" and "surname" with your variables
                print("\t{}, {}".format(name, surname)) # Change .format(v1, v2, ... , vn) with your variables
        cursor2.close()
        print("\n")
    elif(choice == 3):
        cursor3 = connection.cursor()
        name = input("Insert name: ")
        surname = input("Insert surname: ")
        cursor3.execute("SELECT * FROM prova WHERE nome = %s OR cognome = %s", (name, surname)) # Change this query with your data
        print("\n")
        for (nome, cognome) in cursor3: # Change "name" and "surname" with your variables
            print("\t{}, {}".format(nome, cognome)) # Change .format(v1, v2, ... , vn) with your variables
        cursor3.close()
        print("\n")
    elif(choice == -1):
        exit = -1

connection.close()
print("--- END ---")
