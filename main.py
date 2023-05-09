from flask import Flask
from database import Database
import json

app = Flask(__name__)

db = Database("db.sqlite3")
data = db.read_data()

@app.route('/api/users', methods=["GET"])
def get_api_users():
    response = []
    for row in data:
        user = {
            'id': row[0],
            'username': row[1],
            'email': row[2],
            'register_date': row[4]
        }
        response.append(user)
    return json.dumps(response, indent=4, sort_keys=False), {'Content-Type': 'application/json; charset=utf-8', 'Access-Control-Allow-Origin': '*'}
#Сортировку по ключевому порядку я сделал с помощью chatgpt. Тот класс с dictionary не работало
#И еще из за этого порядок даты изменилось. В самой базе данных правильный формат



app.run(debug=True)