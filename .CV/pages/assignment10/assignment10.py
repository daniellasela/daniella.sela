from flask import Flask, url_for, redirect, render_template, request, session, jsonify, Blueprint
import mysql.connector

Assignment10 = Blueprint(
    'Assignment10',
    __name__,
    static_folder='static',
    static_url_path='/pages/Assignments10',
    template_folder='templates'
)

@Assignment10.route('/Assignment10')
def index():
    return redirect('/users')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@Assignment10.route('/users')
def users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('Assignment10.html', users=query_result)


@Assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        query = "insert into users(first_name,last_name,email) values ('%s','%s','%s')" % (firstname, lastname, email)
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return redirect('/users')


@Assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['id']
        query = "delete from users where id ='%s';" % user_id
        interact_db(query, query_type='commit')
        return redirect('/users')
    return redirect('/users')


@Assignment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        user_id = request.form['id']
        if request.form['firstname']:
            newFirstName = request.form['firstname']
            query = "update users set first_name = '%s' where id ='%s';" % (newFirstName, user_id)
            interact_db(query, query_type='commit')
        if request.form['lastname']:
            newLastName = request.form['lastname']
            query = "update users set last_name = '%s' where id ='%s';" % (newLastName, user_id)
            interact_db(query, query_type='commit')
        if request.form['email']:
            newEmail = request.form['email']
            query = "update users set email = '%s' where id ='%s';" % (newEmail, user_id)
            interact_db(query, query_type='commit')
        return redirect('/users')
    return redirect('/users')