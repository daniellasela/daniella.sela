from flask import Flask, render_template, url_for, request, session, redirect
app = Flask(__name__)
import requests

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