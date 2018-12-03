from app import app
from db_setup import init_db, db_session
#from forms import MusicSearchForm, AlbumForm
from flask import flash, render_template, request, redirect
#from models import Album, Artist
from db_model_google import Attachments
from tables import Results
import googledrive as gd
import json
init_db()
qry = db_session.query(Attachments)
results = qry.all()
table = Results(results)