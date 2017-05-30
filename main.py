from flask import Flask, request, render_template, redirect
import psycopg2
import queries as q

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/mentors')
def mentors():
    data_list = q.fetch_database(q.show_mentors())
    return render_template('queries.html', data_list=data_list)


@app.route('/all-school')
def all_school():
    data_list = q.fetch_database(q.show_all_school())
    return render_template('queries.html', data_list=data_list)


@app.route('/mentors-by-country')
def mentors_by_country():
    data_list = q.fetch_database(q.show_mentors_by_country())
    return render_template('queries.html', data_list=data_list)


@app.route('/contacts')
def contacts():
    data_list = []
    return render_template('queries.html', data_list=data_list)


@app.route('/applicants')
def applicants():
    data_list = []
    return render_template('queries.html', data_list=data_list)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    data_list = []
    return render_template('queries.html', data_list=data_list)


@app.errorhandler(404)
def error_handling(e):
    data_list = []
    return render_template('error.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
