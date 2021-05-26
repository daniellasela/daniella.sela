from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, world'

@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html',
                           Hobbies=['scuba_divign', 'listen_to_music'],
                           Favorite_singers=['john_mayer', 'coldplay', 'ivri_lider', 'idan_raichel'],
                           first_name='Daniella', age=26.9
                           )
@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    if request.method == 'POST':
        return
    else:
        return render_template('assignment9.html')
