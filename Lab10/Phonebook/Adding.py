import psycopg2
from config import config

def insert_people_list(people_list):
    sql = "INSERT INTO PhoneBook(Name, Surname, Phone) VALUES(%s, %s, %s) ON CONFLICT (Name, Surname, Phone) DO NOTHING"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, people_list)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def delete_person(name, surname):
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

if __name__ == '__main__':
    print("""What do you want to do?
1)Add Person 2)Delete Person""")
    option = int(input())
    if option == 1:
        
        number1 = int(input("Number of person you want to add: "))
        for i in range(number1):
            name = str(input("Name: "))
            surname = str(input("Surname: "))
            phone = str(input("Phone Numeber: "))
            print("")
            insert_people_list([(name, surname, phone)])
        print("Completed!")
        
    elif option == 2:
        number2 = int(input("Number of person you want to delete: "))
        for i in range(number2):
            name = str(input("Enter the name: "))
            surname = str(input("Enter the surname: "))
            delete_person(name, surname)

        print("Completed!")
    else:
        print("Invalid option is selected")
