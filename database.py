import pymysql
from class_person import Person

#Connecting to main database to obtain both tables
def connect():
    global connection
    connection = pymysql.connect(
        host =	"localhost",
        port = 3306,
        user = "root",
        password = "root_password",
        db = "brew",
    )