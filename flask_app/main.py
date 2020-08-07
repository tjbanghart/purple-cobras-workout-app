from flask import Flask, render_template
from flask_cors import CORS
import mysql.connector as mariadb
import json

app = Flask(__name__)
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
CORS(app)


def make_query(query):
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()
    return data

def get_workout_list(user_id, workout_list, table_id):
    query = (
        "SELECT w.name FROM workouts w " 
        "JOIN " + workout_list + " x ON w.workout_id = x.workout_id "
        "JOIN users u ON x.user_id = u.user_id "
        "WHERE u.user_id = " + str(user_id) + " ORDER BY " + table_id + " DESC;"
    )
    data = make_query(query)
    return data

@app.route('/completed/<user_id>')
def get_completed(user_id):
    data = get_workout_list(user_id, "completed", "completed_id")
    return json.dumps(data)

@app.route('/favorites/<user_id>')
def get_favorites(user_id):
    data = get_workout_list(user_id, "favorites", "favorite_id")
    return json.dumps(data)

@app.route('/todo/<user_id>')
def get_todo(user_id):
    data = get_workout_list(user_id, "todo", "todo_id")
    return json.dumps(data)

@app.route('/user/<user_id>')
def get_user(user_id):
    query = (
        "SELECT username, birthdate, gender FROM users WHERE user_id = " + str(user_id) + ";"
    )
    data = make_query(query)
    for i in data:
        i['birthdate'] = i['birthdate'].strftime('%m/%d/%Y')

    return json.dumps(data)

@app.route('/workout/<workout_id>')
def get_workout(workout_id):
    query = (
        "SELECT * FROM workouts WHERE workout_id = " + str(workout_id) + ";"
    )
    data = make_query(query)
    data[0]['rating'] = get_workout_rating(workout_id)
    return json.dumps(data)

@app.route('/allworkouts')
def get_all_workouts():
    query = (
        "SELECT * FROM workouts ORDER BY workout_id DESC;"
    )
    data = make_query(query)
    for workout in data:
        workout['rating'] = get_workout_rating(workout['workout_id'])
    return json.dumps(data)

def get_workout_rating(workout_id):
    query = (
        "SELECT AVG(wr.rating) AS rating FROM workout_ratings wr "
        "JOIN workouts w ON wr.workout_id = w.workout_id "
        "WHERE wr.workout_id = " + str(workout_id) +";"
    )
    data = make_query(query)
    return str(data[0]['rating'])

@app.route('/forum')
def get_forum():
    query = (
        "SELECT thread_id, name, datetime FROM threads ORDER BY DATETIME DESC;"
    )
    data = make_query(query)
    for i in data:
        i['datetime'] = i['datetime'].strftime('%m/%d/%Y')
        i['rating'] = get_thread_rating(i['thread_id'])

    return json.dumps(data)

@app.route('/thread/<thread_id>')
def get_thread(thread_id):
    query = (
        "SELECT u.username AS 'username', t.name as 'thread_name', t.datetime, t.content FROM threads t "
        "JOIN users u ON t.user_id = u.user_id "
        "WHERE t.thread_id = " + thread_id + ";"
    )
    thread_info = make_query(query)
    for i in thread_info:
        i['datetime'] = i['datetime'].strftime('%m/%d/%Y')

    comments = get_thread_comments(thread_id)
    pictures = get_pictures(thread_id)
    videos = get_pictures(thread_id)
    rating = get_thread_rating(thread_id)
    data = [{"thread": thread_info, "comments": comments, "pictures": pictures, "videos": videos, "rating": rating}]

    return json.dumps(data)

def get_thread_comments(thread_id):
    query = (
        "SELECT u.username AS 'username', c.datetime, c.content FROM comments c "
        "JOIN users u ON c.user_id = u.user_id "
        "JOIN threads t ON c.thread_id = t.thread_id "
        "WHERE t.thread_id = " + thread_id + ";"
    )
    data = make_query(query)
    for i in data:
        i['datetime'] = i['datetime'].strftime('%m/%d/%Y')

    return data

def get_pictures(thread_id):
    query = (
        "SELECT link FROM pictures WHERE thread_id = " + thread_id + ";"
    )
    data = make_query(query)
    return data

def get_videos(thread_id):
    query = (
        "SELECT link FROM videos WHERE thread_id = " + thread_id + ";"
    )
    data = make_query(query)
    return data

def get_thread_rating(thread_id):
    query = (
        "SELECT AVG(tr.rating) AS rating FROM thread_ratings tr "
        "JOIN threads t ON tr.thread_id = t.thread_id "
        "WHERE tr.thread_id = " + str(thread_id) + ";"
    )
    data = make_query(query)
    return str(data[0]['rating'])

if __name__ == '__main__':
    app.run(debug=True)

