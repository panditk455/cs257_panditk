# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
import psycopg2

# This function tests to make sure that you can connect to the database
def test_connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    dropsql = """ DROP TABLE IF EXISTS cities;  DROP TABLE IF EXISTS stateabb; """



    citiessql = """
    CREATE TABLE cities 
    (city VARCHAR(100), state VARCHAR(50), population INT,
    lat DOUBLE PRECISION,lon DOUBLE PRECISION);
    """

    stateabbsql = """ 
    CREATE TABLE stateabb 
    ( state VARCHAR(50), abbreviation VARCHAR(5));
    """

    cur = conn.cursor()

    cur.execute(dropsql)
    cur.execute(  citiessql   )
    cur.execute(  stateabbsql   )

    conn.commit()

    return None

test_connection()