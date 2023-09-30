import psycopg2

# Connect to the "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ['Queen'])

# Query 4 - select only "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = 51')

# Query 5 - select only "ArtistId" #51 from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = 51')

# Query 6 - select all tracks where composer is "Queen" from "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['Queen'])

# Query 7 - select only "Cake" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ['Cake'])

# Query 8 - select only "ArtistId" #196 from the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = 196')

# Query 9 - select all tracks where composer is "Cake" from "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['Cake'])

# Query 10 - select all tracks where composer is "test" from "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['test'])

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the result (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

#print results
for result in results:
    print(result)
