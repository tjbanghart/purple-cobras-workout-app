-- create tables
CREATE TABLE workouts (
    workout_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    beg_reps INT NOT NULL,
    mod_reps INT NOT NULL,
    adv_reps INT NOT NULL,
    beg_wt INT NOT NULL,
    mod_wt INT NOT NULL,
    adv_wt INT NOT NULL,
    sets INT NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY (workout_id)
);
CREATE TABLE users (
    user_id INT NOT NULL AUTO_INCREMENT,
    birthdate DATETIME NOT NULL,
    gender VARCHAR(50) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY (user_id)
);
CREATE TABLE favorites (
    favorite_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    workout_id INT NOT NULL,
    PRIMARY KEY (favorite_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE,
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id)
        ON DELETE CASCADE,
    CONSTRAINT favorited UNIQUE (user_id, workout_id)
);
CREATE TABLE todo (
    todo_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    workout_id INT NOT NULL,
    PRIMARY KEY (todo_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE,
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id)
        ON DELETE CASCADE,
    CONSTRAINT todo_item UNIQUE (user_id, workout_id)
);
CREATE TABLE completed (
    completed_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    workout_id INT NOT NULL,
    PRIMARY KEY (completed_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE,
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id)
        ON DELETE CASCADE,
    CONSTRAINT completed_wkout UNIQUE (user_id, workout_id)
);
CREATE TABLE workout_ratings (
    workout_rating_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    workout_id INT NOT NULL,
    rating INT NOT NULL,
    PRIMARY KEY (workout_rating_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE,
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id)
        ON DELETE CASCADE,
    CONSTRAINT w_rated UNIQUE (user_id, workout_id)
);
CREATE TABLE threads (
    thread_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    datetime DATETIME NOT NULL,
    content TEXT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE,
    PRIMARY KEY (thread_id)
);
CREATE TABLE thread_ratings (
    thread_rating_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    thread_id INT NOT NULL,
    rating INT NOT NULL,
    PRIMARY KEY (thread_rating_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE,
    FOREIGN KEY (thread_id) REFERENCES threads(thread_id)
        ON DELETE CASCADE,
    CONSTRAINT t_rated UNIQUE (user_id, thread_id)
);
CREATE TABLE comments (
    comment_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    thread_id INT NOT NULL,
    datetime DATETIME NOT NULL,
    content TEXT NOT NULL,
    PRIMARY KEY (comment_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE,
    FOREIGN KEY (thread_id) REFERENCES threads(thread_id)
        ON DELETE CASCADE
);
CREATE TABLE videos (
    video_id INT NOT NULL AUTO_INCREMENT,
    thread_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    link VARCHAR(50) NOT NULL,
    PRIMARY KEY (video_id),
    FOREIGN KEY (thread_id) REFERENCES threads(thread_id)
        ON DELETE CASCADE
);
CREATE TABLE pictures (
    picture_id INT NOT NULL AUTO_INCREMENT,
    thread_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    link VARCHAR(50) NOT NULL,
    PRIMARY KEY (picture_id),
    FOREIGN KEY (thread_id) REFERENCES threads(thread_id)
        ON DELETE CASCADE
);



INSERT INTO workouts
    (
        name,
        beg_reps,
        mod_reps,
        adv_reps,
        beg_wt,
        mod_wt,
        adv_wt,
        sets,
        description
    )
VALUES
    ('Workout1', 5, 8, 12, 5, 10, 15, 3, 'Workout1 description.'),
    ('Workout2', 5, 8, 12, 5, 10, 15, 3, 'Workout2 description.');
INSERT INTO users
    (birthdate, gender, username)
VALUES
    ('1969-07-20', 'male', 'User1'),
    ('1975-03-19', 'female', 'User2');
INSERT INTO favorites
    (user_id, workout_id)
VALUES
    (1, 1),
    (2, 2);
INSERT INTO completed
    (user_id, workout_id)
VALUES
    (1, 1),
    (2, 2);
INSERT INTO workout_ratings
    (user_id, workout_id, rating)
VALUES
    (1, 1, 4),
    (2, 2, 7);
INSERT INTO threads
    (name, datetime, content, user_id)
VALUES
    ('Thread1', '2020-02-20 20:20:20', 'Thread 1 content.', 1),
    ('Thread2', '2020-02-20 20:20:20', 'Thread 2 content.', 2);
INSERT INTO thread_ratings
    (user_id, thread_id, rating)
VALUES
    (1, 1, 6),
    (2, 1, 7),
    (2, 2, 3);
INSERT INTO comments
    (user_id, thread_id, datetime, content)
VALUES
    (1, 1, '2020-02-20 20:20:20', 'Comment 1.'),
    (1, 1, '2020-02-20 20:20:20', 'Comment 2.'),
    (1, 2, '2020-02-20 20:20:20', 'Comment 3.'),
    (2, 2, '2020-02-20 20:20:20', 'Comment 4.');
INSERT INTO videos
    (thread_id, name, link)
VALUES
    (1, 'Video1', '/link1/'),
    (1, 'Video2', '/link2/'),
    (2, 'Video3', '/link3/'),
    (2, 'Video4', '/link4/');
INSERT INTO pictures
    (thread_id, name, link)
VALUES
    (1, 'Picture1', '/link1/'),
    (1, 'Picture2', '/link2/'),
    (2, 'Picture3', '/link3/'),
    (2, 'Picture4', '/link4/');
