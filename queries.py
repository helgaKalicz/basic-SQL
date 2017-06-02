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
    finally:
        if conn:
            conn.close()


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
    return """SELECT schools.country, COUNT(mentors.id) FROM mentors
              RIGHT JOIN schools ON mentors.city = schools.city GROUP BY schools.country ORDER BY schools.country ASC;"""


def show_contacts():
    return """SELECT schools.name, mentors.first_name, mentors.last_name FROM mentors
              INNER JOIN schools ON mentors.id = schools.contact_person ORDER BY schools.name;"""


def show_applicants():
    return """SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date FROM applicants
              LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
              WHERE applicants_mentors.creation_date >= '2016-01-01' ORDER BY applicants_mentors.creation_date DESC;"""


def show_applicants_and_mentors():
    return """SELECT applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name FROM applicants
              LEFT JOIN (applicants_mentors LEFT JOIN mentors ON applicants_mentors.mentor_id = mentors.id)
              ON applicants.id=applicants_mentors.applicant_id ORDER BY applicants.id ASC;"""
