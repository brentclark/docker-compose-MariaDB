from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import select, func
from sqlalchemy import Table, MetaData, select, func
from sqlalchemy import create_engine

# Replace with your actual credentials and database details
#DATABASE_URI = 'postgresql+psycopg2://webmailwebdb_staging_user:SbklwDVFaHlNttuhVHHHfecVD6pUIV6@webmaildb-staging.jnb1.host-h.net/webmailwebdb?sslmode=require'
DATABASE_URI = 'postgresql+psycopg2://webmailwebdbuser:JtdwqX5KRrGNumtXsaRoGb2f74XqEE5XIxOmSZBg415Ix47XcMV@webmaildb.flk1.host-h.net/webmailwebdb?sslmode=require'

engine = create_engine(DATABASE_URI)

try:
    connection = engine.connect()
    print("Connected to PostgreSQL successfully!")
except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")

meta = MetaData()
users = Table("users", meta, autoload_with=engine)

stmt = (
    select(
        users.c.username,
        func.count().label("cnt")
    )
    .group_by(users.c.username)
    .having(func.count() > 1)
)

with engine.connect() as conn:
    rows = conn.execute(stmt).all()

for email, cnt in rows:
    print(email, cnt)

connection.close()