import random

import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

names = ["Kritika", "Will", "Kripa", "Navin", "Heidi", "Daniel", "Jeebika", "Darshan"]
adjectives = ["nice", "awesome", "good", "kind", "horrible", "honest", "punctual"]
years = list(range(1992, 2024))

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/randsentence')
def randsentence():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")
    
    cur = conn.cursor()
    
    my_sql = """
    SELECT city
    FROM cities
    ORDER BY random()
    LIMIT 1"""

    cur.execute(my_sql)
    city = cur.fetchone()[0]  
    cur.close()
    
    name = random.choice(names)
    adjective = random.choice(adjectives)
    year = random.choice(years)

    required_sentence = "{name} the {adjective} was born in {city} in {year}" 

    return render_template('index.html', required_sentence=required_sentence)  

@app.route('/rand/<low>/<high>') 

@app.route('/rand/')
def rand(low=None, high=None):
    if low and high:
        low_int = int(low)
        high_int = int(high)
        num = random.randint(low_int, high_int)
    else:
        num = random.randint(0, 100) 

    return render_template("random.html", randNum=num)

if __name__ == '__main__':
    my_port = 5131
    app.run(host='0.0.0.0', port=my_port)
