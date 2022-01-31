import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://postgres:09111957@localhost:5432/netology_db')
connection = engine.connect()

print(connection.execute("""SELECT title, release_year FROM album
                            WHERE release_year = 2018;""").fetchall())

print(connection.execute("""SELECT title, track_length FROM track
                            ORDER BY track_length DESC;""").fetchone())

print(connection.execute("""SELECT title FROM track
                            WHERE track_length >= 3.5 * 60;""").fetchall())

print(connection.execute("""SELECT title FROM collection
                            WHERE release_year BETWEEN 2018 and 2020;""").fetchall())

print(connection.execute("""SELECT name FROM artist
                            WHERE name NOT LIKE '%% %%';""").fetchall())

print(connection.execute("""SELECT title FROM track
                            WHERE title iLIKE '%%my%%';""").fetchall())




