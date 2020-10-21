import pymysql
from class_person import Person

#Connects to main database to obtain people and drinks tables
def connect():
    global connection
    connection = pymysql.connect(
        host =	"localhost",
        port = 3306,
        user = "root",
        password = "ttii2.jI",
        db = "brew",
    )