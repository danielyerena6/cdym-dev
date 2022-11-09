from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    db_host = environ.get('cdym_db_host')
    db_name = environ.get('cdym_db name')
    db_port = environ.get('cdym_db_port')
    db_user = environ.get('cdym_db_user')
    db_password = environ.get('cdym_db_password')
    db_uri = "postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}".format(db_user, db_password, db_host,
                                                                                       db_port, db_name)
