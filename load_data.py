from sqlalchemy import create_engine
import pandas as pd

# PostgreSQL connection URL (Update with your credentials)
db_url = "postgresql://postgres:shiju12@localhost/telematicsdb"

# Create a database connection
engine = create_engine(db_url)

# Load the cleaned dataset
df = pd.read_csv("Cleaned_Telematicsdata.csv")

# Store data into SQL table
df.to_sql("telematics_data", con=engine, if_exists="replace", index=False)

print("\n✅ Data successfully stored in PostgreSQL database!")
