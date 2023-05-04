import psycopg2
from config import config

def insert_people(name, surname, phone):
    sql = "INSERT INTO PhoneBook(Name, Surname, Phone) VALUES(%s, %s, %s)" #ON CONFLICT (Name, Surname) DO UPDATE Phonebook SET Phone = %s WHERE Name = %s AND Surname = %s
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name, surname, phone))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def upload_from_csv():
    import csv
    with open('contact.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            surname = row['surname']
            phone = row['phone']
            insert_people(name, surname, phone)

        
def delete_person_by_name_surname(name, surname):
    sql = "DELETE FROM PhoneBook WHERE Name = %s AND Surname = %s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name, surname))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def delete_person_by_phone(phone):
    sql = "DELETE FROM PhoneBook WHERE Phone = %s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (phone))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
def update_name(old_name, surname, new_name):
    sql = "UPDATE Phonebook SET Name = %s WHERE Name = %s AND Surname = %s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (new_name, old_name, surname))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def update_surname(name, old_surname, new_surname):
    sql = "UPDATE Phonebook SET Surname = %s WHERE Name = %s AND Surname = %s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (new_surname, name, old_surname))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
def update_phone_by_old_phone(old_phone, new_phone):
    sql = "UPDATE Phonebook SET Phone = %s WHERE Phone = %s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (new_phone, old_phone))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def update_phone_by_name_surname(new_phone, name, surname):
    sql = "UPDATE Phonebook SET Phone = %s WHERE Name = %s AND Surname = %s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (new_phone, name, surname))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    print("""What do you want to do?
1)Add Person 2)Delete Person 3)Change Name
4)Change Surname 5)Change Phone 6)Upload from csv
""")
    option = int(input())
    if option == 1:
    
        number = int(input("Number of person you want to add: "))
        for i in range(number):
            name = str(input("Name: "))
            surname = str(input("Surname: "))
            phone = str(input("Phone Numeber: "))
            insert_people(name, surname, phone)
        print("Completed!")
        
    elif option == 2:
        print("1)Delete by name & surname 2)Delete by phone")
        second_option = int(input())
        if second_option == 1:
            name = str(input("Enter the name: "))
            surname = str(input("Enter the surname: "))
            delete_person_by_name_surname(name, surname)
            print("completed!")
        elif second_option == 2:
            phone = str(input("Enter the phone number: "))
            dele_person_by_phone(phone)
            print("Completed!")

    elif option == 3:
        oldname = str(input("The name of the person you want to change: "))
        surname = str(input("The surname of the person you want to change: "))
        phone = str(input("The phone of the person you want to change: "))
        newname = str(input("Enter the new name: "))
        update_name(oldname, surname, newname, phone)
        print("Completed!")

    elif option == 4:
        name = str(input("The name of the person you want to change: "))
        oldsurname = str(input("The surname of the person you want to change: "))
        phone = str(input("The phone of the person you want to change: "))
        newsurname = str(input("Enter the new surname: "))
        update_surname(name, oldsurname, newsurname, phone)
        print("Completed!")
    
    elif option == 5:
        print("1)Change phone by old phone number 2)Change phone by name & surname")
        second_option = int(input())
        if second_option == 1:
            oldphone = str(input("The phone of the person you want to change: "))
            newphone = str(input("Enter the new phone: "))
            update_phone_by_old_phone(oldphone, newphone)
            print("Completed!")
        elif second_option == 2:
            name = str(input("The name of the person you want to change: "))
            surname = str(input("The surname of the person you want to change: "))
            newphone = str(input("Enter the new phone: "))
            update_phone_by_name_surname(newphone, name, surname)
            print("Completed!")
            
        
    elif option == 6:
        upload_from_csv()
        print("Completed!")
    else:
        print("Invalid option is selected")
