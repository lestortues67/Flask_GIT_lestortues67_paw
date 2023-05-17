"""
Source : 
Date : 30/01/2019
Auteur : Christian Doriath
Dossier : /Python34/MesDEv/Flask/FlaskBootstrap_BASE
Fichier : classes.py
Description : tables.py contient toutes les déclarations des classes de BASE DE DONNEES.





"""



from starter import * 

class elements (db.Model):
    __tablename__ = 'elements'
    # Cette table utilise toutes les valeurs de la liste 'mcObligatoire' pour créer CHAQUE CHAMPS
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(45))

    deleted = db.Column(db.Boolean)
    visuel = db.Column(db.Boolean)

    langage = db.Column(db.String(45))
    categorie = db.Column(db.String(45))
    souscategorie = db.Column(db.String(45))

    datecreation = db.Column(db.DateTime)
    datecreation_texte = db.Column(db.Text)

    datemodification = db.Column(db.DateTime)
    datemodification_texte = db.Column(db.Text)

    auteur = db.Column(db.String(45))
    commentaire = db.Column(db.Text)

    code_html = db.Column(db.Text)
    code_js = db.Column(db.Text)


    def __init__(self, p_nom, p_deleted, p_visuel, p_langage, p_categorie, p_souscategorie, p_datecreation, p_datecreation_texte, p_datemodification,
    p_datemodification_texte, p_auteur, p_commentaire, p_code_html, p_code_js ):
    # Ici on crée une instance de la classe 'elements'
    # le champ 'id' est généré automatiquement par MySQL
    # SQLAlchemy adds an implicit constructor to all model classes : __init__

        self.nom = p_nom

        self.deleted = p_deleted
        self.visuel = p_visuel

        self.langage = p_langage
        self.categorie = p_categorie
        self.souscategorie = p_souscategorie

        self.datecreation = p_datecreation
        self.datecreation_texte = p_datecreation_texte

        self.datemodification = p_datemodification
        self.datemodification_texte  = p_datemodification_texte

        self.auteur = p_auteur
        self.commentaire = p_commentaire
        
        self.code_html = p_code_html
        self.code_js = p_code_js
        
    def add(p_mot):
    # Ici on ajoute à la table  1 seul enregistrement en créant une instance de classe
    # La valeur de 'item' est un string aléatoire de 10 symboles. 
        Myadd = languefr(p_mot)
        db.session.add(Myadd) 
        db.session.commit()
    def addListe(p_liste):
        db.session.bulk_save_objects(p_liste)
        db.session.commit()
    def RetrieveMot(p_mot):
        # ici on recherche un enregistrement par son champ 'mot': 
        return (htmlCode.query.filter_by(mot=p_mot).first())


