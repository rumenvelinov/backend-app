import time
from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)

mysql = MySQL()
# load the config from env vars
app.config.from_prefixed_env()
mysql.init_app(app)

time.sleep(100)
# connect to mysql
conn = mysql.connect()
cursor = conn.cursor()


@app.route("/")
def home():
    cursor.execute("select LastName from User where PersonID = 1")
    data = cursor.fetchone()
    return f"Hallo, {data[0]}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)