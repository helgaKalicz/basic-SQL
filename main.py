from flask import Flask, request, render_template, redirect
import psycopg2
import queries

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/mentors')
def mentors():
    return render_template('queries.html',
                           data_list=queries.fetch_database(queries.show_mentors()),
                           table_head=['Mentor first name', 'Mentor last name', 'School name', 'Country'])


@app.route('/all-school')
def all_school():
    return render_template('queries.html',
                           data_list=queries.fetch_database(queries.show_all_school()),
                           table_head=['Mentor first name', 'Mentor last name', 'School name', 'Country'])


@app.route('/mentors-by-country')
def mentors_by_country():
    return render_template('queries.html',
                           data_list=queries.fetch_database(queries.show_mentors_by_country()),
                           table_head=['Country', 'Mentor'])


@app.route('/contacts')
def contacts():
    return render_template('queries.html',
                           data_list=queries.fetch_database(queries.show_contacts()),
                           table_head=['School name', 'Mentor first name', 'Mentor last name'])


@app.route('/applicants')
def applicants():
    return render_template('queries.html',
                           data_list=queries.fetch_database(queries.show_applicants()),
                           table_head=['Applicant first name', 'Application code', 'Creation_date'])


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    return render_template('queries.html',
                           data_list=queries.fetch_database(queries.show_applicants_and_mentors()),
                           table_head=['Applicants first name', 'Application code', 'Mentor first name', 'Mentor last name'])


@app.errorhandler(404)
def error_handling(e):
    return render_template('error.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
