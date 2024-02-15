import flask
import psycopg2

app = flask.Flask(__name__)

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