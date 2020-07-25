Instructions for setting up the database and running the flask app on Windows 10.

* Install Vagrant
* Run `vagrant init hashicorp/bionic64`
* In the Vagrantfile, un-comment out the line `config.vm.network "private_network", ip: "192.168.33.10"`
* Run `vagrant up`
* Run `vagrant ssh`
* Run `sudo apt-get update`
* Run `sudo apt-get install -y python3-pip`
* Run `sudo apt install -y mariadb-server`
* Run `sudo apt-get install -y python3-venv`
* Run `git clone https://github.com/tjbanghart/purple-cobras-workout-app.git`
* Run `cd purple-cobras-workout-app`
* Run `git checkout msg_board_endpoints`
* Run `cd flask_app`

Time to create and source the database.
* Run `sudo mysql -u root`, the default password is blank
* Within the mysql shell, run
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

* Run `python3 -m venv venv`
* Run `. venv/bin/activate`
* Run `pip install Flask`
* Run `pip3 install mysql-connector-python`

Then run app like this
* Run `export FLASK_APP=main.py`
* Run `flask run --host=0.0.0.0`

The web page is visible at http://192.168.33.10:5000/
