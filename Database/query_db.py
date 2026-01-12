import sqlite3
import pandas as pd

db_path = r"C:\Users\HP\Desktop\Movie_Project\data\movies.db"
# Function to query 5 movies by genre and year range
def query_movies(genre, start_year, end_year):
    """
    Query 5 movies based on genre and year range, showing title, year, genre, and rating.
    """
    query = f"""
    SELECT 
        [title ], 
        CAST(SUBSTR([title ], -5, 4) AS INTEGER) AS year,
        [genres ],
        [rating]
    FROM movies
    WHERE [genres ] LIKE '%{genre}%'
      AND CAST(SUBSTR([title ], -5, 4) AS INTEGER) BETWEEN {start_year} AND {end_year}
    LIMIT 5
    """
    # Open connection inside function to ensure it's always available
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query, conn)
    return df
