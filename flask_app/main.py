from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

cnx = mysql.connector.connect(user='cs340_vangemed', password='password',
                                 host='classmysql.engr.oregonstate.edu',
                                 database='cs340_vangemed')
cursor = cnx.cursor()

@app.route('/completed')
def get_completed(user_id):
    query = (
        "SELECT w.name FROM workouts w " 
        "JOIN completed c ON w.workout_id = c.workout_id "
        "JOIN users u ON c.user_id = u.user_id "
        "WHERE u.user_id =" + str(user_id) + "ORDER BY completed_id DESC;"
    )
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data

@app.route('/favorites')
def get_favorites(user_id):
    query = (
        "SELECT w.name FROM workouts w " 
        "JOIN favorites f ON w.workout_id = f.workout_id "
        "JOIN users u ON f.user_id = u.user_id "
        "WHERE u.user_id = " + str(user_id) + " ORDER BY favorite_id DESC;;"
    )
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data

@app.route('/todo')
def get_todo(user_id):
    query = (
        "SELECT w.name FROM workouts w " 
        "JOIN todo td ON w.workout_id = td.workout_id "
        "JOIN users u ON td.user_id = u.user_id "
        "WHERE u.user_id = " + str(user_id) + " ORDER BY todo_id DESC;"
    )
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data

@app.route('/user')
def get_user(user_id):
    query = (
        "SELECT username, birthdate, gender FROM users WHERE user_id = " + str(user_id) + ";"
    )
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data

@app.route('/workout')
def get_workout(workout_id):
    query = (
        "SELECT * FROM workouts WHERE workout_id = " + str(workout_id) + ";"
    )
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data

@app.route('/allworkouts')
def get_all_workouts():
    query = (
        "SELECT * FROM workouts ORDER BY workout_id DESC;"
    )
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data

@app.route('/forum')
def get_forum():
    query = (
        "SELECT name, datetime FROM threads ORDER BY DATETIME DESC;"
    )
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data

@app.route('/thread')
def get_thread(thread_id):
    query = (
        "SELECT u.username AS 'username', t.name as 'thread_name', t.datetime, t.content FROM threads t "
        "JOIN users u ON t.user_id = u.user_id "
        "WHERE t.thread_id = " + thread_id+";"
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    cnx.close()

    comments = get_thread_comments(thread_id)
    pictures = get_pictures(thread_id)
    videos = get_pictures(thread_id)
    data = {"rows": rows, "comments": comments, "pictures": pictures, "videos": videos}
    
    return data

def get_thread_comments(thread_id):
    query = (
        "SELECT u.username AS 'username', c.datetime, c.content FROM comments c "
        "JOIN users u ON c.user_id = u.user_id "
        "JOIN threads t ON c.thread_id = t.thread_id "
        "WHERE t.thread_id = " + thread_id+";"
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    cnx.close()

    return rows

def get_pictures(thread_id):
    query = (
        "SELECT link FROM pictures WHERE thread_id = " + thread_id+";"
    )
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data

def get_videos(thread_id):
    query = (
        "SELECT link FROM videos WHERE thread_id = " + thread_id+";"
    )
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()

    return data


if __name__ == '__main__':
    app.run(debug=True)
