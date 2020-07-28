from flask import Flask
from flask import request
import mysql.connector as mariadb
import json

app = Flask(__name__)

@app.route('/')
def get_homepage():
    return 'HOME PAGE'

# User API endpoint
#     /user/          returns all user ids with no extra data
#     /user/<user_id> returns data for a specific user
@app.route('/user/')
def get_user():
    user_id = request.args.get('id')
    
    if not user_id:
        query = (
            "SELECT users.user_id FROM users" 
        )
        
        cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
        cursor = cnx.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cnx.close()
        
        results = {'user_ids': []}
        
        for row in rows:
            results['user_ids'].append(row[0])
        
        return results
    
    query = (
        "SELECT users.user_id, users.birthdate, users.gender, users.username, thread_ratings.thread_rating_id, " "thread_ratings.thread_id, thread_ratings.rating, comments.comment_id, comments.thread_id, comments.content "
        "FROM users "
        "JOIN thread_ratings ON thread_ratings.user_id = users.user_id "
        "JOIN comments ON comments.user_id = users.user_id "
        "WHERE users.user_id = %s"
    )
    
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    cursor = cnx.cursor()
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    cnx.close()
    
    selected_fields = [
        # user
        'user_id',
        'birthdate',
        'gender',
        'username',
        # thread_ratings
        'thread_rating_id',
        'thread_id',
        'rating',
        # comments
        'comment_id',
        'thread_id',
        'content'
    ]
    
    results = {}
    
    for row in rows:
        row_dict = dict(zip(selected_fields, row))
        row_dict['birthdate'] = row_dict['birthdate'].strftime('%m/%d/%Y')
        
        if row_dict['user_id'] not in results:
            user = {
                'user_id': row_dict['user_id'],
                'birthdate': row_dict['birthdate'],
                'gender': row_dict['gender'],
                'username': row_dict['username'],
                'comments': {row_dict['comment_id']: row_dict['content']},
                'thread_ratings': {row_dict['thread_id']: row_dict['rating']}
            }    
            results[row_dict['user_id']] = user
        else:
            if row_dict['comment_id'] not in results[row_dict['user_id']]['comments']:
                results[row_dict['user_id']]['comments'][row_dict['comment_id']] = row_dict['content']
            
            if row_dict['thread_id'] not in results[row_dict['user_id']]['thread_ratings']:
                results[row_dict['user_id']]['thread_ratings'][row_dict['thread_id']] = row_dict['rating']
    
    return results

# Thread API endpoint
#     /thread/            returns all thread ids with no extra data
#     /thread/<thread_id> returns data for a specific thread
@app.route('/thread/')
def get_thread():
    thread_id = request.args.get('id')
    
    if not thread_id:
        query = (
            "SELECT threads.thread_id FROM threads" 
        )
        
        cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
        cursor = cnx.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cnx.close()
        
        results = {'thread_ids': []}
        
        for row in rows:
            results['thread_ids'].append(row[0])
        
        return results
    
    query = (
        "SELECT threads.thread_id, threads.name AS thread_name, threads.content AS thread_content, " "thread_ratings.thread_rating_id, thread_ratings.rating, comments.comment_id, "
        "comments.content AS comment_content, videos.video_id, videos.name AS video_name, videos.link AS video_link, " "pictures.picture_id, pictures.name AS picture_name, pictures.link AS picture_link "
        "FROM threads "
        "JOIN thread_ratings ON thread_ratings.thread_id = threads.thread_id "
        "JOIN comments ON comments.thread_id = threads.thread_id "
        "JOIN videos ON videos.thread_id = threads.thread_id "
        "JOIN pictures ON pictures.thread_id = threads.thread_id "
        "WHERE threads.thread_id = %s"
    )
    
    cnx = mariadb.connect(user='vagrant', password='password', database='cobras')
    cursor = cnx.cursor()
    cursor.execute(query, (thread_id,))
    rows = cursor.fetchall()
    cnx.close()
    
    selected_fields = [
        # threads
        'thread_id',
        'thread_name',
        'thread_content',
        # thread_ratings
        'thread_rating_id',
        'rating',
        # comments
        'comment_id',
        'comment_content',
        # videos
        'video_id',
        'video_name',
        'video_link',
        # pictures
        'picture_id',
        'picture_name',
        'picture_link',
    ]
    
    results = {}
    
    for row in rows:
        row_dict = dict(zip(selected_fields, row))
        
        if row_dict['thread_id'] not in results:
            thread = {
                'thread_id': row_dict['thread_id'],
                'thread_name': row_dict['thread_name'],
                'thread_content': row_dict['thread_content'],
                'comments': {row_dict['comment_id']: row_dict['comment_content']},
                'thread_ratings': {row_dict['thread_rating_id']: row_dict['rating']},
                'videos': {row_dict['video_id']: {'name': row_dict['video_name'], 'link': row_dict['video_link']}},
                'pictures': {row_dict['picture_id']: {'name': row_dict['picture_name'], 'link': row_dict['picture_link']}}
            }    
            results[row_dict['thread_id']] = thread
        else:
            if row_dict['comment_id'] not in results[row_dict['thread_id']]['comments']:
                results[row_dict['thread_id']]['comments'][row_dict['comment_id']] = row_dict['comment_content']
            
            if row_dict['thread_rating_id'] not in results[row_dict['thread_id']]['thread_ratings']:
                results[row_dict['thread_id']]['thread_ratings'][row_dict['thread_rating_id']] = row_dict['rating']
            
            if row_dict['video_id'] not in results[row_dict['thread_id']]['videos']:
                results[row_dict['thread_id']]['videos'][row_dict['video_id']] = {
                    'name': row_dict['video_name'],
                    'link': row_dict['video_link']
                }
            
            if row_dict['picture_id'] not in results[row_dict['thread_id']]['pictures']:
                results[row_dict['thread_id']]['pictures'][row_dict['picture_id']] = {
                    'name': row_dict['picture_name'],
                    'link': row_dict['picture_link']
                }
    
    return results
