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

    return None

# This function sends an SQL query to the database
def test_query_one():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    firstsql = """
    SELECT City, lat, lon
    FROM cities
    WHERE City = 'Northfield';
    """   
    
    cur.execute( firstsql )

    
    row = cur.fetchone()

    if row:
        print(f"Northfield is present in the dataase, where Location: Latitude {row[1]}, Longitude {row[2]}")

    else:
        print(f"Sorry, Northfield is not present in the database")


    conn.commit()
    
test_query_one()

# def test_query_two():
#     conn = psycopg2.connect(
#     host="localhost",
#     port=5432,
#     database="panditk",
#     user="panditk",
#     password="square555cow")

#     cur = conn.cursor()

#     secondsql = 

#     cur.execute( secondsql )
