"""
Source : 
Date : 30/01/2019
Auteur : Christian Doriath
Dossier : /Python34/MesDEv/Flask/FlaskBootstrap_BASE
Fichier : classes.py
Description : Module des classes uniquement et PAS des fonctions db SQLAlchemy;
trop compliqué à ce jour.

Mot cles : 
"""



from starter import * 

class elementsForm(FlaskForm):
    myFile = FileField('myFile')
    # address = TextAreaField(label='Mailing Address', id="TextArea00",  [validators.optional(), validators.length(max=200)])
    address = TextAreaField(label='Mailing Address', id="TextArea00", default="texte")

class dragAndDropForm(FlaskForm):
    myFile = FileField('myFile')

class dragAndDrop1Form(FlaskForm):
    address = TextAreaField(label='Mailing Address', id="dropZone0", default="This is 'dropZone0' ! ", render_kw={'titi0':'titi0','tata0':'tata0'})

