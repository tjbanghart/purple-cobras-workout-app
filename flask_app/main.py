from flask import Flask, render_template
import mysql.connector as mariadb
import json

app = Flask(__name__)
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
CORS(app)

@app.route('/completed/<user_id>')
def get_completed(user_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT w.name FROM workouts w " 
        "JOIN completed c ON w.workout_id = c.workout_id "
        "JOIN users u ON c.user_id = u.user_id "
        "WHERE u.user_id = " + str(user_id) + " ORDER BY completed_id DESC;"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()
    return json.dumps(data)

@app.route('/favorites/<user_id>')
def get_favorites(user_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT w.name FROM workouts w " 
        "JOIN favorites f ON w.workout_id = f.workout_id "
        "JOIN users u ON f.user_id = u.user_id "
        "WHERE u.user_id = " + str(user_id) + " ORDER BY favorite_id DESC;;"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return json.dumps(data)

@app.route('/todo/<user_id>')
def get_todo(user_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT w.name FROM workouts w " 
        "JOIN todo td ON w.workout_id = td.workout_id "
        "JOIN users u ON td.user_id = u.user_id "
        "WHERE u.user_id = " + str(user_id) + " ORDER BY todo_id DESC;"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return json.dumps(data)

@app.route('/user/<user_id>')
def get_user(user_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT username, birthdate, gender FROM users WHERE user_id = " + str(user_id) + ";"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()
    for i in data:
        i['birthdate'] = i['birthdate'].strftime('%m/%d/%Y')

    return json.dumps(data)

@app.route('/workout/<workout_id>')
def get_workout(workout_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT * FROM workouts WHERE workout_id = " + str(workout_id) + ";"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    cnx.close()
    data[0]['rating'] = get_workout_rating(workout_id)
    return json.dumps(data)

@app.route('/allworkouts')
def get_all_workouts():
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT * FROM workouts ORDER BY workout_id DESC;"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()
    for workout in data:
        workout['rating'] = get_workout_rating(workout['workout_id'])
    return json.dumps(data)

def get_workout_rating(workout_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT AVG(wr.rating) AS rating FROM workout_ratings wr "
        "JOIN workouts w ON wr.workout_id = w.workout_id "
        "WHERE wr.workout_id = " + str(workout_id) +";"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()
    return str(data[0]['rating'])

@app.route('/forum')
def get_forum():
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT thread_id, name, datetime FROM threads ORDER BY DATETIME DESC;"
    )

    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()
    for i in data:
        i['datetime'] = i['datetime'].strftime('%m/%d/%Y')
        i['rating'] = get_thread_rating(i['thread_id'])

    return json.dumps(data)

@app.route('/thread/<thread_id>')
def get_thread(thread_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT u.username AS 'username', t.name as 'thread_name', t.datetime, t.content FROM threads t "
        "JOIN users u ON t.user_id = u.user_id "
        "WHERE t.thread_id = " + thread_id+";"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    thread_info = cursor.fetchall()
    cnx.close()
    for i in thread_info:
        i['datetime'] = i['datetime'].strftime('%m/%d/%Y')

    comments = get_thread_comments(thread_id)
    pictures = get_pictures(thread_id)
    videos = get_pictures(thread_id)
    rating = get_thread_rating(thread_id)
    data = [{"thread": thread_info, "comments": comments, "pictures": pictures, "videos": videos, "rating": rating}]

    return json.dumps(data)

def get_thread_comments(thread_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT u.username AS 'username', c.datetime, c.content FROM comments c "
        "JOIN users u ON c.user_id = u.user_id "
        "JOIN threads t ON c.thread_id = t.thread_id "
        "WHERE t.thread_id = " + thread_id+";"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()
    for i in data:
        i['datetime'] = i['datetime'].strftime('%m/%d/%Y')

    return data

def get_pictures(thread_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT link FROM pictures WHERE thread_id = " + thread_id+";"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data

def get_videos(thread_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT link FROM videos WHERE thread_id = " + thread_id+";"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data

def get_thread_rating(thread_id):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    query = (
        "SELECT AVG(tr.rating) AS rating FROM thread_ratings tr "
        "JOIN threads t ON tr.thread_id = t.thread_id "
        "WHERE tr.thread_id = " + str(thread_id) +";"
    )
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()
    return str(data[0]['rating'])

if __name__ == '__main__':
    app.run(debug=True)

