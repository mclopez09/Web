from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'MySQLMoviesDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'   #'172.20.0.2' #'MySQLMoviesDB'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)