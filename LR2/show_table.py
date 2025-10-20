from sqlalchemy import create_engine, text 

engine = create_engine("postgresql://postgres:secret@localhost:5432/lr2_db")

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users"))  
    for row in result:
        print(row)