from flask import Flask, render_template, url_for, request, session, redirect,Blueprint
import requests
import mysql.connector
import tkinter
from tkinter import messagebox

app = Flask(__name__)
app.secret_key='123'

@app.route('/')
def main_cv():
    return render_template('cv.html')

@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html',
                           Hobbies=['scuba_divign', 'listen_to_music'],
                           Favorite_singers=['john_mayer', 'coldplay', 'ivri_lider', 'idan_raichel'],
                           first_name='Daniella', age=26.9
                           )

@app.route('/assignment9', methods=['GET', 'POST'])
def Assignment_9():
    res = ""
    list = []
    r = requests.get('https://reqres.in/api/users?page=2')

    if r.status_code == 200:
        res_json = r.json()
        users = res_json['data']
    print(users)
    users_names = [u['first_name'] for u in users]
    last_mames = [u['last_name'] for u in users]
    names = []
    emails = {}
    for i in range(len(users_names)):
        full_name = users_names[i] + " " +  last_mames[i]
        names.append(full_name)
        emails[full_name]= users[i]['email']
    if request.method == 'GET':
        message = "Im here!"
        if 'name' in request.args:
            res = request.args['name']
            answer_U = [i for i in names if res in i]
            for v in answer_U:
                list.append(emails[str(v)])
            return render_template('assignment9.html', name=answer_U, email=list, message=message)
    if request.method == 'POST':
        if 'logout' in request.form:
            NICKNAME = ''
            return render_template('assignment9.html', username=NICKNAME)
        if 'username' in request.form:
            NICKNAME = request.form['username']
        else:
            NICKNAME = ''
        return render_template('assignment9.html', session='TRUE', username=NICKNAME)
    return render_template('assignment9.html')

from pages.assignment10.assignment10 import Assignment10
app.register_blueprint(Assignment10)

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Use for INSERT UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int.)
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it is success.
        query_result = cursor.fetchall()
        return_value = query_result

    if return_value == True:
        root = tkinter.Tk()
        root.withdraw()
        # Message Box
        messagebox.showinfo("DataBase Has Been Updated", "The execute was successful")

    connection.close()
    cursor.close()
    return return_value