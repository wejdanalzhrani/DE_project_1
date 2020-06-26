# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"


# CREATE TABLES
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay (songplay_id SERIAL, 
                                                                  start_time timestamp, 
                                                                  user_id varchar, 
                                                                  level varchar, 
                                                                  song_id varchar , 
                                                                  artist_id varchar, 
                                                                  session_id BIGINT, 
                                                                  location varchar, 
                                                                  user_agent TEXT,
                                                                  PRIMARY KEY(songplay_id));""")


user_table_create = (""" CREATE TABLE IF NOT EXISTS users (user_id varchar NOT NULL,
                                                           first_name varchar,
                                                           last_name varchar, 
                                                           gender varchar,
                                                           level varchar,
                                                           PRIMARY KEY(user_id));""")#



song_table_create = (""" CREATE TABLE IF NOT EXISTS song (song_id varchar NOT NULL ,
                                                          title varchar,
                                                          artist_id varchar,
                                                          year int,                                                                                                                       duration numeric,
                                                          PRIMARY KEY(song_id)) """)#



artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist (artist_id varchar NOT NULL,
                                                             name varchar,
                                                             location varchar,
                                                             latitude varchar, 
                                                             longitude varchar,
                                                             PRIMARY KEY(artist_id))""")#




time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time timestamp NOT NULL,
                                                            hour int,
                                                            day int,
                                                            week int,
                                                            month int,
                                                            year int,
                                                            weekday float,
                                                            PRIMARY KEY(start_time))""")#


#create FK for tables
create_songplay_time_fk=( """
                alter table songplay add foreign key (start_time) REFERENCES time(start_time);
                """)

create_songplay_user_fk=("""
                alter table songplay add foreign key (user_id) REFERENCES users(user_id);
                """)
create_songplay_song_fk=("""
                alter table songplay add foreign key (song_id) REFERENCES song(song_id);
                """)
create_songplay_artist_fk=("""
                    alter table songplay add foreign key (artist_id) REFERENCES artist(artist_id);
                    """)


# INSERT RECORDS

songplay_table_insert = (" INSERT INTO songplay(start_time, user_id, level, song_id, \
                                                 artist_id, session_id, location, user_agent )\
                         values(%s,%s,%s,%s,%s,%s,%s,%s)")

user_table_insert = ("""INSERT INTO users (user_id, first_name,last_name, gender,level )
                      values(%s,%s,%s,%s,%s)
                      ON CONFLICT (user_id)
                      DO UPDATE
                      SET level = EXCLUDED.level ;""")

song_table_insert = ("""INSERT INTO song(song_id, title, artist_id, year, duration)\
                      values(%s,%s,%s,%s,%s)
                      ON CONFLICT (song_id)
                      DO NOTHING ;""")

artist_table_insert = ("""INSERT INTO artist (artist_id, name, location, latitude, longitude)\
                        values(%s,%s,%s,%s,%s)
                        ON CONFLICT (artist_id)
                        DO NOTHING ;""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month,\
                                        year , weekday)\
                      values(%s,%s,%s,%s,%s,%s,%s)
                      ON CONFLICT (start_time)
                      DO NOTHING ;""")


# FIND SONGS
# Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.
song_select = ("""select song_id,song.artist_id from song
                  JOIN artist ON song.artist_id = artist.artist_id
                  WHERE song.title=%s AND artist.name=%s AND song.duration= %s
                  """)

#where title='City Slickers' and name='Marc Shaiman' and duration = 149.86404

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop,user_table_drop,song_table_drop, artist_table_drop, time_table_drop]
create_fk_queries= [create_songplay_time_fk,create_songplay_user_fk,create_songplay_song_fk,
                    create_songplay_artist_fk]