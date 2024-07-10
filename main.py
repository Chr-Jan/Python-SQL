import pypyodbc as odbc # pip install pypyodbc

DRIVER_NAME = "ODBC Driver 17 for SQL Server"
SERVER_NAME = "Your SQL server name"
DATABASE_NAME = "your database name"

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;
"""

try:
    print("Attempting to connect to the database...")
    conn = odbc.connect(connection_string)
    print("Connection Successful!")
    # Optional: Perform a simple query to test the connection
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION;")
    row = cursor.fetchone()
    print("SQL Server Version:", row)
    cursor.close()
    conn.close()
except odbc.Error as e:
    print("Error in Connection:", e)
