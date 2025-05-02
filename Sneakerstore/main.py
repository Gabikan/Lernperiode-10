from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append("..")  # Damit Flask die models.py im übergeordneten Ordner findet

from models import Sneaker, Brand, Base

app = Flask(__name__)

# Datenbankverbindung
engine = create_engine('sqlite:///../sneakerstore.db')
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def home():
    sneakers = session.query(Sneaker).all()
    return render_template('home.html', sneakers=sneakers)

if __name__ == '__main__':
    app.run(debug=True)
