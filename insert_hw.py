import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://postgres:09111957@localhost:5432/netology_db')
connection = engine.connect()

artists = ["Amy Winehouse", "Lady Gaga", "Beyoncé", "Taylor Swift",
           "David Bowie", "LORDE", "Adele", "U2", "Arctic Monkeys"]
i = 0
for artist in artists:
    connection.execute(f"""INSERT INTO artist(name)
                          VALUES('{artists[i]}');""")
    i += 1

albums = {'Back to Black': 2006,
          'Fame': 2008 ,
          'Everything Is Love': 2018,
          'Red': 2012,
          'Tonight': 1984,
          'Melodrama': 2017,
          '30': 2021,
          'The Joshua Tree': 1987,
          'Tranquility Base Hotel & Casino': 2018}
for album in albums:
    connection.execute(f"""INSERT INTO album(title, release_year)
                          VALUES('{album}', {albums.get(album)});""")


artist_album = {'Amy Winehouse': 'Back to Black',
                'Lady Gaga': 'Fame',
                'Beyoncé': 'Everything Is Love',
                'Taylor Swift': 'Red',
                'David Bowie': 'Tonight',
                'LORDE': 'Melodrama',
                'Adele': '30',
                'U2': 'The Joshua Tree',
                'Arctic Monkeys': 'Tranquility Base Hotel & Casino'}
for art_alb in artist_album:
    artist_id = connection.execute(f"""SELECT id FROM artist
                                      WHERE name = '{art_alb}';""").fetchone()
    album_id = connection.execute(f"""SELECT id FROM album
                                          WHERE title = '{artist_album.get(art_alb)}';""").fetchone()
    connection.execute(f"""INSERT INTO artistalbum (artist_id, album_id)
                           VALUES({artist_id[0]}, {album_id[0]});""")


genres = ["rock", "pop", "blues", "indie", "hip-hop", "classical", "R&B"]
i = 0
for genre in genres:
    connection.execute(f"""INSERT INTO genre(title)
                          VALUES('{genres[i]}');""")
    i += 1

tracks = {"Rehab": ["Back to Black", 200], "Love Is a Losing Game": ["Back to Black", 154],
          "Poker Face": ["Fame", 200], "Paparazzi": ["Fame", 196],
          "Summer": ["Everything Is Love", 267], "Friends": ["Everything Is Love", 326],
          "Red": ["Red", 206], "State of grace": ["Red", 273],
          "Loving the alien": ["Tonight", 427], "When I Live My Dream": ["Tonight", 180],
          "Green light": ["Melodrama", 212], "Writer in the dark": ["Melodrama", 217],
          "My Propeller": ["Tranquility Base Hotel & Casino", 195],
          "Where the Streets Have No Name": ["The Joshua Tree", 261], "With or Without You": ["The Joshua Tree", 295]}
for track in tracks:
    album_id = connection.execute(f"""SELECT id FROM album
                                      WHERE title = '{tracks.get(track)[0]}';""").fetchone()
    connection.execute(f"""INSERT INTO track (title, track_length, album_id)
                           VALUES('{track}', {tracks.get(track)[1]}, {album_id[0]});""")


genre_artist = {"rock": ["David Bowie", "U2", "Arctic Monkeys"],
                "pop": ["Lady Gaga", "Beyoncé", "Taylor Swift"],
                "blues": ["Amy Winehouse"],
                "indie": ["LORDE"],
                "hip-hop": ["Beyoncé"],
                "classical": [],
                "R&B": ["Beyoncé"]}
for genre in genre_artist:
    genre_id = connection.execute(f"""SELECT id FROM genre
                                      WHERE title = '{genre}';""").fetchone()
    for artist in genre_artist.get(genre):
        artist_id = connection.execute(f"""SELECT id FROM artist
                                      WHERE name = '{artist}';""").fetchone()
        connection.execute(f"""INSERT INTO genreartist (genre_id, artist_id)
                           VALUES({genre_id[0]}, {artist_id[0]});""")

collections = {'Collection 1': 2015,
               'Collection 2': 2016,
               'Collection 3': 2017,
               'Collection 4': 2018,
               'Collection 5': 2019,
               'Collection 6': 2020,
               'Collection 7': 2021,
               'Collection 8': 2022}
for collection in collections:
    connection.execute(f"""INSERT INTO collection (title, release_year)
                          VALUES('{collection}', {collections.get(collection)});""")

collection_track = {'Collection 1': ["Loving the alien", "My Propeller"],
                    'Collection 2': ["Rehab", "Friends", "Summer"],
                    'Collection 3': ["Poker Face", "Red"],
                    'Collection 4': ["Writer in the dark", "State of grace"],
                    'Collection 5': ["With or Without You", "Love Is a Losing Game"],
                    'Collection 6': ["When I Live My Dream"],
                    'Collection 7': ["Paparazzi", "Summer"],
                    'Collection 8': ["Writer in the dark", "Green light", "Love Is a Losing Game"]}
for collection in collection_track:
    collection_id = connection.execute(f"""SELECT id FROM collection
                                      WHERE title = '{collection}';""").fetchone()
    for track in collection_track.get(collection):
        track_id = connection.execute(f"""SELECT id FROM track
                                      WHERE title = '{track}';""").fetchone()
        connection.execute(f"""INSERT INTO collectiontrack (collection_id, track_id)
                           VALUES({collection_id[0]}, {track_id[0]});""")
