# Analyze-Log-Files
Log Analysis Project of the Udacity Full Stack Web Developer Nanodegree

# What is it?
This is the **Log Analysis Project** of the **Udacity Full Stack Web Developer Nanodegree**. 

It represents a simple internal reporting tool using information from a database of a newspaper website. 

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, the code answers questions about the site's user activity.

The program runs from the command line. It does not take any input from the user. Instead, it connects to the database, uses SQL queries to analyze the log data, and prints out the answers of what kind of articles the site's readers like.

# Prerequesites
- Python 3.6.0
- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)

# How to run it?
1. Install VirtualBox and Vagrant.
2. Download or clone the [Udacity Fullstack-Nanodegree-VM](https://github.com/udacity/fullstack-nanodegree-vm) repository
3. Download newsdata.sql and unzip it.

## Launching the Virtual Machine
1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command: 
`$ vagrant up`. 
2. Then Log into this using command: 
`$ vagrant ssh` 
3. Change directory to /vagrant:
`$ cd /vagrant`

## Setting up the Database
Load the data into the local database using the command:
`$ psql -d news -f newsdata.sql`

## Running the SQL Query from the python script:
`$ python3 log_project.py`


# What can I do with it?
After running the python code, the terminal prints the result of the sql-query (see also `output.txt`), e.g.:

- the most popular article authors of all time
- the most popular three articles of all time
- on which days more than 1 Percent of requests lead to errors

*Feel free to alter the python code in `log_project.py` for your own database queries.*
