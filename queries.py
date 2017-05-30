import psycopg2


def read_user_datas(filename):
    with open(filename) as file:
        return (file.read()).split(',')


def fetch_database(query):
    try:
        datas = read_user_datas('user.txt')
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(datas[0], datas[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)
        '''
    finally:
        if conn:
            conn.close()
            '''


def modify_database(query):
    try:
        datas = read_user_datas('user.txt')
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(datas[0], datas[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()


def show_mentors():
    return """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country FROM mentors
              LEFT JOIN schools ON mentors.city = schools.city ORDER BY mentors.id ASC;"""


def show_all_school():
    return """SELECT mentors.first_name, mentors.last_name, schools.name, schools.country FROM mentors
              RIGHT JOIN schools ON mentors.city = schools.city ORDER BY mentors.id ASC;"""


def show_mentors_by_country():
    return """SELECT schools.country, COUNT(mentors.id) FROM schools
              LEFT JOIN mentors ON schools.city = mentors.city GROUP BY schools.country ORDER BY schools.country ASC;"""


def show_contacts():
    pass


def show_applicants():
    pass


def show_applicants_and_mentors():
    pass
