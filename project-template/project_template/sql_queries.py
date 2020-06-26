# DROP TABLES

songplay_table_drop = "DROP TABLE song_table_create"
user_table_drop = "DROP TABLE user_table_create"
song_table_drop = "DROP TABLE song_table_create"
artist_table_drop = "DROP TABLE artist_table_create"
time_table_drop = "DROP TABLE time_table_create"

# CREATE TABLES
#songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
songplay_table_create = ("""CREATE TABLE IF NOT EXISCTS songplay (songplay_id varchar, 
                                                                  start_time numirec, 
																  user_id varchar, 
																  level varchar, 
																  song_id varchar, 
																  artist_id varchar, 
																  session_id varchar, 
																  location varchar, 
																  user_agent varchar) 
""")


#user_id, first_name, last_name, gender, level
user_table_create = (""" CREATE TABLE IF NOT EXISCTS user (user_id varchar, first_name varchar,
                                                           last_name varchar, gender varchar,
														   level varchar)
""")


#song_id, title, artist_id, year, duration
song_table_create = (""" CREATE TABLE IF NOT EXISCTS song (song_id varchar , title varchar, artist_id varchar, year varchar, duration numirec)
""")


#artist_id, name, location, latitude, longitude
artist_table_create = ("""CREATE TABLE IF NOT EXISCTS artist (artist_id varchar, name varchar, location varchar,
                                                              latitude varchar, longitude varchar)
""")



#start_time, hour, day, week, month, year, weekday
time_table_create = (""" CREATE TABLE IF NOT EXISCTS artist (start_time numirec, hour varchar, day varchar,
                                                              week varchar, month varchar
															  year varchar, weekday varchar )
""")

# INSERT RECORDS

songplay_table_insert = (" INSERT INTO songplay_table_create(songplay_id, start_time, user_id, level, song_id, \
															 artist_id, session_id, location, user_agent )\
					       values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
						   ('songplay',1,'user','two','song','Artist', 'session','Riyadh','useragent'))

user_table_insert = ("INSERT INTO user_table_create (user_id, first_name,last_name, gender,level )\
					  values(%s,%s,%s,%s,%s)",
					  ('user','wejdan','alzahrani','femile','tow'))

song_table_insert = ("""INSERT INTO song_table_create (song_id, title, artist_id, year, duration)\
					  values(%s,%s,%s,%s,%s),
					  ('song','love','artist','1996',5.20)
""")

artist_table_insert = ("""INSERT INTO artist_table_create (artist_id, name, location, latitude, longitude)\
					  values(%s,%s,%s,%s,%s),
					  ('artist','Ahmed','Riyadh','12345','54321')
""")


time_table_insert = ("""INSERT INTO artist_table_create (start_time numirec, hour numirec, day int,
                                                              week int, month varchar
															  year int, weekday varchar)\
					  values(%s,%s,%s,%s,%s,%s,%s),
					  (1,'2:30','8','one','aprel','1996','sunday')
""")

# FIND SONGS

song_select = (""" select * from song_table_create
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]