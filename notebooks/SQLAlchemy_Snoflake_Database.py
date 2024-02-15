#Importing warnings and dependencies
import warnings
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

# Loading the environment variables from .env file
load_dotenv()

# Ignore warnings
warnings.filterwarnings("ignore")

# Database connection details
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DATABASE_NAME}"

# Creating SQLAlchemy engine for MySQL
mysql_engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creating MySQL table
Base = declarative_base()

class CFADataTable(Base):
    __tablename__ = "CFA_data_table"

    id = Column(Integer, primary_key=True, index=True)
    Name_of_the_topic = Column(String(255))
    Year = Column(Integer)
    Level = Column(String(50))
    Introduction_Summary = Column(String(500))
    Learning_Outcomes = Column(String(500))
    Link_to_the_Summary_Page = Column(String(255))
    Link_to_the_PDF_file = Column(String(255))

    def __repr__(self):
        return f"<CFADataTable(id={self.id}, Name_of_the_topic={self.Name_of_the_topic}, Year={self.Year})>"

# Creating MySQL table in the database
Base.metadata.create_all(bind=mysql_engine)

# Creating Snowflake engine
snowflake_engine = create_engine(
    'snowflake://{user}:{password}@{account}/'.format(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
    )
)

# Snowflake queries
create_database_query = "CREATE OR REPLACE DATABASE CFA_DATABASE;"
create_table_query = """CREATE OR REPLACE TABLE CFA_DATA_TABLE (
    name_of_the_topic STRING(255),
    Year STRING,
    level STRING,
    introduction_summary STRING,
    learning_outcomes STRING,
    link_to_the_summary_page STRING,
    link_to_the_pdf STRING
    );"""

create_warehouse = """CREATE OR REPLACE WAREHOUSE CFA_DATA_WAREHOUSE
    WITH WAREHOUSE_SIZE='X-SMALL'
    AUTO_SUSPEND = 180
    AUTO_RESUME = TRUE
    INITIALLY_SUSPENDED=TRUE;"""

create_stage = """CREATE STAGE DUMMY DIRECTORY = (ENABLE = true);"""
upload_to_stage = """PUT 'file://C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/test.csv' @DUMMY;"""

copy_stage_to_table = """COPY INTO CFA_DATA_TABLE
FROM @CFA_DATABASE.public.dummy
FILE_FORMAT = (type = csv field_optionally_enclosed_by='"')
PATTERN = '.*test.csv.gz'
ON_ERROR = 'CONTINUE';

"""

try:
    # MySQL operations
    mysql_connection = mysql_engine.connect()
    mysql_connection.close()
    
    # Snowflake operations
    snowflake_connection = snowflake_engine.connect()
    results = snowflake_connection.execute(create_database_query)
    results = snowflake_connection.execute(create_table_query)
    results = snowflake_connection.execute(create_warehouse)
    results = snowflake_connection.execute("USE DATABASE CFA_DATABASE")
    results = snowflake_connection.execute(create_stage)
    results = snowflake_connection.execute(upload_to_stage)
    results = snowflake_connection.execute(copy_stage_to_table)

finally:
    print("Done")
    snowflake_connection.close()
    snowflake_engine.dispose()
