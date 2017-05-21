import psycopg2


def connection(question):
    try:
        connect_str = "dbname='kalicz' user='kalicz' host='localhost' password='nincsen'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(question)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)


def modify_database(question):
    try:
        connect_str = "dbname='kalicz' user='kalicz' host='localhost' password='nincsen'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(question)
    except Exception as e:
        print(e)


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


def print_menu():
    menu_list = ['0 Exit program',
                 '1 Show mentors',
                 '2 Show mentors from Miskolc',
                 '3 Show Carol\'s data',
                 '4 Show other girls\' datas',
                 '5 Add new applicant',
                 '6 Update phone number',
                 '7 Delete applicant',
                 '8 Show all mentors\' datas',
                 '9 Show all apllicants\' datas']
    for menu_option in menu_list:
        print(menu_option)


def print_result(datas):
    for data in datas:
        print('  '.join(map(str, data)))
    print()
