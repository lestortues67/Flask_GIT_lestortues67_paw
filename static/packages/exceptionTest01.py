"""
Date : 13/12/2022
Auteur : Christian Doriath
Dossier : /Python39/MesDEv/Flask/Flask_codebase2023
Fichier : exceptionTest01.py
Description : Tester s'il est possible de créer ses propres exceptions. 
"""





class myException01(Exception):
    pass




def errorPrinter(p_value):
    print("type(p_value) : ",type(p_value))
    print("dir(p_value) : ",dir(p_value))
    print("p_value.__context__ : ",p_value.__context__)
    print("p_value.__cause__ : ",p_value.__cause__)
    print("p_value.__class__ : ",p_value.__class__)


    print("Voici le message d'erreur : ",p_value)
    print("Voici le message d'erreur : ",p_value['errorText'])





def add5(p_value):
    if p_value>150:
        raise myException01({'errorText' : "SQLAlchemy reporte une erreur"})
    if p_value>100:
        raise myException01({'errorText' : "La balise 'sous-catégorie' est absente"})    
    if p_value>50:
        raise myException01({'errorText' : "La balise 'catégorie' est absente"})
    
    
    else:
        return p_value + 5 




try:
    print("add5(65) : ",add5(65))
except Exception as e:
    errorPrinter(e)
else:
    print("Je passe par 'else'")
finally:
    print("Je passe par 'finally'")


# print("add5(20) : ",add5(20))






