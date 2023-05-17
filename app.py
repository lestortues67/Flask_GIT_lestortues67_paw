"""
An example how a very minimal Flask blog using TinyMongo (as an local database) and Summernote (as visual control).

Note: I include verbose comments for people that are using this code as tutorial.

This is meant not to be a serious tool, but has minimal functionality to demonstrate how a larger blog could leverage
these particular tools into a bigger project.  Note that there is NO login or userid, etc. If you want that, then
I suggest using the package Flask-Login (simple implementation) or for a more comprehesive application, Flask-Security.

The blog has 4 routes:
1. '/' is the index of all pages
2. '/view/<id>' shows a page with a particular id (this is the actual MongoDB id of the object)
3. '/edit' and '/edit/<id>' if no id is supplied, a new page is created.  if a valid id is presented, edit the page
4. '/delete/<id>' delete a page with a particular ID.

Flask: http://flask.pocoo.org/

A very comprehensive, robust microframework

TinyMongo: https://github.com/schapman1974/tinymongo

A PyMongo-like wrapper of tinyDB.  It is trivial to port TinyMongo to full-fledged MongoDB.

SummerNote: https://summernote.org/

Summernote is a fairly lightweight and fast WYSYWIG web control that has a Content Delivery Network implementation.
"""

import datetime
import string
from flask import Flask, request, render_template, session, redirect, url_for, flash, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, DateTimeField
from wtforms.validators import DataRequired,Regexp,IPAddress,Length,Required,InputRequired
from wtforms.validators import Email ,Regexp, EqualTo, NumberRange, NoneOf, URL, AnyOf 
#List of available validators : http://wtforms.simplecodes.com/docs/0.6.1/validators.html
from flask_sqlalchemy import SQLAlchemy
from random import choice
import locale
import time
import pdb
import json 
from flask_debugtoolbar import DebugToolbarExtension
import os 
import uuid

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    
app = Flask(__name__)
#DB = TinyMongoClient().blog


app.debug = True
app.config['SECRET_KEY'] = 'hard to guess string'
#app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://MissPandinou:clairePapa2021@MissPandinou.mysql.eu.pythonanywhere-services.com/MissPandinou$missPandinou'

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+mysqlconnector://root:root@localhost/relation_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)


if not app.debug:
    file_handler = FileHandler('errorlog.txt')
    file_handler.setLevel(WARNING)
    app.logger.addHandler(file_handler)

class Langage (db.Model):
    __tablename__ = 'langage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dateCreation = db.Column(db.DateTime)
    dateLongueTexteCreation = db.Column(db.Text)
    epochCreation = db.Column(db.Integer)
    langage = db.Column(db.Text)
    supprime = db.Column(db.Integer)
    dossiers = db.relationship("Dossier", backref="langage")
    uuid = db.Column(db.Text)
    def __init__(self, p_langage):
        # Ici on crée une instance de la classe 'Langage'
        # le champ 'id' est généré automatiquement par MySQL

        now = datetime.datetime.today()
        #now = datetime_from_utc_to_local(datetime.datetime.today())
        today_year = datetime.datetime.today().year
        today_month = datetime.datetime.today().month
        today_day = datetime.datetime.today().day

        today_hour = datetime.datetime.today().hour
        today_minute = datetime.datetime.today().minute
        today_second = datetime.datetime.today().second

        print("today : ",today_year," ",today_month," ",today_day," ",today_hour," ",today_minute," ",today_second,"\n")

        dateHeureCmde = datetime.datetime(today_year,today_month,today_day,today_hour,today_minute,today_second,0)
        dateEpoch = int(time.time())+7200
        # il convient de modifier la ligne suivante pour tenir compte du décalage horaire
        # entre la France et le serveur
        dateLongueTexte = time.strftime("%A, %d %B %Y %H:%M:%S")

        self.langage=p_langage
        self.dateCreation=now
        self.dateLongueTexteCreation = dateLongueTexte
        self.epochCreation = dateEpoch
        self.supprime = 0
        self.uuid = str(uuid.uuid4())
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        
    def create(self, p_langage):
        Myadd = Langage(p_langage)
        db.session.add(Myadd)
        db.session.commit()

class Dossier (db.Model):
    __tablename__ = 'dossier'
    # Cette table est un enfant de la classe 'Langage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dateCreation = db.Column(db.DateTime)
    dateLongueTexteCreation = db.Column(db.Text)
    epochCreation = db.Column(db.Integer)
    parentId = db.Column(db.Integer, db.ForeignKey("langage.id"), nullable=False)
    dossier = db.Column(db.Text)
    supprime = db.Column(db.Integer)
    sousdossiers = db.relationship("Sousdossier", backref="langage")
    uuid = db.Column(db.Text)
    def __init__(self, p_parentId, p_dossier):
        # Ici on crée une instance de la classe 'Langage'
        # le champ 'id' est généré automatiquement par MySQL


        now = datetime.datetime.today()
        #now = datetime_from_utc_to_local(datetime.datetime.today())
        today_year = datetime.datetime.today().year
        today_month = datetime.datetime.today().month
        today_day = datetime.datetime.today().day

        today_hour = datetime.datetime.today().hour
        today_minute = datetime.datetime.today().minute
        today_second = datetime.datetime.today().second

        print("today : ",today_year," ",today_month," ",today_day," ",today_hour," ",today_minute," ",today_second,"\n")

        dateHeureCmde = datetime.datetime(today_year,today_month,today_day,today_hour,today_minute,today_second,0)
        dateEpoch = int(time.time())+7200
        # il convient de modifier la ligne suivante pour tenir compte du décalage horaire
        # entre la France et le serveur
        dateLongueTexte = time.strftime("%A, %d %B %Y %H:%M:%S")


        try:
            self.parentId = p_parentId
            self.dossier = p_dossier
            self.dateCreation=now
            self.dateLongueTexteCreation = dateLongueTexte
            self.epochCreation = dateEpoch
            self.supprime = 0
            self.uuid = str(uuid.uuid4())
        except: 
            print("error __init__")
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



class Sousdossier (db.Model):
    __tablename__ = 'sousdossier'
    # Cette table est un enfant de la classe 'Langage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dateCreation = db.Column(db.DateTime)
    dateLongueTexteCreation = db.Column(db.Text)
    epochCreation = db.Column(db.Integer)
    parentId = db.Column(db.Integer, db.ForeignKey("dossier.id"), nullable=False)
    supprime = db.Column(db.Integer)
    sousdossier = db.Column(db.Text)
    uuid = db.Column(db.Text)
    def __init__(self, p_parentId, p_sousdossier):
        
        now = datetime.datetime.today()
        #now = datetime_from_utc_to_local(datetime.datetime.today())
        today_year = datetime.datetime.today().year
        today_month = datetime.datetime.today().month
        today_day = datetime.datetime.today().day

        today_hour = datetime.datetime.today().hour
        today_minute = datetime.datetime.today().minute
        today_second = datetime.datetime.today().second

        print("today : ",today_year," ",today_month," ",today_day," ",today_hour," ",today_minute," ",today_second,"\n")

        dateHeureCmde = datetime.datetime(today_year,today_month,today_day,today_hour,today_minute,today_second,0)
        dateEpoch = int(time.time())+7200
        # il convient de modifier la ligne suivante pour tenir compte du décalage horaire
        # entre la France et le serveur
        dateLongueTexte = time.strftime("%A, %d %B %Y %H:%M:%S")

        try:
            self.parentId = p_parentId
            self.sousdossier = p_sousdossier
            self.dateCreation=now
            self.dateLongueTexteCreation = dateLongueTexte
            self.epochCreation = dateEpoch
            self.supprime = 0
            self.uuid = str(uuid.uuid4())
        except: 
            print("error __init__")
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Notrecode (db.Model):
    __tablename__ = 'notrecode'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dateCreation = db.Column(db.DateTime)
    dateLongueTexteCreation = db.Column(db.Text)
    epochCreation = db.Column(db.Integer)
    titre = db.Column(db.Text)
    langage = db.Column(db.Text)
    dossier = db.Column(db.Text)
    sousdossier = db.Column(db.Text)
    fichier = db.Column(db.Text)
    supprime = db.Column(db.Integer)
    
    #def __init__(self, p_titre, p_langage, p_dossier, p_sousdossier, p_fichier, p_supprime):
    def __init__(self, p_titre, p_langage, p_dossier, p_sousdossier,p_fichier):
        # Ici on crée une instance de la classe 'Langage'
        # le champ 'id' est généré automatiquement par MySQL

        now = datetime.datetime.today()
        #now = datetime_from_utc_to_local(datetime.datetime.today())
        today_year = datetime.datetime.today().year
        today_month = datetime.datetime.today().month
        today_day = datetime.datetime.today().day

        today_hour = datetime.datetime.today().hour+2
        today_minute = datetime.datetime.today().minute
        today_second = datetime.datetime.today().second

        print("today : ",today_year," ",today_month," ",today_day," ",today_hour," ",today_minute," ",today_second,"\n")

        dateHeureCmde = datetime.datetime(today_year,today_month,today_day,today_hour,today_minute,today_second,0)
        dateEpoch = int(time.time())+7200
        # il convient de modifier la ligne suivante pour tenir compte du décalage horaire
        # entre la France et le serveur
        dateLongueTexte = time.strftime("%A, %d %B %Y %H:%M:%S")

        self.langage= p_langage
        self.titre = p_titre
        self.langage = p_langage
        self.dossier = p_dossier
        self.sousdossier = p_sousdossier
        self.fichier = p_fichier
    
        self.dateCreation=now
        self.dateLongueTexteCreation = dateLongueTexte
        self.epochCreation = dateEpoch
        self.supprime = 0
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

#Créer toutes les tables 
db.create_all() 

            
@app.route('/')
def index():
    """return all the pages to a user view"""
    return render_template('page_list.html')

@app.route('/page1', methods=['GET','POST'])
def page1():          
    return render_template('page1.html')

@app.route('/page2', methods=['GET','POST'])
def page2():        
    return render_template('page2.html')

@app.route('/page3', methods=['GET','POST'])
def page3():        
    return render_template('page3.html')

@app.route('/createPage', methods=['GET','POST'])
def createPage():
    print("Voici le chemin absolu : ",os.getcwd())
    if request.method == 'POST':
        contenu = "jhhj"
        mon_uuid = str(uuid.uuid4())
        print("request.form : ", request.form)        
        print("request.form[titre] : ", request.form["titre"])
        print("request.form[langage] : ", request.form["langage"])
        # print("request.form[dossier] : ", request.form["dossier"])
        # print("request.form[sousdossier] : ", request.form["sousdossier"])
        with open(os.path.join(os.getcwd()+"/static", mon_uuid), "w") as file:
            # Écrire du texte dans le fichier
            file.write(request.form["fichier"])
            # doss = request.form["dossier"]
            doss2 = request.form.get('dossier')
            print("voici doss2:",doss2)
        # maValeur = Notrecode(request.form["titre"],request.form["langage"],doss or "",request.form["sousdossier"],mon_uuid)
        maValeur = Notrecode(request.form["titre"],request.form["langage"],request.form["dossier"],request.form["sousdossier"],mon_uuid)
        # def __init__(self, p_titre, p_langage, p_dossier, p_sousdossier,p_fichier):
        # maValeur = Notrecode(request.form["titre"],request.form["langage"],"dossier","sousdossier",mon_uuid)

        db.session.add(maValeur)
        db.session.commit() 
        print("les informations ont été ajoutés !!!! ")        
    return render_template('createPage.html')



# 19/04/2023
@app.route("/createLangage")
def mycreateLangage():
    s = randomString(10)
    l = Langage(s)
    db.session.add(l)
    db.session.commit()
    return (s+'<p> OK, a été ajouté</p>')

# 24/04/2023
@app.route("/getLangage")
def mygetLangage():
    # retourne TOUTES les lignes de la table 'langage'
    dd = Langage.query.filter_by().all()
    # parcourir les instances pour en créer une liste de dict
    ll = []
    for data in dd:
        d = {'id':data.id, 'dossier':data.langage}
        ll.append(d)
    return jsonify(ll)



# 19/04/2023
@app.route("/createDossier/<p_parent>")
def mycreateDossier(p_parent):
    # vérifier l'ID du parent existe 
    try:
        s = randomString(10)
        l = Dossier(p_parent, s)
        db.session.add(l)
        db.session.commit()
        return ('<span>Le dossier </span> '+s+'<span>, a été ajouté</span>')
    except Exception as e:
        print("Error "+ str(e))
        return ('Impossible de créer cet enregistrement avec cet id '+p_parent)

# 19/04/2023
@app.route("/getDossier/<p_parent>")
def mygetDossier(p_parent):
    dd = Dossier.query.filter_by(parentId = p_parent).all()
    # parcourir les instances pour en créer une liste de dict
    ll = []
    for data in dd:
        d = {'id':data.id, 'dossier':data.dossier,'parentId':data.parentId}
        ll.append(d)
    return jsonify(ll)


# 19/04/2023
@app.route("/createSousDossier/<p_parent>")
def mycreateSousDossier(p_parent):
    # vérifier l'ID du parent existe 
    try:
        s = randomString(10)
        l = Sousdossier(p_parent, s)
        db.session.add(l)
        db.session.commit()
        return ('<span>Le sous dossier </span> '+s+'<span>, a été ajouté</span>')
    except Exception as e:
        print("Error "+ str(e))
        return ('Impossible de créer cet enregistrement avec cet id '+p_parent)

# 19/04/2023
@app.route("/getSousDossier/<p_parent>")
def mygetSousDossier(p_parent):
    dd = Sousdossier.query.filter_by(parentId = p_parent).all()
    # parcourir les instances pour en créer une liste de dict
    ll = []
    for data in dd:
        d = {'id':data.id, 'sousdossier':data.sousdossier,'parentId':data.parentId}
        ll.append(d)
    return jsonify(ll)


# 09/05/2023
@app.route("/langageAll")
def mylangageAll():
    dd = Notrecode.query.filter_by().all()
    # parcourir les instances pour en créer une liste de dict
    ll = []
    for data in dd:
        ll.append(data.as_dict())
    return jsonify(ll)


# 09/05/2023
@app.route("/langage/<p_langageId>")
def mylangage(p_langageId):
    print("type(p_langageId) : ",type(p_langageId))
    print("p_langageId : ",p_langageId)
    print("p_langageId == 0 : ",int(p_langageId) == 0)
    if(int(p_langageId) == 0):
        print("p_ est 0 ")
        dd = Notrecode.query.all()
    else:
        dd = Notrecode.query.filter_by(langage = p_langageId).all()
    # parcourir les instances pour en créer une liste de dict
    ll = []
    for data in dd:
        ll.append(data.as_dict())
    return jsonify(ll)


# 09/05/2023
@app.route("/dossier/<p_dossierId>")
def mydossier(p_dossierId):
    print("type(p_dossierId) : ",type(p_dossierId))
    print("p_dossierId : ",p_dossierId)
    print("p_dossierId == 0 : ",int(p_dossierId) == 0)
    if(int(p_dossierId) == 0):
        print("p_ est 0 ")
        dd = Notrecode.query.all()
    else:
        dd = Notrecode.query.filter_by(dossier = p_dossierId).all()
    # parcourir les instances pour en créer une liste de dict
    ll = []
    for data in dd:
        ll.append(data.as_dict())
    return jsonify(ll)

# 09/05/2023
@app.route("/sousdossier/<p_sousdossierId>")
def mysousdossier(p_sousdossierId):
    print("type(p_sousdossierId) : ",type(p_sousdossierId))
    print("p_sousdossierId : ",p_sousdossierId)
    print("p_sousdossierId == 0 : ",int(p_sousdossierId) == 0)
    if(int(p_sousdossierId) == 0):
        print("p_ est 0 ")
        dd = Notrecode.query.all()
    else:
        dd = Notrecode.query.filter_by(sousdossier = p_sousdossierId).all()
    # parcourir les instances pour en créer une liste de dict
    ll = []
    for data in dd:
        ll.append(data.as_dict())
    return jsonify(ll)



# users = User.query.order_by(User.age.desc()).all()

# 09/05/2023
@app.route("/langageAllDecroissant")
def mylangageAllDecroissant():
    # dd = Notrecode.query.filter_by().all()
    dd = Notrecode.query.order_by(Notrecode.dateCreation.desc(),Notrecode.titre.desc()).all()
    # parcourir les instances pour en créer une liste de dict
    ll = []
    for data in dd:
        ll.append(data.as_dict())
    return jsonify(ll)

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler-- 404 status set explicitly"""
    return render_template('404.html'), 404


# papa est passé par ici 
#Claire est passée :)

