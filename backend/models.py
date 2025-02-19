import mysql.connector
from mysql.connector import pooling
from config import DB_CONFIG

# Create connection pool
connection_pool = pooling.MySQLConnectionPool(
    pool_name="search_pool",
    pool_size=DB_CONFIG['pool_size'],
    pool_reset_session=True,
    **{k: v for k, v in DB_CONFIG.items() if k not in ['pool_size', 'max_overflow', 'pool_recycle']}
)

def get_db_connection():
    return connection_pool.get_connection()

def create_tables():
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS search_history (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                query TEXT NOT NULL,
                results TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        """)

        connection.commit()
    except Exception as e:
        raise RuntimeError(f"Database error: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Initialize tables only if not in test environment
if DB_CONFIG.get('database') != 'test':
    create_tables()
