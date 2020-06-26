# Data Modeling with Postgres

---



### Introduction


- A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.


As Data Engineer at Sparkify I desinged a star schema model to facilitate the processes of queriying the data about the habits of the users of our music platform.

This provides an environment that is designed for:

* decision support 
* analytics reporting
* data mining 

When you isolate and optimize your data, you can manage it without impacting primary business processes.Being in the star schema model will enable us to get important measures: what songs users are listening to? for offering a better experience when it comes to listen to the music.

### Database schema design and ETL process:


* I modeled the database using the Star Schema Model by used python and postgres.We have got one Fact table, "songplays" along with four more Dimension tables named users", "songs", "artists" and "time".


* In the first part, I perform ETL on the first dataset, `song_data`, to create the `songs` and `artists` dimensional   tables and `log_data` and insert it into Tables


* In the seconed part, I perform ETL on the second dataset, `log_data`, to create the `time` and `users` dimensional tables, as well as the `songplays` fact table.


## (ER Diagram) showing how the fact and dimension tables are connected.

![schema](schema.png "schema")


####  Function For create tables:

```python

def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

```


### Files in repository

Description of files and how to use them in your own application are mentioned below.

| File | Description |
| ------ | ------ |
| test.ipynb | displays the first few rows of each table to let you check database. |
| create_tables.py | drops and creates tables. You run this file to reset the tables before each time you run your ETL scripts. |
| etl.ipynb | reads and processes a single file from song_data and log_data and loads the data into tables. This notebook contains detailed instructions on the ETL process for each of the tables. |
| etl.py | reads and processes files from song_data and log_data and loads them into the tables. |
| sql_queries.py | contains all sql queries, and is imported into the last three files above. |





