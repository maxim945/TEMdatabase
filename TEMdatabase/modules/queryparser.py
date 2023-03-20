import sqlite3
import pandas as pd

def query_database(query, database):
    # Connect to the database file
    conn = sqlite3.connect(database)

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Get the column names from the cursor description
    columns = [description[0] for description in cursor.description]

    # Create a dataframe from the rows and columns
    df = pd.DataFrame(rows, columns=columns)

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return df
