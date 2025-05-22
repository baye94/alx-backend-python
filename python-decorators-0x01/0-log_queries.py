import sqlite3
import functools
from datetime import datetime

#### decorator to log SQL queries
def log_queries():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Try to extract the SQL query from kwargs or args
            query = kwargs.get('query') or (args[0] if args else None)

            # Log the query with a timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if query:
                print(f"[{timestamp}] Executing SQL Query: {query}")
            else:
                print(f"[{timestamp}] No SQL query provided.")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_queries()
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
