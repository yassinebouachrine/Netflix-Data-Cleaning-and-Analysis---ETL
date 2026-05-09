import pyodbc
from sqlalchemy import create_engine

SERVER   = 'Yassine'       
DATABASE = 'netflix_db'
DRIVER   = 'ODBC Driver 17 for SQL Server'

CONNECTION_STRING = (
    f"mssql+pyodbc://{SERVER}/{DATABASE}"
    f"?driver={DRIVER.replace(' ', '+')}"
    f"&trusted_connection=yes"   
)

def get_engine():
    return create_engine(CONNECTION_STRING)