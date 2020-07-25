Instructions for setting up the database and running the flask app on Windows 10.

1. Install Vagrant
2. Run `vagrant init hashicorp/bionic64`
3. In the Vagrantfile, un-comment out the line `config.vm.network "private_network", ip: "192.168.33.10"`
4. Run `vagrant up`
5. Run `vagrant ssh`
6. Run `sudo apt-get update`
7. Run `sudo apt-get install -y python3-pip`
8. Run `sudo apt install -y mariadb-server`
9. Run `sudo apt-get install -y python3-venv`

10. Run `git clone https://github.com/tjbanghart/purple-cobras-workout-app.git`
11. Run `cd purple-cobras-workout-app`
12. Run `git checkout msg_board_endpoints`
13. Run `cd flask_app`

Time to create and source the database.
14. Run `sudo mysql -u root`, the default password is blank
15. Within the mysql shell, run
```
CREATE USER 'vagrant'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'vagrant'@'localhost' WITH GRANT OPTION;
CREATE USER 'vagrant'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'vagrant'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

CREATE DATABASE cobras;
USE cobras;
SOURCE cobrasdump.sql;
exit;
```

16. Run `python3 -m venv venv`
17. Run `. venv/bin/activate`
18. Run `pip install Flask`
19. Run `pip3 install mysql-connector-python`

Then run app like this
20. Run `export FLASK_APP=main.py`
21. Run `flask run --host=0.0.0.0`

The web page is visible at http://192.168.33.10:5000/
