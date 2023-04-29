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


if __name__ == '__main__':
    number = int(input("Number of people you want to add: "))

    for i in range(number):
        name = str(input("Name: "))
        surname = str(input("Surname: "))
        phone = str(input("Phone Numeber: "))
        insert_people_list([(name, surname, phone)])

