import flask
import psycopg2

app = flask.Flask(__name__)


@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Green">' + word1 + '</h1>'

# Adding two numbers:
@app.route('/add/<num1>/<num2>')
def my_sum(num1, num2):
    sum = int(num1) + int(num2)
    return str(sum)

# Abbreviation 
@app.route('/pop/<abbrev>')
def my_pop(abbrev):

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()
    
    abbsql = """
    SELECT state
    FROM stateabb
    WHERE abbreviation = %s
    """

    cur.execute(abbsql, (abbrev,))

    state_name = cur.fetchone()

    
    pop_sql = """SELECT SUM(population)
    FROM cities 
    WHERE state = %s
    """

    cur.execute(pop_sql, state_name) 

    total_population = cur.fetchone()[0] or 0

    return str(total_population)

    

if __name__ == '__main__':
    my_port = 5131
    app.run(host='0.0.0.0', port = my_port) 