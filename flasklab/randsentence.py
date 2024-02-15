import random

import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

names = ["Kritika", "Will", "Kripa", "Navin", "Heidi", "Daniel", "Jeebika", "Darshan"]
adjectives = ["nice", "awesome", "good", "kind", "horrible", "honest", "punctual"]
years = list(range(1992, 2024))

@app.route('/')
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

    required_sentence = f"{name} the {adjective} was born in {city} in {year}"

    return render_template('myindex.html', required_sentence=required_sentence)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5131)
