import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    '''
    cur = data connection 
    filepath = path of song data 
    
    This function receive curser and file path from process_data function in order to process song data and 
    insert it into a tables (song, artist) 
    
    '''
    # open song file
    df = pd.read_json(filepath,lines=True)

    # insert song record
    song_data = df[['song_id','title','artist_id','year','duration']].values.tolist()
    cur.execute(song_table_insert, song_data[0])
    
    # insert artist record
    artist_data = df[['artist_id','artist_name','artist_longitude','artist_latitude','artist_location']].values.tolist()
    cur.execute(artist_table_insert, artist_data[0])


def process_log_file(cur, filepath):
    '''
    cur = data cursor 
    filepath = path of log data 
    
    This function receve curser and file path from process_data function in order to process log data:
    1-filter log file by (page=='NextSong')
    2-convert data into a right types(ex: convert timestamp column'df.ts' to datetime)
    after that insert data into a tables (time, user, song_play)
    
    '''
    # open log file
    df = pd.read_json(filepath,lines=True)

    # filter by NextSong action
    df = df[df.page=='NextSong']

    # convert timestamp column to datetime
    import datetime
    #t = datetime.datetime.fromtimestamp(df.ts / 1e3)
    t = pd.to_datetime(df.ts,unit='us')
    
    # insert time data records
    time_data=(t,t.dt.hour,t.dt.day,t.dt.week,t.dt.month,t.dt.year,t.dt.weekday)
    column_labels =(['start_time','hour','day','week','month','year','weekday'])
    time_df = pd.DataFrame(list(zip(*time_data)),columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName','lastName', 'gender','level']]
    
    # to remove dublicated 
    user_df=user_df.drop_duplicates()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)
     #cast length into str
    df['length']=df.length.astype(str)
     #cast ts into timestamp
    df['ts']=pd.to_datetime(df.ts,unit='ms')
    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts,
                     row.userId, 
                     row.level, 
                     songid, 
                     artistid,
                     row.sessionId,
                     row.location,
                     row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
    cur = data cursor
    conn = data connection
    filepath = path of data 
    func = function to processing the data
    
    This function get all files-path, data and, the total number of files found and 
    call the previous tow function in order to filter iterate over files and processes.

    '''
    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()