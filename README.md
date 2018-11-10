# Log Analysis project

First project in Udacity Fullstack Nanodegree
It's a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

Answering the flowing question:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Installation

  - [Python](https://www.python.org/downloads/)
  - [Vagrant](https://www.vagrantup.com/downloads.html)
  - [Virtual Machine](https://www.virtualbox.org/wiki/Downloads)
  - [The Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## How to Run the project?
Once you get the above installed, run the flowing in the terminal:

you should downlad [FSND virtual machine](https://github.com/udacity/fullstack-nanodegree-vm). then,
```sh 
$ cd vagrant
```
to Launch Vagrant VM
```sh 
$ vagrant up
```

to login into the VM
```sh 
$ vagrant ssh
```

then,
```sh 
$ cd /vagrant
```
you should downlaod or clone the project inside the vagrant folder. then run
```sh 
$ cd log-analysis-project
```

 and finally to run the program and print the results of the three question, run
 ```sh 
$ python log-analyser.py
```

