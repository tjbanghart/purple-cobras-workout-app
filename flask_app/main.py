from flask import Flask
import mysql.connector as mariadb
import json

app = Flask(__name__)

@app.route('/')
def get_workouts():
    cnx = mariadb.connect(user='vagrant', password='password')
    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM cobras.workouts')
    rows = cursor.fetchall()
    
    workout_fields = [
        'workout_id',
        'name',
        'beg_reps',
        'mod_reps',
        'adv_reps',
        'beg_wt',
        'mod_wt',
        'adv_wt',
        'sets',
        'description'
    ]
    
    results = {}
    
    for row in rows:
        row_dict = dict(zip(workout_fields, row))
        results[row_dict['workout_id']] = row_dict
    
    json_dump = json.dumps(results)
    
    cnx.close()
    
    return json_dump
