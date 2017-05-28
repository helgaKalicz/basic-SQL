from flask import Flask, request, render_template, redirect
import psycopg2
import queries as q

app = Flask(__name__)


@app.route('/')
@app.route('/mentors')
@app.route('/all-school')
@app.route('/mentors-by-country')
@app.route('/contacts')
@app.route('/applicants')
@app.route('/applicants-and-mentors')
@app.errorhandler(404)
def error_handling(e):
    return render_template('error.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
