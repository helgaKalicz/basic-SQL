import psycopg2


def read_user_datas(filename):
    with open(filename) as file:
        return file.read().split(',')


def fetch_database(query):
    try:
        datas = read_user_datas('user.txt')
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(data[0], data[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()


def modify_database(query):
    try:
        datas = read_user_datas('user.txt')
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(data[0], data[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()


def mentors_name():
    return "SELECT first_name, last_name FROM mentors;"


def mentors_nickname():
    return "SELECT nick_name FROM mentors WHERE city = 'Miskolc';"


def carols_datas():
    return "SELECT first_name || ' ' || last_name AS full_name, phone_number FROM applicants WHERE first_name='Carol';"


def other_girls_datas():
    return "SELECT first_name || ' ' || last_name AS full_name, phone_number FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';"


def insert_new_applicant():
    return "INSERT INTO applicants(first_name, last_name, phone_number, email, application_code) SELECT 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823;"


def show_new_applicant():
    return "SELECT * FROM applicants WHERE application_code=54823;"


def update_phone_number():
    return "UPDATE applicants SET phone_number='003670/223-7459' WHERE first_name='Jemima' AND last_name='Foreman';"


def show_updated_number():
    return "SELECT phone_number FROM applicants WHERE first_name='Jemima' AND last_name='Foreman';"


def delete_applicants():
    return "DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';"


def show_all_mentors():
    return "SELECT * FROM mentors;"


def show_all_applicants():
    return "SELECT * FROM applicants;"
