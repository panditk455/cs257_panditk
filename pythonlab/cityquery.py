# Author: Kritika Pandit
# Edited on: Jan 29, 2024

# These are different queries which does specifc function as given:

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

# This Determine if Northfield is present in the database. 
# If it is, print its location (Latitude and Longitude).
#  If it is not, print an appropriate message for the user.
def test_query_one():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow"
        )

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

    cur.close()
    conn.close()
    
test_query_one()

# This function will help to print out the name of the city with the largest population.
def test_query_two():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")
        
    cur = conn.cursor()
    
    secondsql = """
    SELECT City
    FROM cities 
    ORDER BY population DESC
    LIMIT 1"""
    
    cur.execute( secondsql )


    # fetchone Just retuns one row:
    row = cur.fetchone()

    if row:
        print(f"The city with lagest population:{row[0]} ")
    else:
        print(f"Opps! Something went wrong")

    cur.close()
    conn.close()
    

test_query_two()



# # This function will help to print out the name of the city with the largest population.
def test_query_three():
    
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="panditk",
    user="panditk",
    password="square555cow"
    )

    cur = conn.cursor()

    thirdsql = """
    SELECT City
    FROM cities
    WHERE state = 'Minnesota' 
    ORDER BY population 
    LIMIT 1"""
    
    cur.execute( thirdsql )
    
    # fetchone Just retuns one row:
    row = cur.fetchone()

    if row:
        print(f"The city with smallest population in Minnesota is: {row[0]} ")
    else:
        print(f"No city in Minnesota with the smallest population")

    cur.close()
    conn.close()

test_query_three()


# # This function will help to print out the name of the city with the largest population.
def test_query_four():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()
    

    # For the state in the farthest east:
    eastsql = """
    SELECT city
    FROM cities
    ORDER BY lon DESC
    LIMIT 1
    """
    
    cur.execute( eastsql )
    eastestcity = cur.fetchone()[0] if cur.rowcount > 0 else "No cities were found."

    # For the city in the farthest west:
    westsql = """
    SELECT city
    FROM cities
    ORDER BY lon ASC
    LIMIT 1
    """
    
    cur.execute( westsql )
    westestcity = cur.fetchone()[0] if cur.rowcount > 0 else "No cities were found."

    # For the one in the farthest north:
    northsql = """
    SELECT city
    FROM cities
    ORDER BY lat DESC
    LIMIT 1;
    """

    cur.execute( northsql )
    northestcity = cur.fetchone()[0] if cur.rowcount > 0 else "No cities were found."


    # For the one in the farthest south:
    southsql = """
    SELECT city
    FROM cities
    ORDER BY lat ASC
    LIMIT 1;
    """

    cur.execute( southsql )
    southestcity = cur.fetchone()[0] if cur.rowcount > 0 else "No cities were found."
    
    print (f"Furthest North: {northestcity}")
    print (f"Furthest East: {eastestcity}")
    print (f"Furthest West: {westestcity}")
    print (f"Furthest South: {southestcity}")
    

    cur.close()
    conn.close()

test_query_four()


# Have the user enter a State from the keyboard.
#  Print the Total population of all the cities in that state.
#   The user should be able to enter either an abbreviation or the full name of the sate. 
#   If the user enters an abbreviation, then you should look up the abbreviation in
#    the second table to learn the full name of the state.

def test_query_five():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="panditk",
        user="panditk",
        password="square555cow")

    cur = conn.cursor()

    input_state = input("Enter a State name, you can enter an Abbreviation or full name:")

    abbsql = """
    SELECT state
    FROM stateabb
    WHERE abbreviation = %s
    """

    cur.execute(abbsql, (input_state,))

    state_name = cur.fetchone()

    if not state_name:
        state_name = (input_state,)

    population_sql = """
    SELECT SUM(population)
    FROM cities 
    WHERE state = %s
    """

    cur.execute(population_sql, state_name)  # Passing state_name as a tuple

    total_population = cur.fetchone()[0] or 0

    print(f"The total population of {input_state}, including all cities is: {total_population}")

    cur.close()
    conn.close()

test_query_five()
