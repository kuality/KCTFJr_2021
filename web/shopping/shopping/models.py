from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Shopping.sqlite', connect_args={'check_same_thread': False})
Base = declarative_base()
Session = sessionmaker(bind=engine)
db_session = Session()
db = SQLAlchemy()

class User(Base):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(32),unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    point = db.Column(db.Integer, nullable=False)

    def is_active(self):
        return True

    def __repr__(self):
        return " "
class Contact(db.Model):
    __tablename__ = "user_context"

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(32), nullable=False)
    context = db.Column(db.Text)
User.__table__.create(bind=engine, checkfirst=True)


