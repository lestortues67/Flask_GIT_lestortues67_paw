"""
Source : 
Date : 30/01/2019
Auteur : Christian Doriath
Dossier : /Python34/MesDEv/Flask/FlaskBootstrap_BASE
Fichier : classes.py
Description : Toutes les ROUTES.
"""

from starter import * 


@app.route('/')
def myindex():
    return render_template('index.html',title="Flask_cadebase2023")

# 19/11/2022
# Jinja sait envoyer une balise html ? 
@app.route('/txBaliseHtml01', methods=['GET', 'POST'])
def mytxBaliseHtml01():
    elements = "<span> je suis un test </span>"
    btnBlue = "<button type='button' class='btn btn-primary' id='btnBlue0' data-state='0' >bouton bleu</button>"
    btnRed = "<button type='button' class='btn btn-danger' id='btnRed0' data-state='0' >bouton rouge</button>"
    return render_template('txBaliseHtml01.html',elements=elements,btnBlue=btnBlue,btnRed=btnRed) 




@app.route('/aPropos01')
def myaPropos01():
    return render_template('aPropos01.html',title="A propos")


# 21/11/2022 
#test des btn avec svg 
@app.route('/btn01')
def mybtn01():
    return render_template('btn01.html',title="Bouton avec svg")






@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


