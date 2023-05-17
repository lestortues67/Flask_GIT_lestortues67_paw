"""
Date : 29/12/2022
Auteur : Christian Doriath
Dossier : /Python39/MesDEv/Flask/Flask_codebaseTest
Fichier : newMethods01.py
Description : TOUTES les méthodes retournent un namedTuple. 

=========================================================================

#Création d'un namedTuple appelé "methodResponse"
self.responseNamedTuple = namedtuple('methodResponse', ['succes', 'data', 'errorNamedTuple'])

'succes' informe du succès de la méthode avec True/False
'data' si une data est escomptée elle se trouve ici
'errorNamedTuple' si une erreur est à signaler elle se trouve ici

#Utilisation de "methodResponse" : 
return self.responseNamedTuple(True,(),())

=========================================================================

#Création d'un namedTuple appelé "errorNamedTuple"
self.errorNamedTuple = namedtuple('errorNamedTuple', ['logLevel','logMessage','TX_mail','mailSubject','mailMessage'])

'logLevel' avec un string,
'logMessage' avec un string,
'TX_mail' avec True/False,
'mailSubject' avec un string,
'mailMessage' avec un string

Quand 'succes':False, la méthode indique une erreur et 
'errorNamedTuple' contient OBLIGATOIREMENT un namedTuple au format
demandé par la méthode 'logMailAlerteInfo()'. 

#Utilisation de "errorNamedTuple" : 
except FileNotFoundError:
et0 = self.errorNamedTuple("error","FileNotFoundError, le dossier : "+self.path+" a provoqué une erreur",
True,"error with PATH","FileNotFoundError, le dossier : "+self.path+" a provoqué une erreur")
return self.responseNamedTuple(False,(),et0)


"""

from starter import * 


class Main(object):
    def __init__(self, p_path):
        # créer des objets utilse (instances des classes)
        self.logger = Log()
        self.path = p_path
        self.d = Dossier(self.path)
        self.mailSender = MailSender()
        # une instance de la classe 'Mail' qui s'appelle 'mail' est crée dans le fichier 'starter.py'
        self.errorNamedTuple = namedtuple('errorNamedTuple', ['logLevel','logMessage','TX_mail','mailSubject','mailMessage'])



    def run(self):


        """
        Phase 1 : Vérification et recherche des erreurs, enregistrer la propriété "INVALIDE"

        Phase 2 : Pour les oFile de type INVALIDE=False lire et stocker les datas. 

        ==========================================================================

        Phase 1 :

        1) Dossier est valide : Dossier_cheminEstValide(chemin) OK

        2) dossier contient des fichiers : Dossier_dossierEstNonVide(chemin) OK

        3) à partir de l'extension du fichier renseigner la propriété 'type' : 
        Fichier_setType_setInvalide() sur TOUS les oFile OK 

        4) Vérifier la taille des fichiers type="CODE"
        Trier les oFile sur type== «CODE» : Dossier_getCodeFiles()
        Vérifier la taille avec : Fichier_verifTaille_tf()

        5) Vérifier la présence du fichier associé pour les oFile avec extension== «.MC»

        a) Créer une liste des oFile 'MC' en triant les oFile sur extension== «.MC»:
        listMC = Dossier_getMcFiles()

        b) Créer une liste des oFile 'IMAGE' en triant les oFile sur type== «NONCODE»:
        listNonCode = Dossier_getNonCodeFiles()

        c) Parcourir tous les oFile dans la sélection 'listMC'

        d) Rechercher la présence du fichier associé dans la liste 'listNonCode' avec le même nom de fichier: 
        Dossier_searchInList(listNonCode, 'fichier', o.dict['fichier']

        6) Vérifier la présence du fichier associé pour les oFile avec type == «NONCODE»

        a) Créer une liste des oFile 'IMAGE' en triant les oFile sur type== «NONCODE»:
        listNonCode = Dossier_getNonCodeFiles()

        b) Créer une liste des oFile 'CODE' en triant les oFile sur type== «CODE»:
        listCode = Dossier_getCodeFiles()

        c) Parcourir tous les oFile dans la sélection 'listNonCode'

        d) Rechercher la présence du fichier associé avec le même nom de fichier dans la liste 'listCode': 
        Dossier_searchInList(listCode, 'fichier', o.dict['fichier']

        7) Copier chaque ligne de texte des fichiers 'CODE' vers une liste (array) : 
        a) créer une liste des oFile de type 'CODE' : 
        oFileCode = Dossier_getCodeFiles()

        b) Parcourir la liste 'oFileCode' pour copier chaque ligne de texte vers une liste : 
        oFile.Fichier_readText4b2_ToArray()

        8) Copier le texte des fichiers 'CODE' vers un string : 
        a) créer une liste des oFile de type 'CODE' : 
        oFileCode = Dossier_getCodeFiles()

        b) Parcourir la liste 'oFileCode' pour copier chaque le texte vers un string : 
        oFile.Fichier_readText4b2_ToString()

        9) Dans le texte, vérifier la présence de toutes les balises obligatoires 
        a) créer une liste des oFile de type 'CODE' : 
        oFileCode = Dossier_getCodeFiles()

        b) Parcourir la liste 'balisesObligatoires' 

        c) Balise START : Fichier_verifBaliseEndObligatoirePresent(p_motCle)
        d) Balise END : Fichier_verifBaliseStartObligatoirePresent(p_motCle)

        10) Dans le texte, vérifier la présence de toutes les datas obligatoires 
        a) créer une liste des oFile de type 'CODE' : 
        oFileCode = Dossier_getCodeFiles()

        b) Parcourir la liste 'balisesObligatoires' 

        c) Vérifier la présence de la data
        Fichier_verifDataObligatoirePresent(self, p_motCle)

        11) Afficher tous les fichiers : 
        for file in self.d.Dossier_getAllFiles()

        

        """


        """
        ==========================================================================




        Phase 1 :
        """
        self.logger.storeLogMessage("info", "Démarrage de l'app")

        # 1) Dossier est valide ? Dossier_cheminEstValide(chemin) OK
        print("Phase 1: Dossier est valide ? Dossier_cheminEstValide(chemin)")
        pathOk = self.d.Dossier_cheminEstValide()
        if not( pathOk.succes ):
            # ['succes', 'data', 'errorNamedTuple']
            print("pathOk : ",pathOk,"\n")
            print("pathOk.errorNamedTuple : ",pathOk.errorNamedTuple)
            # msg = "Une erreur "+pathOk['errorDict']+" s'est produite lors de la tentative d'ouvrir ce dossier : "+self.path        
            # save logs and send e-mail
            # self.l.logMailAlerteInfo(pathOk['logLevel'], msg, "erreur répertoire/dossier", msg)
            return False 

        # 2) dossier contient des fichiers ? Dossier_dossierEstNonVide(chemin) OK
        print("\nPhase 2: Dossier contient des fichiers ? Dossier_dossierEstNonVide(chemin)")
        filesArePresent = self.d.Dossier_dossierEstNonVide()
        if not(filesArePresent.succes):
            # le dossier ne contient PAS de fichiers 
            message = filesArePresent.errorNamedTuple 
            print("message erreur dossier vide : ",message)
            # save logs and send e-mail
            self.logMailAlerteInfo(message)
            return False 
        # YES, Le dossier contient des fichiers ! 
        my_oFiles = self.d.Dossier_getFiles() # la liste de TOUS les 'oFile'        

        if my_oFiles.succes:
            print("La méthode 'Dossier_getFiles()' a retourné "+str(len(my_oFiles.data))+" fichiers.")
        else:
            print("error avec self.d.Dossier_getFiles() : ")
            print(my_oFiles,"\n")
            print(my_oFiles.errorNamedTuple,"\n")

        # 3) à partir de l'extension du fichier renseigner la propriété 'type' : 
        # Fichier_setType_setInvalide() sur TOUS les oFile OK 
        print("\nPhase 3: Avec la méthode 'Fichier_setType_setInvalide()'' renseigner la propriété 'type' sur TOUS les oFile")
        for oFile in my_oFiles.data:
            oFile.Fichier_setType_setInvalide()

        print("Lister les fichiers invalidés après la méthode 'Fichier_setType_setInvalide()': ")
        for oFile in self.d.Dossier_getInvalideFiles().data:
            print("Fichier invalidé : ",oFile.nom)
            # Afficher "errorList" pour chaque fichier INVALIDE
            print("errorList : ",oFile.errorList,"\n")
        print("\n")
        

        # 4) Vérifier la taille des fichier VALIDE et de type="CODE"
        # Trier les oFile sur type== «CODE» : Dossier_getCodeFiles()
        print("\nPhase 4: Vérifier la taille des fichier VALIDE et de type='CODE'")
        oFileCode = self.d.Dossier_getValideCodeFiles()
        for oFile in oFileCode.data:
            if not oFile.Fichier_verifTaille_tf().succes:
                # print("Ce fichier CODE est trop grand : ",oFile.Fichier_getProperty('nom'))
                # print("AVANT Voici sa liste errorList : ",oFile.errorList)
                oFile.Fichier_setProperty('invalide', True)
                eNamedTuple = oFile.Fichier_verifTaille_tf().errorNamedTuple
                oFile.errorList.append(eNamedTuple)

        print("Lister les fichiers invalidés après la méthode 'Fichier_verifTaille_tf()': ")
        for oFile in self.d.Dossier_getInvalideFiles().data:
            print("Fichier invalidé : ",oFile.nom)
            # Afficher "errorList" pour chaque fichier INVALIDE
            print("errorList : ",oFile.errorList,"\n")
        print("\n")


        # 5) Vérifier la présence du fichier IMAGE associé pour les oFile MC () avec extension== «.MC» )
        print("\nPhase 5: Vérifier la présence du fichier associé IMAGE pour les oFile avec extension== «.MC»")

        # a) Créer une liste des oFile 'MC' en triant les oFile sur extension== «.MC»:
        # listMC = Dossier_getMcFiles()
        listMC = self.d.Dossier_getMcFiles()

        # b) Créer une liste des oFile 'IMAGE' en triant les oFile sur type== «NONCODE»:
        # listNonCode = Dossier_getNonCodeFiles()
        # print("\n Voici la liste des fichiers IMAGE") 
        fichiersIMAGE = self.d.Dossier_getNonCodeFiles()

        # c) Parcourir tous les oFile dans la sélection 'listMC'
        for oFileMc in listMC.data:
            # d) Rechercher la présence du fichier associé dans la liste 'fichiersIMAGE' avec le même nom de fichier: 
            # Dossier_searchInList(fichiersIMAGE, 'fichier', o.dict['fichier']    
            # self.d.Dossier_searchInList(fichiersIMAGE['data'], 'fichier', oFileMc.dict['fichier'])
            if not self.d.Dossier_searchInList(fichiersIMAGE.data, 'fichier', oFileMc.fichier).succes:
                print("Je recherche ce fichier : ",oFileMc.fichier," dans la liste des fichiers IMAGE")
                print("Ce fichier IMAGE est manquant : ",oFileMc.Fichier_getProperty('fichier'))
                # print("fichier manquant...............")
                oFileMc.Fichier_setProperty('invalide', True)
                et0 = self.errorNamedTuple("error","Fichier IMAGE manquant pour ce fichier MC : "+oFileMc.nom,
                True,"Fichier IMAGE manquant ","Fichier IMAGE manquant pour ce fichier MC : "+oFileMc.nom)
                oFileMc.errorList.append(et0)

        print("Lister les fichiers invalidés après la méthode qui recherche les fichiers IMAGE: ")
        for oFile in self.d.Dossier_getInvalideFiles().data:
            print("Fichier invalidé : ",oFile.nom)
            # Afficher "errorList" pour chaque fichier INVALIDE
            print("errorList : ",oFile.errorList,"\n")
        print("\n")


        # 6) Vérifier la présence du fichier associé MC pour les oFile 'IMAGE' (avec type == «NONCODE» )
        print("\nPhase 6: Vérifier la présence du fichier associé MC pour les oFile IMAGE avec type == «NONCODE»")

        # a) Créer une liste des oFile 'IMAGE' en triant les oFile sur type== «NONCODE»:
        # fichiersIMAGE = Dossier_getNonCodeFiles()
        fichiersIMAGE = self.d.Dossier_getNonCodeFiles()

        # b) Créer une liste des oFile 'CODE' en triant les oFile sur type== «CODE»:
        # listCode = Dossier_getCodeFiles()
        listCode = self.d.Dossier_getCodeFiles()
        

        # c) Parcourir tous les oFile dans la sélection 'fichiersIMAGE'
        for oFileNonCode in fichiersIMAGE.data:
            # d) Rechercher la présence du fichier associé avec le même nom de fichier dans la liste 'listCode': 
            # Dossier_searchInList(listCode, 'fichier', o.dict['fichier']
            # self.d.Dossier_searchInList(listCode['data'], 'fichier', oFileNonCode.dict['fichier'])
            if not self.d.Dossier_searchInList(listCode.data, 'fichier', oFileNonCode.fichier).succes:
                print("Ce fichier MC est introuvable : ",oFileNonCode.fichier)
                oFileNonCode.Fichier_setProperty('invalide', True)
                et0 = self.errorNamedTuple("error","Fichier MC manquant pour ce fichier MC : "+oFileNonCode.nom,
                True,"Fichier MC manquant ","Fichier MC manquant pour ce fichier MC : "+oFileNonCode.nom)
                oFileNonCode.errorList.append(et0)

        print("Lister les fichiers invalidés après la méthode qui recherche les fichiers MC: ")
        for oFile in self.d.Dossier_getInvalideFiles().data:
            print("Fichier invalidé : ",oFile.nom)
            # Afficher "errorList" pour chaque fichier INVALIDE
            print("errorList : ",oFile.errorList,"\n")
        print("\n")

        # 7) Copier chaque ligne de texte des fichiers 'CODE' vers une liste (array) : 
        print("\nPhase 7: Copier chaque ligne de texte des fichiers 'CODE' vers self.listeLigne")
        # a) créer une liste des oFile de type 'CODE' : 
        oFileCode = self.d.Dossier_getCodeFiles()

        # b) Parcourir la liste 'oFileCode' pour copier chaque ligne de texte vers une liste : 
        for oFile in oFileCode.data:
            oFile.Fichier_readText4b2_ToArray()        

        # c) Afficher toutes les listes des lignes 
        for oFile in oFileCode.data:
            if not oFile.invalide:
                print("Array et ses lignes pour le fichier "+oFile.nom+" : ", oFile.listeLigne)
                print("-----------------------------")

        # 8) Copier le texte des fichiers 'CODE' vers un string : 
        print("\nPhase 8: Copier chaque ligne de texte des fichiers 'CODE' vers self.stringTexte")
        # a) créer une liste des oFile de type 'CODE' : 
        # oFileCode = Dossier_getCodeFiles()
        oFileCode = self.d.Dossier_getCodeFiles()

        # b) Parcourir la liste 'oFileCode' pour copier chaque le texte vers un string : 
        # oFile.Fichier_readText4b2_ToString()
        for oFile in oFileCode.data:
            oFile.Fichier_readText4b2_ToString()

        # c) Afficher toutes les strings des lignes 
        for oFile in oFileCode.data:
            if not oFile.invalide:
                print("Le string et ses lignes pour le fichier "+oFile.nom+" : ", oFile.stringTexte)
                print("-----------------------------")

        # 9) Dans le texte, vérifier la présence de toutes les balises obligatoires 
        print("\nPhase 9: Dans le texte self.stringTexte, vérifier la présence de toutes les balises obligatoires")
        # a) créer une liste des oFile de type 'CODE' : 
        # oFileCode = Dossier_getCodeFiles()
        oFileCode = self.d.Dossier_getCodeFiles()

        # b) Parcourir la liste 'balisesObligatoires' 
        # return self.responseNamedTuple(True,(),())
        for balise in balisesObligatoires:
            for oFile in oFileCode.data:
                # c) Balise START : Fichier_verifBaliseStartObligatoirePresent(p_motCle)
                if not oFile.Fichier_verifBaliseStartObligatoirePresent(balise).succes:
                    print("Balise START manquante : ",balise," | dans le fichier : ",oFile.nom)
                    et0 = self.errorNamedTuple("error","Le manque de la balise START pour : "+balise+" a provoqué une erreur",
                    True,"error balise START pour : "+balise,"Le manque de la balise START pour : "+balise+" a provoqué une erreur")
                    oFile.errorList.append(et0)
                    oFile.Fichier_setProperty('invalide', True)

                # d) Balise END : Fichier_verifBaliseStartObligatoirePresent(p_motCle)        
                if not oFile.Fichier_verifBaliseEndObligatoirePresent(balise).succes:
                    print("Balise END manquante : ",balise," dans le fichier : ",oFile.nom)
                    et0 = self.errorNamedTuple("error","Le manque de la balise END pour : "+balise+" a provoqué une erreur",
                    True,"error balise END pour : "+balise,"Le manque de la balise END pour : "+balise+" a provoqué une erreur")
                    oFile.errorList.append(et0)
                    oFile.Fichier_setProperty('invalide', True)
        print("\nLister les fichiers VALIDE après la méthode qui recherche les balises OBLIGATOIRES: ")
        for oFile in self.d.Dossier_getValideFiles().data:
            print("Fichier VALIDE : ",oFile.nom)
        print("\n")
        print("\nLister les fichiers INVALIDE après la méthode qui recherche les balises OBLIGATOIRES: ")
        for oFile in self.d.Dossier_getInvalideFiles().data:
            print("Fichier INVALIDE : ",oFile.nom)
            for eT in oFile.errorList:
                print("errorTuple : ",eT,"\n")
            print("\n")
        print("\n")

        # 10) Dans le texte, vérifier la présence de toutes les datas obligatoires 
        print("\nPhase 10: Dans le texte self.stringTexte, vérifier la présence de toutes les datas obligatoires")
        print("Voici les balises utilisées : langage,categorie,souscategorie,commentaire,nom,code")
        # a) créer une liste des oFile de type 'CODE' : 
        oFileCode = self.d.Dossier_getCodeFiles()

        # b) Parcourir la liste 'balisesObligatoires' 
        for balise in balisesObligatoires:
            # c) Vérifier la présence de la data
            for oFile in oFileCode.data:
                if not oFile.Fichier_verifDataObligatoirePresent(balise).succes:
                    print("Data manquante pour la balise : ",balise," | dans le fichier : ",oFile.nom)
                    et0 = self.errorNamedTuple("error","Le manque de la DATA pour la balise : "+balise+" a provoqué une erreur",
                    True,"error DATA manquante pour la balise : "+balise,"Le manque de la DATA pour la balise : "+balise+" a provoqué une erreur")
                    oFile.errorList.append(et0)
                    oFile.Fichier_setProperty('invalide', True)
        print("\nLister les fichiers VALIDE après la méthode qui recherche les DATAS OBLIGATOIRES: ")
        for oFile in self.d.Dossier_getValideFiles().data:
            print("Fichier VALIDE : ",oFile.nom)
        print("\n")
        print("\nLister les fichiers INVALIDE après la méthode qui recherche les DATAS OBLIGATOIRES: ")
        for oFile in self.d.Dossier_getInvalideFiles().data:
            print("Fichier INVALIDE : ",oFile.nom)
            for eT in oFile.errorList:
                print("errorTuple : ",eT,"\n")
            print("\n")
        print("\n")
        
        return False # FIN provisoire ...    

        # 11) Afficher tous les fichiers : 
        print("\nPhase 11: Afficher tous les fichiers \n")

        # 12) Afficher le texte de chaque fichier CODE : 
        print("\nPhase 12: Afficher la liste self.errorList = [] de chaque fichier CODE qui est INVALIDE \n")

        # 13) Afficher la liste errorDict de chaque fichier CODE qui est INVALIDE: 
        print("\nPhase 13: Afficher la liste self.errorList = [] de chaque fichier CODE qui est INVALIDE \n")


        for oFile in self.d.Dossier_getCodeFiles()['data']:
            # print("Fichier : ",oFile['data'].dict['nom'])
            print("Fichier : ",oFile.dict['nom'])
            print("errorList : ",oFile.dict["errorList"],"\n")
        print("13) FIN   \n")

        

        # FIN PHASE 1
        # ==========================================================================

        # Phase 2 : Pour les oFile de type INVALIDE=False lire et stocker les datas. 






    def valideMySQL(self):
        """ Parcourir la liste des oFile VALIDE
        pour stocker les datas dans une table
        """

    def valideAlerteInfo(self):
        """ Parcourir la liste des oFile VALIDE
        pour inscrire les logs.
        """

    def invalideAlerteInfo(self):
        """ Parcourir la liste des oFile INVALIDE
        pour inscrire les logs et envoyer les 
        e-mails.
        """

        """
        self.responseNamedTuple = namedtuple('methodResponse', ['succes', 'data', 'errorNamedTuple'])
        #Création d'un namedTuple appelé "methodResponse"


        # Pour une réponse "True", exemple de création d'un namedTuple de type "methodResponse"
        # rTrue = self.responseNamedTuple(True,(),())

        
        """


    def logMailAlerteInfo(self,p_errorNamedTuple):
        """

        Inscrire des logs et/ou envoyer des
        e-mails. 
        Le p_ : 
        Un namedTuple appelé "errorNamedTuple"
        self.errorNamedTuple = namedtuple('errorNamedTuple', ['logLevel','logMessage','TX_mail','mailSubject','mailMessage'])

        Pour TX un mail utiliser ceci : 
        def sendMail(self, p_subject, p_message, p_type, p_ListeDestinataires=mailDestinataires):
        # p_subject : l'entête du mail, ex : "Une erreur de LOG"
        # p_message : ex : "Le LOG n'est PAS conforme à la norme ..."
        # p_ListeDestinataires est un ARRAY de string des e-mails des destinataires
        # p_type indique si le corps du mail est constitué de code HTML ou pas
        # seules 2 valeurs sont acceptées : 'html' ou TOUT autre string comme 'texte'

        Un e-mail est automatiquement envoyé quand logLevel = "ERROR" ou "CRITICAL" ou 'TX_mail']== True
        def storeLogMessage(self, p_level, p_message):

        """
        self.logger.storeLogMessage(p_errorNamedTuple.logLevel ,p_errorNamedTuple.logMessage)
        # if (p_errorNamedTuple.logLevel.upper() == "ERROR" or p_errorNamedTuple.logLevel.upper() == "CRITICAL" or p_errorNamedTuple.TX_mail == True):
        #     mailSender.sendMail(p_errorNamedTuple.mailSubject, p_errorNamedTuple.mailMessage, "texte", p_ListeDestinataires=mailDestinataires)


class MainOld(object):
    def __init__(self, p_path):
        """
    	Dans cette classe TOUT se passe dans __init__

    	1) Demander à la classe 'Dossier' une liste de dict :
    	 1 dict par fichier présent dans le dossier

    	2) Avec cette liste, créer un objet 'oFichier' 
    	pour chaque dict; renseigner ses propriétés ou son dict

    	3) Stocker chaque oFichier dans la liste 
    	'dossierFichier' de la classe 'Dossier' 
    	PS : la classe 'Data' n'est PLUS utilisée

    	4) Parcourir tous les oFichier pour les marquer 
    	VALIDE/INVALIDE selon des conditions

    	5) Importer dans le système tous les fichiers VALIDE 
    	et supprimer le fichier du dossier.

    	6) Envoyer e-mail et enregistrer un LOG pour 
    	chaque fichier INVALIDE

    	"""
        self.path = p_path
        # creér une instance de la classe 'Dossier' avec self.path
        d = Dossier(self.path)

        if not (d.Dossier_cheminEstValide()['succes']):
            msg = d.Dossier_cheminEstValide()['errorDict']
            print(msg)
            exit()
        else:
            """
            # le path est valide
            # 1) Demander à la classe 'Dossier' une liste de dict 
            # ( 1 dict par fichier présent dans le dossier)
            """
            if (d.Dossier_getFiles()['succes']):
                listOfFiles = d.Dossier_getFiles()['data']
                # print("listOfFiles : ",listOfFiles)
            else:
                print(d.Dossier_getFiles()['errorDict'])
                exit()
            # print("voici listOfFiles : ",listOfFiles)
            """
            # 2) Avec cette liste, créer un objet 'oFichier' 
            # pour chaque dict; renseigner ses propriétés ou son dict
            """
            for file in listOfFiles:
                # print("Voici file : ",file,"\n")
                oFichier = Fichier(file)
                """
                # 3) Stocker chaque oFichier dans la liste 
                # 'dossierFichier' de la classe 'Dossier' 
                # PS : la classe 'Data' n'est PLUS utilisée
                """
                d.Dossier_addFile(oFichier)
                """
                # 4) Parcourir tous les oFichier pour :
        		a) Définir les valeurs pour 'type' et 'invalide' selon ce tableau : 

        		extension est 		Type	invalide
        		présente dans 		
        		la liste : 

        		extensionCode 		CODE 	0
        		extensionNonCode	NONCODE 0
        		aucune			    NON 	1

    		    Les marquer VALIDE/INVALIDE selon les conditions suivantes : 
    				(utiliser les méthodes de la classe 'Fichier')
                
                ATTENTION : en fonction du type du fichier les vérif sont différentes. 
                4b) : Il reste des vérif pour un fichier de type CODE : 
                    - taille, 
                    - lecture du texte vers "listeLigne", "stringTexte"
                    - vérif présence balises, 
                    - stockage du texte entres balises
                    - si fichier MC recherche du fichier IMAGE associé

                4b.1) fichier CODE/MC sa taille < 5000 def verifTailleFichier(self):
                4b.2) lire le texte et le stocker dans les clés "listeLigne" et "stringTexte"
                4b.3) rechercher la présence de TOUTES les balises obligatoires
                4b.4) lire le contenu des balises obligatoires
                4b.5) si fichier MC recherche du fichier IMAGE associé

                4c) Il reste des vérif pour un fichier de type NONCODE : 
                    - fichier associé présent, 

            	4c.1) rechercher les fichiers IMAGE sans fichier MC def fichierMcManquant(self):
            	4c.2) rechercher les fichiers MC sans fichier IMAGE def fichierImageManquant(self):

            	"""

            for oFile in d.Dossier_getAllFiles():
                # 4a) marquer les proprités TYPE et INVALIDE basée sur l'extension
                oFile.Fichier_setType_setInvalide()

                typeOfFile = oFile.Fichier_getProperty("type") # "CODE", "NONCODE")
                print("typeOfFile : ",typeOfFile)

                if (typeOfFile == "CODE") :
                    # créer une instance de la classe 'Indicateur' qui est utile quand 
                    # plusieurs vérif doivent retourner True pour une validation
                    self.i = Indicateur(1)

                    # 4b.1) fichier CODE/MC sa taille < 5000 def verifTailleFichier(self):
                    # vérifier l'extension du fichier, est-elle acceptable ? 

                    if(self.i.Indicateur_getIndicateur()):
                        if not (oFile.Fichier_verifTaille_tf()):
                            self.i.Indicateur_indicateur_serie(False)
                            # oFile.Fichier_setProperty("errormsg",oFile.Fichier_verifTaille_data())
                        else:
                            self.i.Indicateur_indicateur_serie(True)

                    # 4b.2) lire le texte et le stocker dans les clés "listeLigne" et "stringTexte"
                    if(self.i.Indicateur_getIndicateur()):   
                        if not(oFile.Fichier_readText4b2_ToArray()):  
                            self.i.Indicateur_indicateur_serie(False)
                            messageErreur = oFile.Fichier_readText4b2_ToArray()   
                            oFile.Fichier_setProperty("errormsg",messageErreur)
                        if not(oFile.Fichier_readText4b2_ToString()):  
                            self.i.Indicateur_indicateur_serie(False)
                            messageErreur = oFile.readText4b2_ToString_data()
                            oFile.Fichier_setProperty("errormsg",messageErreur)

                    # 4b.3) rechercher la présence de TOUTES les balises obligatoires
                    for motCleBalise in mcObligatoire:
                        # On utilise et parcours la liste "mcObligatoire"
                        if(self.i.Indicateur_getIndicateur()):
                            if not(oFile.Fichier_verifBaliseObligatoirePresent(motCleBalise)):  
                                self.i.Indicateur_indicateur_serie(False)
                                oFile.Fichier_setProperty("errormsg",messageErreur)

                    # 4b.4) lire le contenu des balises obligatoires
                    r = Regex() # 4b4) lire les datas obligatoires contenues dans les balises obligatoires
                    for motCleBalise in mcObligatoire:
                        if(self.i.Indicateur_getIndicateur()):  
                            if not (r.Regex_texteEntreBalises(motCleBalise, oFile.Fichier_getProperty("stringTexte"))['succes']):
                                self.i.Indicateur_indicateur_serie(False)
                                messageErreur = r.Regex_texteEntreBalises(motCleBalise, oFile.Fichier_getProperty("stringTexte"))['errorDict']
                                oFile.Fichier_setProperty("errormsg",messageErreur)
                                oFile.Fichier_setProperty("invalide",1)
                            else: 
                                # stocker la data 
                                texte = r.Regex_texteEntreBalises(motCleBalise, oFile.Fichier_getProperty("stringTexte"))['data']
                                oFile.Fichier_setProperty(motCleBalise, texte)
                    # 4b.5) si fichier MC recherche du fichier IMAGE associé

                else: # "NONCODE"
                    self.i = Indicateur(1)
                    # 4c.1) rechercher les fichiers IMAGE sans fichier MC def fichierMcManquant(self):
                    fichier = oFile.Fichier_getProperty("fichier")

                    if(self.i.Indicateur_getIndicateur()):
                        # Dossier_elementIsPresent_tf(self, p_property, p_value)
                        a = 100

                    # 4c.2) rechercher les fichiers MC sans fichier IMAGE def fichierImageManquant(self):
                    if(self.i.Indicateur_getIndicateur()):
                        a = 100



            b = 100
    		# 5) Importer dans le système tous les fichiers VALIDE 
    		# et supprimer le fichier du dossier.
    		# créer une instance de la classe de stockage vers mySQL

            # table = DataHolder()
            # for valideFile in d.getValideFiles():
            #     table.add(valideFile)

                # vérifier si l'enregistrement dans la table est OK
    			# si oui, alors effecer le fichier du dosssier
                # d.deleteFile(valideFile)
            # 6) Envoyer e-mail et enregistrer un LOG pour 
    		# chaque fichier INVALIDE
    		# créer une instance des classe 'Log' et 'Mail'

            # log = Log()
            # mail = Mail()
            # for invalideFile in d.getInvalideFiles():
            #     log(invalideFile)
            #     mail(invalideFile)


            # print("Voici TOUS les fichiers")
            # print(d.getAllFiles(),"\n")

            print("Voici TOUS les fichiers VALIDE")
            if (d.Dossier_getValideFiles()['succes']):
                ff = d.Dossier_getValideFiles()['data']
                for file in ff:
                    print("fichier VALIDE : ",file,"\n")
            else:
                print(d.Dossier_getValideFiles()['errorDict'])

            print("Voici TOUS les fichiers INVALIDE")
            if (d.Dossier_getInvalideFiles()['succes']):
                ff = d.Dossier_getInvalideFiles()['data']
                for file in ff:
                    print("fichier INVALIDE : ",file,"\n")
            else:
                print(d.Dossier_getInvalideFiles()['errorDict'])


def __init__(self, p_path, p_dossierFichier=None):
    if p_dossierFichier is None:
        dossierFichier = []
    self.dossierFichier = dossierFichier

class Dossier(object):
    def __init__(self, p_path):
        self.path = p_path
        self.dossierFichier = []
        self.tata=100
        self.responseNamedTuple = namedtuple('methodResponse', ['succes', 'data', 'errorNamedTuple'])
        #Création d'un namedTuple appelé "methodResponse"


        # Pour une réponse "True", exemple de création d'un namedTuple de type "methodResponse"
        # rTrue = self.responseNamedTuple(True,(),())

        #Création d'un namedTuple appelé "errorNamedTuple"
        self.errorNamedTuple = namedtuple('errorNamedTuple', ['logLevel','logMessage','TX_mail','mailSubject','mailMessage'])
        # Pour une réponse "False", exemple de création d'un namedTuple "et0" de type "errorNamedTuple" puis de la réponse
        # "rFalse" de type "responseNamedTuple"
        # Création d'un namedTuple de type "errorTuple"
        # et0 = self.errorNamedTuple("error","Path is NOT valid",True,"error with PATH","Path is NOT valid")
        # Création de la réponse 
        # rFalse = rT(False,"",et0)

    def Dossier_cheminEstValide(self):
    	# vérifier si le dossier self.path existe
        try:
            t = os.stat(self.path)
            print(self.path, " is a VALID path !")
            return self.responseNamedTuple(True,(),())
        except FileNotFoundError:
            et0 = self.errorNamedTuple("error","FileNotFoundError, le dossier : "+self.path+" a provoqué une erreur",
                True,"error with PATH","FileNotFoundError, le dossier : "+self.path+" a provoqué une erreur")
            return self.responseNamedTuple(False,(),et0)
        except OSError:
            et0 = self.errorNamedTuple("error","OSError, le dossier : "+self.path+" a provoqué une erreur",
                True,"error with PATH","OSError, le dossier : "+self.path+" a provoqué une erreur")
            return self.responseNamedTuple(False,(),et0)

    def Dossier_dossierEstNonVide(self):
        successTuple=(True,"",())
        if len(os.listdir(self.path)) == 0:
            et0 = self.errorNamedTuple("info","Le dossier : "+self.path+" ne contient PAS de fichiers",
                False,"Dossier vide","Le dossier : "+self.path+" ne contient PAS de fichiers")
            return self.responseNamedTuple(False,(),et0)
        return self.responseNamedTuple(True,(),())


    def Dossier_getFiles(self):
        # Placer dans la liste 'self.dossierFichier' 1 objet 'Fichier' (oFile) par fichier présent dans le dossier.
        # La présence des clés issues des liste 'fileKeys' et 'mcObligatoire' est OBLIGATOIRE.
        tempList = []
        # n = 0
        # tata = os.scandir(self.path)
        # print("Le path utilisé est ",self.path,"\n")
        # print("os.getcwd() : ",os.getcwd(),"\n")
        # print("listdir(self.path) : ",os.listdir(self.path),"\n")

        # dList = list(os.scandir(self.path))
        # print("dList : ",dList)

        # tList = list(os.scandir("d://temp"))
        # print("tList : ",tList)
        
        
        # try:
        with os.scandir(self.path) as iterator:
            for file in iterator:
                """
                file est un objet "DirEntry" voir détails ici -> https://docs.python.org/3/library/os.html#os.DirEntry
                Combiner 2 dicts 'fileDict' et 'mcObligatoireDict' pour créer le dict "d" : 
                
                fileDict = {"nom":"", "fichier":"", "extension":"", "path":"", "taille":"", 
                "errorList":[], "logLevel":"", "type":"", "invalide":"", "listeLigne":[], "stringTexte":""}

                mcObligatoireDict = {"id":0,"deleted":0,"priorId":0,"langage":"","categorie":"","souscategorie":"",
                "commentaire":"","nom":"","code":"","creationDate":"","modificationDate":"","auteur":""}

                """
                # créer une instance de classe : 
                oFileTuple = Fichier({})
                
                d = fileDict.copy()
                

                # ajouter au dict 'd' le dict 'mcObligatoireDict'
                for key, value in mcObligatoireDict.items():
                    d.update({key: value})

                # d = {}
                # for key in fileKeys:
                #     d[key] = ""
                # for key in mcObligatoire:
                #     d[key] = ""

                if not file.name.startswith('.') and file.is_file():
                    statinfo = os.stat(file)
                    
                    data =  os.path.splitext(file.name)                    
                    stat = file.stat
                    
                    timeA = statinfo[7]
                    timeM = statinfo[8]
                    timeC = statinfo[9]
                    
                    d['nom'] = file.name
                    oFileTuple.Fichier_setProperty('nom',file.name)
                    # oFileTuple.nom = file.name

                    d["fichier"] = data[0]
                    oFileTuple.Fichier_setProperty('fichier',data[0])
                    # oFileTuple.fichier = data[0]
                    # print("oFileTuple.fichier : ",oFileTuple.fichier)
                    d["extension"] = data[1]
                    oFileTuple.Fichier_setProperty('extension',data[1])
                    # oFileTuple.extension = data[1]
                    d["path"] = file.path
                    oFileTuple.Fichier_setProperty('path',file.path)
                    # oFileTuple.path = file.path
                    d["invalide"] = 0
                    oFileTuple.Fichier_setProperty('invalide',False)
                    # oFileTuple.invalide = False
                    d["taille"] = file.stat()[6]
                    oFileTuple.Fichier_setProperty('taille',file.stat()[6])
                    # oFileTuple.taille = file.stat()[6]
                    """
                    print("file.name : ",file.name)
                    print("statinfo : ",statinfo)
                    print("statinfo.st_size : ",statinfo.st_size)
                    print("statinfo[0] : ",statinfo[0])
                    print("timeA : ",timeA)
                    print("timeB : ",timeM)
                    print("timeC : ",timeC)
                    print("dir(statinfo) : ",dir(statinfo))
                    print("nom : ",nom)
                    print("data : ",data)
                    print("path : ",path)
                    print("stat : ",stat())
                    print("taille: ",taille)
                    print("tempList : ",tempList,"\n")
                    print("\n")
                    """
                    oFile = Fichier(d)
                    # self.Dossier_addFile(oFile)
                    self.Dossier_addFile(oFileTuple)
                    # print("file.name : ",file.name)
                    # print("oFileTuple.nom : ",oFileTuple.nom,"\n")
                    
            iterator.close()            
            # print("Ce dossier contient ",str(len(self.Dossier_getAllFiles()))," fichiers.\n")
            return self.responseNamedTuple(True,self.dossierFichier,())
        # except:
            print("error : with os.scandir(self.path) as iterator","\n")
            print("self.path : ",self.path,"\n")
            et0 = self.errorNamedTuple("error","erreur lecture des fichiers présents dans ce dossier : "+self.path,
                True,"Erreur dossier","erreur lecture des fichiers présents dans ce dossier : "+self.path)
            return self.responseNamedTuple(False,(),et0)

    def Dossier_addFile(self, p_oFichier):
    	# Stocker p_oFichier dans la liste 'dossierFichier' de la classe 'Dossier' 
    	# PS : la classe 'Data' n'est PLUS utilisée
    	self.dossierFichier.append(p_oFichier)

    def Dossier_getAllFiles(self):
    	# retourner TOUS les oFichier sans condition
    	return self.dossierFichier

    def Dossier_getValideFiles(self):
    	# retourner les oFichier pour valide = 1
        try:
            tempList = []
            for o in self.dossierFichier : 
                if o.invalide==0:
                    tempList.append(o)
            return self.responseNamedTuple(True,tempList,())
        except:
            et0 = self.errorNamedTuple("error","erreur lecture des objets fichiers VALIDE",
                True,"Erreur objets fichiers VALIDE","Erreur objets fichiers VALIDE")
            return self.responseNamedTuple(False,(),et0)

    def Dossier_getInvalideFiles(self):
        successTuple=(True,"",())
    	# retourner les oFichier pour valide = 0
        try:
            tempList = []
            for o in self.dossierFichier : 
                if o.invalide==1:
                    tempList.append(o)
            return self.responseNamedTuple(True,tempList,())
        except:
            et0 = self.errorNamedTuple("error","erreur lecture des objets fichiers INVALIDE",
                True,"Erreur objets fichiers INVALIDE","Erreur objets fichiers INVALIDE")
            return self.responseNamedTuple(False,(),et0)

    def Dossier_getCodeFiles(self):
        # retourner les oFichier pour type = "CODE"
        successTuple=(True,"",())
        try:
            tempList = []
            for o in self.dossierFichier : 
                if o.type=="CODE":
                    tempList.append(o)
            return self.responseNamedTuple(True,tempList,())
        except:
            et0 = self.errorNamedTuple("error","erreur lecture des objets fichiers CODE",
                True,"Erreur objets fichiers CODE","Erreur objets fichiers CODE")
            return self.responseNamedTuple(False,(),et0)

    def Dossier_getValideCodeFiles(self):
        # retourner les oFichier pour type = "CODE"
        successTuple=(True,"",())
        try:
            tempList = []
            for o in self.dossierFichier : 
                if o.type=="CODE" and o.invalide==0 :
                    tempList.append(o)
            return self.responseNamedTuple(True,tempList,())
        except:
            et0 = self.errorNamedTuple("error","erreur lecture des objets fichiers CODE VALIDE",
                True,"Erreur objets fichiers CODE VALIDE","Erreur objets fichiers CODE VALIDE")
            return self.responseNamedTuple(False,(),et0)

    def Dossier_getNonCodeFiles(self):
        # retourner les oFichier pour type = "NONCODE" (IMAGE)
        successTuple=(True,"",())
        try:
            tempList = []
            for o in self.dossierFichier : 
                if o.type=="NONCODE":
                    tempList.append(o)
            return self.responseNamedTuple(True,tempList,())
        except:
            et0 = self.errorNamedTuple("error","erreur lecture des objets fichiers NONCODE ",
                True,"Erreur objets fichiers NONCODE","Erreur objets fichiers NONCODE")
            return self.responseNamedTuple(False,(),et0)

    def Dossier_getMcFiles(self):
        # retourner les oFichier pour extension = ".MC"
        successTuple=(True,"",())
        try:
            tempList = []
            for o in self.dossierFichier : 
                if o.extension.upper()==".MC":
                    tempList.append(o)
            return self.responseNamedTuple(True,tempList,())
        except:
            et0 = self.errorNamedTuple("error","erreur lecture des objets fichiers Mot clé",
                True,"Erreur objets fichiers Mot clé","Erreur objets fichiers Mot clé")
            return self.responseNamedTuple(False,(),et0)

    def Dossier_deleteFile(self, p_valideFile): 
    	# supprimer du disque le fichier associé
    	os.remove(p_valideFile['path']) 

    def Dossier_elementIsPresent_tf(self, p_property, p_value):
        successTuple=(True,"",())
        for o in self.dossierFichier : 
            if o.getProperty(p_property)==p_value : 
                return self.responseNamedTuple(True,"",())
        et0 = self.errorNamedTuple("info","élément recheché introuvable, clé : "+p_property+", valeur : "+p_value+" NON présent",
                False,"","")
        return self.responseNamedTuple(False,(),et0)

    def Dossier_searchInList(self, p_list, p_property, p_value):
        """
        Rechercher si une clé contient une valeur dans une liste de oFile donnée (p_list). 
        p_list : une liste de oFile
        p_property : la propriété à rechercher
        p_value : la valeur pour retourner True
        """
        successTuple=(True,"",())
        for oFile in p_list : 
            if oFile.Fichier_getProperty('nom')==p_value :
                return self.responseNamedTuple(True,"",())
        et0 = self.errorNamedTuple("info","élément recheché introuvable, clé : "+p_property+", valeur : "+p_value+" NON présent",
                False,"","")
        return self.responseNamedTuple(False,(),et0)

class Fichier(object):
    def __init__(self, p_dict):
        self.dict = p_dict
        self.responseNamedTuple = namedtuple('methodResponse', ['succes', 'data', 'errorNamedTuple'])
        #Création d'un namedTuple appelé "methodResponse"


        # Pour une réponse "True", exemple de création d'un namedTuple de type "methodResponse"
        # rTrue = self.responseNamedTuple(True,(),())

        #Création d'un namedTuple appelé "errorNamedTuple"
        self.errorNamedTuple = namedtuple('errorNamedTuple', ['logLevel','logMessage','TX_mail','mailSubject','mailMessage'])
        # Pour une réponse "False", exemple de création d'un namedTuple "et0" de type "errorNamedTuple" puis de la réponse
        # "rFalse" de type "responseNamedTuple"
        # Création d'un namedTuple de type "errorTuple"
        # et0 = self.errorNamedTuple("error","Path is NOT valid",True,"error with PATH","Path is NOT valid")
        # Création de la réponse 
        # rFalse = rT(False,"",et0)
        """


        self.dict = {"nom":"", "fichier":"", "extension":"", "path":p_path, "taille":"", 
        "errorList":[], "type":"", "invalide":"", "listeLigne":"", 
        "stringTexte":"", "id":"","deleted":"","priorId":"","langage":"",
        "categorie":"","souscategorie":"","commentaire":"","code":"",
        "creationDate":"","modificationDate":"","auteur":""}
        
        # Les clés FICHIER : 
        fileKeys = ["nom", "fichier", "extension", "path", "taille", 
        "errormsg", "mc_extAssocie", "type", "invalide", "listeLigne", "stringTexte"]

        # Les clés de dictionnaire obligatoires ( et les champs du STOCKAGE dans table mySQL ) : 
        mcObligatoire = ["id","deleted","priorId","langage","categorie","souscategorie",
        "commentaire","nom","code","creationDate","modificationDate","auteur"]

        'errorList' est une liste de 'errorNamedTuple' qui contient 4 clés : 
        
        'logLevel' : pour 'error' ou 'critical' un mail est envoyé automatiquement
        'logMessage' : 
        'TX_mail' : True ou False pour envoyer un mail
        'mailSubject' : 
        'mailMessage' :
        
        'errorList' permet d'enregistrer plusieurs erreurs sur le même oFile : 
        




        "mc_extAssocie" : permet à un fichier 'mc' de spécifier l'extension de son fichier associé; 
        toutefois ceci ne sert à RIEN car il est impossible de placer 2 fichiers de même nom avec
        ext différente car le fichier mc ne peut pas être en double ! 

    
        """
        self.nom =""
        self.fichier =""
        self.extension =""
        self.path =""
        self.taille =""
        self.errorList = []
        self.type =""
        self.invalide =""
        self.listeLigne =[]
        self.stringTexte =""
        self.id =""
        self.deleted =""
        self.priorId =""
        self.langage =""
        self.categorie =""
        self.souscategorie =""
        self.commentaire =""
        self.code =""
        self.creationDate =""
        self.modificationDate =""
        self.auteur =""




        
        self.baliseObligatoire = ["langage","categorie","souscategorie","commentaire",
        "nom","code","creationDate","modificationDate","auteur"]

        self.texteFichier = ""
        self.ligneTexteFichier =[]
        self.valide = 1
        self.messageErreur = ""

        self.extensionCode = ['.C','.H','.JS','.PY','.HTML','.HTM','.TXT','.MC']
        self.extensionNonCode = ['.BMP','.JPG','.JPEG','.JPG','.PNG','.SVG','.ICO']
        self.tailleMaxiFichierCode = 5000
        self.fichierBalise = []

        


    def Fichier_setType_setInvalide(self):
        """ 4a) marquer les proprités TYPE et INVALIDE basée sur l'extension : 

            extension est                  Type        invalide
            présente dans       
            la liste ... : 

            oui, dans 'extensionCode'     CODE            0
            oui, dans 'extensionNonCode'    NONCODE          0
            non                           NON              1
        """
        if self.Fichier_verifIsCode().succes:
            self.Fichier_setProperty("type", "CODE")
            self.Fichier_setProperty("invalide", False)

        if self.Fichier_verifIsNonCode().succes:
            self.Fichier_setProperty("type", "NONCODE")
            self.Fichier_setProperty("invalide", False)
        if not (self.Fichier_verifIsNonCode().succes or self.Fichier_verifIsCode().succes):
            self.Fichier_setProperty("type", "NON")
            self.Fichier_setProperty("invalide", True)
            # print("Ce fichier avec son extension n'est PAS admis : ",self.Fichier_getProperty("nom"))
            # créer un errorNamedTuple : 
            et0 = self.errorNamedTuple("error","erreur, extension NON reconnue pour ce fichier : "+self.nom,
                True,"erreur d'extension","erreur, extension NON reconnue pour ce fichier : "+self.nom)
            self.errorList.append(et0)

    def Fichier_readText4b2_ToArray(self):
        # la clé "listeLigne" contient un array 
        try:
            self.Fichier_setProperty("listeLigne", [])
            f = open(self.Fichier_getProperty("path"), "r")
            arrayOfLines = f.readlines()
            self.listeLigne.append(arrayOfLines)
            f.close()
            return self.responseNamedTuple(True,(),())
        except:
            et0 = self.errorNamedTuple("error","erreur écriture lignes de code vers array pour le fichier "+self.Fichier_getProperty("path"),
                True,"Erreur lignes de code vers array","erreur écriture lignes de code vers array pour le fichier "+self.Fichier_getProperty("path"))
            return self.responseNamedTuple(False,(),et0)

    def Fichier_readText4b2_ToString(self):
        successTuple=(True,"",())
        a = 100
        # b.2) lire le texte et le stocker dans les clés "listeLigne" et "stringTexte" 
        # convertir le contenu du fichier en un grand string : 
        try:
            f = open(self.Fichier_getProperty("path"), "r")
            myString = f.read().replace('\n', ' ')
            f.close()

            self.Fichier_setProperty("stringTexte", myString)
            return self.responseNamedTuple(True,(),())
        except:
            et0 = self.errorNamedTuple("error","Impossible de lire le texte et le stocker dans la clé 'stringTexte' pour le fichier "+self.Fichier_getProperty("path"),
                True,"Erreur lignes de code vers array","Impossible de lire le texte et le stocker dans la clé 'stringTexte' pour le fichier "+self.Fichier_getProperty("path"))
            return self.responseNamedTuple(False,(),et0)

    def Fichier_verifTaille_tf(self):
        # Pour les extensions de type CODE ou MC : 
        successTuple=(True,"",())
        if self.taille <  self.tailleMaxiFichierCode:
            return self.responseNamedTuple(True,(),())
        else:
            et0 = self.errorNamedTuple("error","La taille du fichier "+self.nom+" est "+str(self.taille)+" elle est supérieure à la taille maximale",
                True,"Problème taille de fichier","La taille du fichier "+self.nom+" est supérieure à la taille maximale")
            return self.responseNamedTuple(False,(),et0)
            
    def Fichier_verifIsCode(self):
        # print("self.extension.upper() : ",self.extension.upper())
        if self.extension.upper() in self.extensionCode:
            return self.responseNamedTuple(True,(),())
        et0 = self.errorNamedTuple("info","Le fichier : "+self.nom+" n'est pas de type CODE",
                False,"Fichier non CODE","Le fichier : "+self.nom+" n'est pas de type CODE")
        return self.responseNamedTuple(False,(),et0)

    def Fichier_verifIsNonCode(self):
        if self.extension.upper() in self.extensionNonCode:
            return self.responseNamedTuple(True,(),())
        et0 = self.errorNamedTuple("info","Le fichier : "+self.nom+" n'est pas de type NONCODE",
                False,"Fichier non CODE","Le fichier : "+self.nom+" n'est pas de type NONCODE")
        return self.responseNamedTuple(False,(),et0)

    def Fichier_verifExtensionIsValide(self):
        if not( self.dict["extension"].upper() in self.extensionNonCode or self.dict["extension"].upper() in self.extensionCode ) : 
            p_dict={
            'logLevel':"error",
            'logMessage':"l'extension du fichier " + self.dict["nom"]+ " n'est PAS reconnue", 
            'TX_mail':True,
            'mailSubject' : "extension NON reconnue",
            'mailMessage' : "l'extension du fichier " + self.dict["nom"]+ " n'est PAS reconnue"}
            return {'succes':False, 'data':'', 'errorDict':p_dict}
        else:
            return {'succes':True, 'data':'', 'errorDict':{}}


    def Fichier_setProperty(self, p_property, p_value):
        self.__setattr__(p_property, p_value)
        
    def Fichier_getProperty(self, p_property):
        return self.__getattribute__(p_property)

    def Fichier_addErrorTuple(self, p_tuple):
        """
        p_dict est un dict à ce format : 
        p_dict={
        'logLevel':"info",
        'logMessage':"le fichier n'est PAS de type NONCODE", 
        'TX_mail':False,
        'mailSubject' : "",
        'mailMessage' : ""}
        """
        self.errorList.append(p_tuple)

    def Fichier_addErrorDict(self, p_dict):
        """
        p_dict est un dict à ce format : 
        p_dict={
        'logLevel':"info",
        'logMessage':"le fichier n'est PAS de type NONCODE", 
        'TX_mail':False,
        'mailSubject' : "",
        'mailMessage' : ""}
        """
        self.dict['errorList'].append(p_dict)

    def Fichier_verifBaliseStartObligatoirePresent(self, p_motCle):
        motCleStart = '<mccd_'+p_motCle+'>'
        nbrStart = self.Fichier_compteMc_data(motCleStart, self.stringTexte)
        if nbrStart==1:
            return self.responseNamedTuple(True,(),())
        if nbrStart==0:
            et0 = self.errorNamedTuple("error","La balise "+motCleStart+"du fichier "+self.nom+" est absente",
                True,"Balise START " +motCleStart+" est absente","La balise "+motCleStart+"du fichier "+self.nom+" est absente")
            return self.responseNamedTuple(False,(),et0)

        if nbrStart>1:
            et0 = self.errorNamedTuple("error","Le nombre de balise "+motCleStart+"du fichier "+self.nom+" est supérieur à 1",
                True,"Balise START " +motCleStart+" est multiple","Le nombre de balise "+motCleStart+"du fichier "+self.nom+" est supérieur à 1")
            return self.responseNamedTuple(False,(),et0)

    def Fichier_verifBaliseEndObligatoirePresent(self, p_motCle):
        motCleEnd = '</mccd_'+p_motCle+'>'
        nbrEnd = self.Fichier_compteMc_data(motCleEnd, self.stringTexte)
        if nbrEnd==1:
            return self.responseNamedTuple(True,(),())
        if nbrEnd==0:
            et0 = self.errorNamedTuple("error","La balise "+motCleEnd+"du fichier "+self.nom+" est absente",
                True,"Balise END " +motCleEnd+" est absente","La balise "+motCleEnd+"du fichier "+self.nom+" est absente")
            return self.responseNamedTuple(False,(),et0)
        if nbrEnd>1:
            et0 = self.errorNamedTuple("error","Le nombre de balise "+motCleEnd+"du fichier "+self.nom+" est supérieur à 1",
                True,"Balise END " +motCleEnd+" est multiple","Le nombre de balise "+motCleEnd+"du fichier "+self.nom+" est supérieur à 1")
            return self.responseNamedTuple(False,(),et0)

    def Fichier_verifDataObligatoirePresent(self, p_motCle):
        # Retourne True/False si un texte est présent entre les 2 balises 'p_motCle'
        # Créer une instance de la classe 'Regex'
        r = Regex()
        print("\nDans la méthode 'Fichier_verifDataObligatoirePresent'")
        print("self.stringTexte : ",self.stringTexte)
        
        print("self.nom NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN: ",self.nom,"\n")

        if r.Regex_textePresentEntreBalises(p_motCle, self.stringTexte).succes:
            return self.responseNamedTuple(True,(),())
        else:
            et0 = self.errorNamedTuple("error","La balise "+p_motCle+"du fichier "+self.nom+" est vide.",
                True,"Balise vide : "+p_motCle ,"La balise "+p_motCle+"du fichier "+self.nom+" est vide.")
            return self.responseNamedTuple(False,(),et0)

    def Fichier_readDataObligatoire(self, p_motCle):
        # Lire la data entre les 2 balises 'p_motCle'
        r = Regex()
        readValue = r.Regex_textePresentEntreBalises (p_motCle, self.stringTexte)
        if readValue.succes:
            # stocker la data dans la balise
            self.Fichier_setProperty(p_motCle, readValue.data)
            return self.responseNamedTuple(True,(),())
        else:
            et0 = self.errorNamedTuple("error","La balise "+p_motCle+"du fichier "+self.nom+" est vide.",
                True,"Balise vide : "+p_motCle ,"La balise "+p_motCle+"du fichier "+self.nom+" est vide.")
            return self.responseNamedTuple(False,(),et0)

    def Fichier_get_pairs(self):
        return (self.dict.items())

    def Fichier_get_keys(self):
        return (self.dict.keys())
        
    def Fichier_get_values(self):
        return (self.dict.values())

    def Fichier_mcIsPresent_tf(self, p_mc, p_text):
        """Le mot-clé est présent dans le texte ? """
        text = re.findall(p_mc,p_text)
        print("text : ",text)
        if text:
            return(True)
        return(False)
            
    def Fichier_compteMc_data(self, p_mc, p_text):
        """Retourne le nombre de mot-clé dans le texte."""
        return len(re.findall(p_mc, p_text))

	
class FichierOLD(object):
    def __init__(self, p_dict):
        self.dict = p_dict
        self.responseNamedTuple = namedtuple('methodResponse', ['succes', 'data', 'errorNamedTuple'])
        #Création d'un namedTuple appelé "methodResponse"


        # Pour une réponse "True", exemple de création d'un namedTuple de type "methodResponse"
        # rTrue = self.responseNamedTuple(True,(),())

        #Création d'un namedTuple appelé "errorNamedTuple"
        self.errorNamedTuple = namedtuple('errorNamedTuple', ['logLevel','logMessage','TX_mail','mailSubject','mailMessage'])
        # Pour une réponse "False", exemple de création d'un namedTuple "et0" de type "errorNamedTuple" puis de la réponse
        # "rFalse" de type "responseNamedTuple"
        # Création d'un namedTuple de type "errorTuple"
        # et0 = self.errorNamedTuple("error","Path is NOT valid",True,"error with PATH","Path is NOT valid")
        # Création de la réponse 
        # rFalse = rT(False,"",et0)
        """


        self.dict = {"nom":"", "fichier":"", "extension":"", "path":p_path, "taille":"", 
        "errorList":[], "type":"", "invalide":"", "listeLigne":"", 
        "stringTexte":"", "id":"","deleted":"","priorId":"","langage":"",
        "categorie":"","souscategorie":"","commentaire":"","code":"",
        "creationDate":"","modificationDate":"","auteur":""}
        
        # Les clés FICHIER : 
        fileKeys = ["nom", "fichier", "extension", "path", "taille", 
        "errormsg", "mc_extAssocie", "type", "invalide", "listeLigne", "stringTexte"]

        # Les clés de dictionnaire obligatoires ( et les champs du STOCKAGE dans table mySQL ) : 
        mcObligatoire = ["id","deleted","priorId","langage","categorie","souscategorie",
        "commentaire","nom","code","creationDate","modificationDate","auteur"]

        'errorList' est une liste de 'errorNamedTuple' qui contient 4 clés : 
        
        'logLevel' : pour 'error' ou 'critical' un mail est envoyé automatiquement
        'logMessage' : 
        'TX_mail' : True ou False pour envoyer un mail
        'mailSubject' : 
        'mailMessage' :
        
        'errorList' permet d'enregistrer plusieurs erreurs sur le même oFile : 
        




        "mc_extAssocie" : permet à un fichier 'mc' de spécifier l'extension de son fichier associé; 
        toutefois ceci ne sert à RIEN car il est impossible de placer 2 fichiers de même nom avec
        ext différente car le fichier mc ne peut pas être en double ! 

    
        """
        self.nom =""
        self.fichier =""
        self.extension =""
        self.path =""
        self.taille =""
        self.errorList = []
        self.type =""
        self.invalide =""
        self.listeLigne =""
        self.stringTexte =""
        self.id =""
        self.deleted =""
        self.priorId =""
        self.langage =""
        self.categorie =""
        self.souscategorie =""
        self.commentaire =""
        self.code =""
        self.creationDate =""
        self.modificationDate =""
        self.auteur =""




        
        self.baliseObligatoire = ["langage","categorie","souscategorie","commentaire",
        "nom","code","creationDate","modificationDate","auteur"]

        self.texteFichier = ""
        self.ligneTexteFichier =[]
        self.valide = 1
        self.messageErreur = ""

        self.extensionCode = ['.C','.H','.JS','.PY','.HTML','.HTM','.TXT','.MC']
        self.extensionNonCode = ['.BMP','.JPG','.JPEG','.JPG','.PNG','.SVG','.ICO']
        self.tailleMaxiFichierCode = 5000
        self.fichierBalise = []

        


    def Fichier_setType_setInvalide(self):
        """ 4a) marquer les proprités TYPE et INVALIDE basée sur l'extension : 

        	extension est 		           Type	       invalide
    		présente dans 		
    		la liste ... : 

            oui, dans 'extensionCode'     CODE 	          0
            oui, dans 'extensionNonCode'	NONCODE          0
    		non			                  NON 	           1
    	"""
        r = self.Fichier_verifIsCode() 
        if r.succes:
            self.Fichier_setProperty("type", "CODE")
            self.Fichier_setProperty("invalide", False)
        else:
            print("réponse de Fichier_verifIsCode() : ",r)
        if self.Fichier_verifIsNonCode().succes:
            self.Fichier_setProperty("type", "NONCODE")
            self.Fichier_setProperty("invalide", False)
        if not (self.Fichier_verifIsNonCode().succes or self.Fichier_verifIsCode().succes):
            self.Fichier_setProperty("type", "NON")
            self.Fichier_setProperty("invalide", True)
            print("Ce fichier avec son extension n'est PAS admis : ",self.Fichier_getProperty("nom"))
            # créer un errorNamedTuple : 
            et0 = self.errorNamedTuple("error","erreur, extension NON reconnue pour ce fichier : "+self.nom,
                True,"erreur d'extension","erreur, extension NON reconnue pour ce fichier : "+self.nom)
            self.errorList.append(et0)

    def Fichier_readText4b2_ToArray(self):
        # la clé "listeLigne" contient un array 
        successTuple=(True,"",())
        try:
            self.Fichier_setProperty("listeLigne", [])
            f = open(self.Fichier_getProperty("path"), "r")
            for line in f:
                self.dict['listeLigne'].append(line)
            return {'succes':True, 'data':'', 'errorDict':''}
        except:
            p_dict={
            'logLevel':"error",
            'logMessage':"Impossible d'ouvrir ce fichier : "+self.Fichier_getProperty("path"), 
            'TX_mail':True,
            'mailSubject' : "Impossible d'ouvrir ce fichier",
            'mailMessage' : "Impossible d'ouvrir ce fichier : "+self.Fichier_getProperty("path")}
            return {'succes':False, 'data':'', 'errorDict':p_dict}

    def Fichier_readText4b2_ToString(self):
        successTuple=(True,"",())
        a = 100
        # b.2) lire le texte et le stocker dans les clés "listeLigne" et "stringTexte" 
        # convertir le contenu du fichier en un grand string : 
        try:
            f = open(self.Fichier_getProperty("path"), "r")
            with f as file:
                myString = file.read().replace('\n', '')
            # print("Voici le texte du fichier ",self.Fichier_getProperty("nom")," ",myString)
            self.Fichier_setProperty("stringTexte", myString)
            return {'succes':True, 'data':'', 'errorDict':''}
        except:
            p_dict={
            'logLevel':"error",
            'logMessage':"Impossible de lire le texte et le stocker dans la clé 'stringTexte'", 
            'TX_mail':True,
            'mailSubject' : "Impossible de lire le texte",
            'mailMessage' : "Impossible de lire le texte et le stocker dans la clé 'stringTexte'"}
            return {'succes':False, 'data':'', 'errorDict':p_dict}

    def Fichier_verifTaille_tf(self):
        # Pour les extensions de type CODE ou MC : 
        successTuple=(True,"",())
        if self.dict["taille"] <  self.tailleMaxiFichierCode:
            return {'succes':True, 'data':'', 'errorDict':''}
        else:
            p_dict={
            'logLevel':"error",
            'logMessage':"La taille du fichier "+self.dict["nom"]+" est supérieure à la taille maximale", 
            'TX_mail':True,
            'mailSubject' : "Problème taille de fichier",
            'mailMessage' : "La taille du fichier "+self.dict["nom"]+" est supérieure à la taille maximale"}
            return {'succes':False, 'data':'', 'errorDict':p_dict}
            
    def Fichier_verifIsCode(self):
        if self.extension.upper() in self.extensionCode:
            return self.responseNamedTuple(True,(),())
        et0 = self.errorNamedTuple("info","Le fichier : "+self.nom+" n'est pas de type CODE",
                False,"Fichier non CODE","Le fichier : "+self.nom+" n'est pas de type CODE")
        return self.responseNamedTuple(False,(),et0)

    def Fichier_verifIsNonCode(self):
        if self.extension.upper() in self.extensionNonCode:
            return self.responseNamedTuple(True,(),())
        et0 = self.errorNamedTuple("info","Le fichier : "+self.nom+" n'est pas de type NONCODE",
                False,"Fichier non CODE","Le fichier : "+self.nom+" n'est pas de type NONCODE")
        return self.responseNamedTuple(False,(),et0)

    def Fichier_verifExtensionIsValide(self):
        if not( self.dict["extension"].upper() in self.extensionNonCode or self.dict["extension"].upper() in self.extensionCode ) : 
            p_dict={
            'logLevel':"error",
            'logMessage':"l'extension du fichier " + self.dict["nom"]+ " n'est PAS reconnue", 
            'TX_mail':True,
            'mailSubject' : "extension NON reconnue",
            'mailMessage' : "l'extension du fichier " + self.dict["nom"]+ " n'est PAS reconnue"}
            return {'succes':False, 'data':'', 'errorDict':p_dict}
        else:
            return {'succes':True, 'data':'', 'errorDict':{}}

    def Fichier_getProperty (self, p_property):
    	return self.p_property


    def Fichier_setProperty(self, p_property, p_value):
    	self.p_property=p_value

    def Fichier_addErrorTuple(self, p_tuple):
        """
        p_dict est un dict à ce format : 
        p_dict={
        'logLevel':"info",
        'logMessage':"le fichier n'est PAS de type NONCODE", 
        'TX_mail':False,
        'mailSubject' : "",
        'mailMessage' : ""}
        """
        self.errorList.append(p_tuple)

    def Fichier_addErrorDict(self, p_dict):
        """
        p_dict est un dict à ce format : 
        p_dict={
        'logLevel':"info",
        'logMessage':"le fichier n'est PAS de type NONCODE", 
        'TX_mail':False,
        'mailSubject' : "",
        'mailMessage' : ""}
        """
        self.dict['errorList'].append(p_dict)

    def Fichier_verifBaliseStartObligatoirePresent(self, p_motCle):
        motCleStart = '<mccd_'+p_motCle+'>'
        nbrStart = self.Fichier_compteMc_data(motCleStart, self.dict["stringTexte"])
        if nbrStart==1:
            return {'succes':True, 'data':'', 'errorDict':''}
        if nbrStart==0:
            p_dict={
            'logLevel':"error",
            'logMessage':"La balise "+motCleStart+"du fichier "+self.dict["nom"]+" est absente", 
            'TX_mail':True,
            'mailSubject' : "Balise manquante",
            'mailMessage' : "La balise "+motCleStart+"du fichier "+self.dict["nom"]+" est absente"}
            return {'succes':False, 'data':'', 'errorDict':p_dict}
        if nbrStart>1:
            p_dict={
            'logLevel':"error",
            'logMessage':"Le nombre de balise "+motCleStart+"du fichier "+self.dict["nom"]+" est supérieure à 1", 
            'TX_mail':True,
            'mailSubject' : "Balise multiple",
            'mailMessage' : "Le nombre de balise "+motCleStart+"du fichier "+self.dict["nom"]+" est supérieure à 1", }
            return {'succes':False, 'data':'', 'errorDict':p_dict}

    def Fichier_verifBaliseEndObligatoirePresent(self, p_motCle):
        motCleEnd = '</mccd_'+p_motCle+'>'
        nbrEnd = self.Fichier_compteMc_data(motCleEnd, self.dict["stringTexte"])
        if nbrEnd==1:
            return {'succes':True, 'data':'', 'errorDict':''}
        if nbrEnd==0:
            p_dict={
            'logLevel':"error",
            'logMessage':"La balise "+motCleEnd+"du fichier "+self.dict["nom"]+" est absente", 
            'TX_mail':True,
            'mailSubject' : "Balise manquante",
            'mailMessage' : "La balise "+motCleEnd+"du fichier "+self.dict["nom"]+" est absente"}
            return {'succes':False, 'data':'', 'errorDict':p_dict}
        if nbrEnd>1:
            p_dict={
            'logLevel':"error",
            'logMessage':"Le nombre de balise "+motCleEnd+"du fichier "+self.dict["nom"]+" est supérieure à 1", 
            'TX_mail':True,
            'mailSubject' : "Balise multiple",
            'mailMessage' : "Le nombre de balise "+motCleEnd+"du fichier "+self.dict["nom"]+" est supérieure à 1", }
            return {'succes':False, 'data':'', 'errorDict':p_dict}

    def Fichier_verifDataObligatoirePresent(self, p_motCle):
        # Retourne True/False si un texte est présent entre les 2 balises 'p_motCle'
        # Créer une instance de la classe 'Regex'
        r = Regex()
        # print("self.dict['stringTexte'] : ",self.dict['stringTexte'])
        if r.Regex_textePresentEntreBalises(p_motCle, self.dict["stringTexte"])['succes']:
            return {'succes':True, 'data':'', 'errorDict':{}}
        else:
            p_dict={
            'logLevel':"error",
            'logMessage':"La balise "+p_motCle+"du fichier "+self.dict["nom"]+" est vide.", 
            'TX_mail':True,
            'mailSubject' : "Balise vide",
            'mailMessage' : "La balise "+p_motCle+"du fichier "+self.dict["nom"]+" est vide." }
            return {'succes':False, 'data':'', 'errorDict':p_dict}


    def Fichier_readDataObligatoire(self, p_motCle):
        # Retourne True/False si un texte est présent entre les 2 balises 'p_motCle'
        # Créer une instance de la classe 'Regex'
        r = Regex()
        readValue = r.Regex_texteEntreBalises (p_motCle, self.dict["stringTexte"])
        if readValue['succes']:
            # stocker la data dans la balise
            self.Fichier_setProperty(p_motCle, readValue['data'])
            return {'succes':True, 'data':'', 'errorDict':{}}
        else:
            p_dict={
            'logLevel':"error",
            'logMessage':"Une erreur lors de la lecture de data de la balise "+p_motCle+"du fichier "+self.dict["nom"]+" s'est produite.", 
            'TX_mail':True,
            'mailSubject' : "Erreur lors de la lecture de data",
            'mailMessage' : "Une erreur lors de la lecture de data de la balise "+p_motCle+"du fichier "+self.dict["nom"]+" s'est produite." }
            return {'succes':False, 'data':'', 'errorDict':p_dict}







        if r.Regex_textePresentEntreBalises(p_motCle, self.dict["stringTexte"])['succes']:
            return {'succes':True, 'data':'', 'errorDict':{}}
        else:
            p_dict={
            'logLevel':"error",
            'logMessage':"La balise "+p_motCle+"du fichier "+self.dict["nom"]+" est vide.", 
            'TX_mail':True,
            'mailSubject' : "Balise vide",
            'mailMessage' : "La balise "+p_motCle+"du fichier "+self.dict["nom"]+" est vide." }





    def Fichier_get_pairs(self):
    	return (self.dict.items())

    def Fichier_get_keys(self):
    	return (self.dict.keys())
        
    def Fichier_get_values(self):
    	return (self.dict.values())

    def Fichier_mcIsPresent_tf(self, p_mc, p_text):
        """Le mot-clé est présent dans le texte ? """
        text = re.findall(p_mc,p_text)
        print("text : ",text)
        if text:
            return(True)
        return(False)
            
    def Fichier_compteMc_data(self, p_mc, p_text):
        """Retourne le nombre de mot-clé dans le texte."""
        return len(re.findall(p_mc, p_text))

class Indicateur(object):
    def __init__(self, p_indicateurInitValue):
        """
        p_indicateurInitValue : la valeur initiale

        Cette classe sert à vérifier qu'une succession d'opération qui 
        retournent True et False on bien retourné les valeurs escomptées.

        Exemples d'utilisations : 
        1) Toutes les opérations doivent être à True
        La valeur initiale est mise à True
        on utilise le mode SERIE avec la méthode 'indicateur_serie'

        2) Toutes les opérations doivent être à False
        La valeur initiale est mise à False
        on utilise le mode PARALLELE avec la méthode 'indicateur_para'
        si une seule valeur est à True le résultat sera True

        3) Au moins une valeur doit être à True
        La valeur initiale est mise à False
        on utilise le mode PARALLELE avec la méthode 'indicateur_para'

        4) Au moins une valeur doit être à False
        La valeur initiale est mise à True
        on utilise le mode SERIE avec la méthode 'indicateur_serie'
        si une seule valeur est à False le résultat sera False
        """
        self.indicateur = p_indicateurInitValue

    def Indicateur_indicateur_serie( self, p_value):
        # Si True est recherché alors toutes les 
        # valeurs doivent être les même que p_valueInit=1
        # print("Dans la classe, valeur passée à indicateur_serie : ",p_value)
        # print("self.indicateur : ",self.indicateur)
        self.indicateur = self.indicateur * p_value
        # print("Dans la classe, APRES self.indicateur : ",self.indicateur,"\n")

    def Indicateur_indicateur_para( self, p_value):
        # Si au moins un True est recherché alors au moins
        # l'une des valeurs doit être à True
        self.indicateur = self.indicateur | p_value

    def Indicateur_getIndicateur(self):
        return self.indicateur

    def Indicateur_setIndicateur(self, p_value):
        self.indicateur = p_value

class Regex(object):
    def __init__(self):
        self.regex = ""
        self.errorNamedTuple = namedtuple('errorNamedTuple', ['logLevel','logMessage','TX_mail','mailSubject','mailMessage'])
        self.responseNamedTuple = namedtuple('methodResponse', ['succes', 'data', 'errorNamedTuple'])
    def Regex_textIsPresent_tf(self, p_text): # OK 30/11 11h51
        # 'p_text' est le texte à parcourir pour y rechercher une réponse. 
        # répondre T/F si le texte de la regex ('self.regex') est présent/absent.
        # self.regex est utilisé
        text = re.findall(self.regex,p_text)
        print("text : ",text)
        if text:
            return(True)
        return(False)

    def Regex_countWords(self, p_text): # OK 30/11 13h38
        # Compter le nbr de mots dans le texte 'p_text'
        # self.regex n'est PAS utilisé
        # 'p_text' est un string
        return len(re.findall("\s+",p_text))

    def Regex_countLines(self, p_text): # OK 30/11 13h49
        # compter les lignes dans le texte
        # self.regex n'est PAS utilisé
        tr = re.findall("\n",p_text)
        return len(tr)

    def Regex_countLetters(self, p_text): # OK 30/11 13h47
        # compter les lettres dans le texte
        # self.regex n'est PAS utilisé
        tr = re.findall(r".",p_text)
        return len(tr)
        
    def Regex_replaceText(self, p_text, p_replacementText): # OK 30/11 12h05
        # 'self.regex' est utilisée pour rechercher du texte dans 'p_text'
        # qui est remplacé par le texte 'p_replacementText'
        # To replace a string in Python, the regex sub() method is used.
        # 'flags' info : https://docs.python.org/3/library/re.html#flags
        return re.sub(self.regex,p_replacementText, p_text, count=0, flags=0)

    def Regex_createBaliseStart(self, p_text):
        return "<mccd_"+p_text+">"

    def Regex_createBaliseEnd(self, p_text):
        return "</mccd_"+p_text+">"

    def Regex_textePresentEntreBalises(self, p_balise, p_text): # OK 30/11 12h47
    	# Vérifier si du texte est présent entre les balises données. 
        # Exemple p_balise='categorie' : <mccd_categorie> texte à retourner </mccd_categorie>
        # 'self.regex' n'est pas à renseigner
        # p_text le texte qui est parcouru pour recherche

        # créer les deux balises : 
        start_balise = "<mccd_"+p_balise+">"
        end_balise = "</mccd_"+p_balise+">"
        # self.regex = "(?<=" + start_balise + ")(.*)(?=" +end_balise + ")"
        regex0 = "(?<=" + start_balise + ")(.*)(?=" +end_balise + ")"
        tr = re.findall(regex0,p_text)
        print("Voici le résultat de la recherche : ",tr,"\n")
        if len(tr)>0:
            if len(tr[0])>4:
                return self.responseNamedTuple(True,(tr[0]),())
        else:
            msg = "Erreur lecture entre les balises "+start_balise+" et "+end_balise
            print("Aucune DATA +++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            et0 = self.errorNamedTuple("error","Dans le fichier ... le texte de la balise "+start_balise+" est absent",
                True,"Texte absent dans balise","Dans le fichier ... le texte de la balise "+start_balise+" est absent")
            return self.responseNamedTuple(False,(),et0)

    def Regex_texteEntreBalises (self, p_balise, p_text): # OK 30/11 12h47
        # retourner les texte compris entre deux balises 'mccd'. 
        # Exemple p_balise='categorie' : <mccd_categorie> texte à retourner </mccd_categorie>
        # 'self.regex' n'est pas à renseigner
        # p_text le texte qui est parcouru pour recherche

        # créer les deux balises : 
        start_balise = "<mccd_"+p_balise+">"
        end_balise = "</mccd_"+p_balise+">"
        try:
            self.regex = "(?<=" + start_balise + ")(.*)(?=" +end_balise + ")"
            tr = re.findall(self.regex,p_text)
            # vérifier si tr[0] contient du texte (NON vide)
            return self.responseNamedTuple(True,(tr[0]),())
        except:
            msg = "Texte absent entre les balises "+start_balise+" et "+end_balise
            et0 = self.errorNamedTuple("error",msg,
                True,"Texte absent entre balises "+p_balise,msg)
            return self.responseNamedTuple(False,(),et0)

    def Regex_compterOccurences(self, p_text): # OK 30/11 12h52
        # Compter les occurences de self.regex dans le texte en 'p_text'
        # 'self.regex' est utilisée
        tr = re.findall(self.regex,p_text)
        return len(tr)

    def Regex_extractText(self, p_text): # OK 30/11 12h56
        # 'self.regex' est utilisée pour extraire toutes les occurences dans le texte 'p_text'
        # finditer : return re.finditer(self.regex,p_text)
        return re.findall(self.regex,p_text)
        
    def Regex_deleteText(self, p_text): # OK 30/11 12h30
        # 'self.regex' est utilisée pour effacer toutes les occurences dans le texte 'p_text'
        return re.sub(self.regex,"", p_text, count=0, flags=0)

class Balise(object):
    def __init__(self):
        """
        Les paramètres : PPPPPPPPPPPPPPPPPPPPPPPPPPPPP

        # Les preffixes (ajoutés aux méthodes) utilisés : FFFFFFFFFFFFFFFFFFFFF
        Ils sont 1 : 
        errorIfNot_ : une autre méthode a retourné False. Si l'on souhaite en avoir la raison 
        on appelle cette méthode. 

        # Les suffixes (ajoutés aux méthodes) utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'errorDict':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        Exemple de valeurs retournées par TOUTES les méthodes : 
        return {'succes':True, 'data':'', 'errorDict':'', 'logLevel':''} 
        return {'succes':False, 'data':'', 'errorDict':'FileNotFoundError', 'logLevel':'error'}


        """
        self.baliseObligatoirePresent_tf = False
        self.dataObligatoirePresent_tf = False
        self.data = ""

        

    def getWorkDir_data(self):
        return os.getcwd()

class Log(object):
    def __init__(self):
        """
        Ecriture dans le fichier de LOG
        
        A installer : 
        import logging
        import datetime
        import locale
        import time
        locale.setlocale(locale.LC_TIME, "fr_FR")

        
        Quel est le fichier utilisé pour écrire tous les LOG ? 
        app.config['LOG_FILE']
        

        # Les suffixes (ajoutés aux méthodes) utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'errorDict':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        # Utilisation : UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
        # création d'une instance de la classe : 
        # l = Log('example.log')

        # Enregistrement d'un LOG : 
        # l.storeLogMessage("This is a DEBUG message ...","DEBUG")


        """
        self.logFile = app.config['LOG_FILE']
        # Configuration du système des LOG : 
        logging.basicConfig(filename=self.logFile, encoding='utf-8', 
            format='%(levelname)s:%(message)s', level=logging.DEBUG)
        # level=logging.DEBUG
        # le niveau minimun du message pour être écrit dans le fichier de LOG est DEBUG

    def storeLogMessage(self, p_level, p_message):
        # p_level parmi : DEBUG,INFO,WARNING, ERROR, CRITICAL
        # p_message : le message a enregistrer
        # La date est enregistrée automatiquement

        # now = datetime.datetime.today()
        # today_year = datetime.datetime.today().year
        # today_month = datetime.datetime.today().month
        # today_day = datetime.datetime.today().day

        # today_hour = datetime.datetime.today().hour
        # today_minute = datetime.datetime.today().minute
        # today_second = datetime.datetime.today().second

        # # Les dates sont en FR grâce à cette ligne placée plus haut : 
        # # locale.setlocale(locale.LC_TIME, "fr_FR")

        # dateHeureCmde = datetime.datetime(today_year,today_month,today_day,
        # today_hour,today_minute,today_second,0)
        # dateEpoch = int(time.time())
        dateLog = time.strftime("%d %B %Y %A, %H:%M:%S")

        if p_level.upper()=="DEBUG": #level = 10
            logging.debug(dateLog+' '+p_message)
  
        elif p_level.upper()=="INFO": #level = 20
            logging.info(dateLog+' '+p_message)

        elif p_level.upper()=="WARNING": #level = 30
            logging.warning(dateLog+' '+p_message)

        elif p_level.upper()=="ERROR": #level = 40
            logging.error(dateLog+' '+p_message)

        elif p_level.upper()=="CRITICAL": #level = 50
            logging.critical(dateLog+' '+p_message)

        else:
            msg = "LOGGING ERROR : Le niveau de LOG utilisé " +p_level.upper()+" est inconnu. Vous devez utiliser un niveau parmi : DEBUG, INFO, WARNING, ERROR, CRITICAL"
            logging.critical(dateLog+' '+msg)
            msg = "LOGGING ERROR : Le message à enregistrer était : "+p_message
            logging.critical(dateLog+' '+msg)
            p_dict={
            'logLevel':"info",
            'logMessage':"LOGGING ERROR", 
            'TX_mail':True,
            'mailSubject' : "LOGGING ERROR",
            'mailMessage' : "LOGGING ERROR : Le niveau de LOG utilisé " +p_level.upper()+" est inconnu. Vous devez utiliser un niveau parmi : DEBUG, INFO, WARNING, ERROR, CRITICAL"}
            return {'succes':False, 'data':'', 'errorDict':p_dict}                        
        return ({'succes':True, 'errorDict':'LOG effectué', 'data':""})
    def logFile_data(self):
        """ Retourne LE NOM du fichier des LOG. 
        Il pourra ainsi être utilisé par une instance de la classe 'Fichier'
        pour en afficher ses lignes. """
        return self.logFile


class MailSender(object):
    def __init__(self):
        """
        La classe de gestion des E-MAILS ! 

        ATTENTION : l'envoi d'un mail est LONG. En JS on utilise une 'promise' pour les 
        actions qui durent. 
        Qu'en est-il ici en python ? Le serveur attend indéfiniment  jusqu'au retour 
        de l'app 'flask-mail' ? 

        Qu'en est-il de la gestion des 'EXCEPTIONS' ? 
        Si le serveur de mails refuse la connexion, si un p_ de config est faux , etc ...
        'flask-mail' utilise 'smtplib' qui liste ses exceptions ici : 
        https://docs.python.org/3/library/smtplib.html

        à installer : 
        from flask_mail import Message, Mail
        import smtplib
        mail = Mail(app)

        # Les paramètres : PPPPPPPPPPPPPPPPPPPPPPPPPPPPP

        'p_configMailFile' contient les infos pour paramétrer l'envoi des E-MAILS. 
        J'utilise une extension *.cfg ex : 'configFree.cfg'
        exemple du contenu : 
        MAIL_SERVER = 'smtp.free.fr'
        MAIL_PORT = 465
        MAIL_USE_TLS = False
        MAIL_USE_SSL = True

        MAIL_USERNAME = 'newsolar@free.fr'
        MAIL_PASSWORD = '2018?Sugar'

        # Les suffixes (ajoutés aux méthodes) utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'errorDict':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        """

        

        self.a = 100

    def sendMail(self, p_subject, p_message, p_type, p_ListeDestinataires=mailDestinataires):
        # p_subject : l'entête du mail, ex : "Une erreur de LOG"
        # p_message : ex : "Le LOG n'est PAS conforme à la norme ..."
        # p_ListeDestinataires est un ARRAY de string des e-mails des destinataires
        # p_type indique si le corps du mail est constitué de code HTML ou pas
        # seules 2 valeurs sont acceptées : 'html' ou TOUT autre string comme 'texte'

        #mailDestinataires=["commercial01@bio220.fr","christian.doriath@free.fr"]
        destinataires = ', '.join(p_ListeDestinataires)

        msg= Message(subject=p_object, sender="serveur@codebase.fr",
        recipients=p_ListeDestinataires) 

        msg.body = p_message
        if p_type.upper() == 'HTML' :
            msg.html = render_template('MyTable.html')

        try:
            mail.send(msg)
            msg = 'e-mail envoyé à ' + destinataires +" à " + str(datetime.datetime.now())
            return ({'succes':True, 'errorDict':msg, 'data':""})                  

        except smtplib.SMTPAuthenticationError:
            print(" smtplib.SMTPAuthenticationError")
            p_dict={
            'logLevel':"error",
            'logMessage':"Impossible d'envoyer le mail car une erreur 'smtplib.SMTPAuthenticationError' s'est produite.", 
            'TX_mail':False,
            'mailSubject' : "",
            'mailMessage' : ""}
            return {'succes':False, 'data':'', 'errorDict':p_dict}
        except smtplib.SMTPException:
            print(" smtplib.SMTPException")
            p_dict={
            'logLevel':"error",
            'logMessage':"Impossible d'envoyer le mail car une erreur 'smtplib.SMTPException' s'est produite.", 
            'TX_mail':False,
            'mailSubject' : "",
            'mailMessage' : ""}
            return {'succes':False, 'data':'', 'errorDict':p_dict}