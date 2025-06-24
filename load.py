from sqlalchemy import create_engine

def load_to_postgres(df, table_name):
    engine = create_engine("postgresql://postgres:1234@localhost:5432/stockdb")
    df.to_sql(table_name, engine, if_exists='replace', index=False)

