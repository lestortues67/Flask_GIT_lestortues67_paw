"""
Date : 21/11/2022
Auteur : Christian Doriath
Dossier : /Python39/MesDEv/Flask/Flask_codebase2023
Fichier : app.py
Description : name space tests
"""

from starter import * 

class Main(object):
    def __init__(self, p_path):
        """
    	Dans cette classe TOUT se passe dans __init__

    	1) Demander à la classe 'Dossier' une liste de dict 
    	( 1 dict par fichier présent dans le dossier)

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

        if not (d.pathIsValid_tf()):
            msg = d.pathIsValid_data()
            print(msg)
            exit()
        else:
            """
            # le path est valide
            # 1) Demander à la classe 'Dossier' une liste de dict 
            # ( 1 dict par fichier présent dans le dossier)
            """
            listOfFiles = d.getFiles()
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
                d.addFile(oFichier)
                """
                # 4) Parcourir tous les oFichier pour :
        		a) Définir les valeurs pour 'type' et 'invalide' selon ce tableau : 

        		extension est 		Type	invalide
        		présente dans 		
        		la liste : 

        		extensionCode 		CODE 	0
        		extensionNonCode	NONCODE 0
        		aucune			NON 	1

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

            for oFile in d.getAllFiles():
                # 4a) marquer les proprités TYPE et INVALIDE basée sur l'extension
                oFile.setTypeInvalide()

                typeOfFile = oFile.getProperty("type") # "CODE", "NONCODE")

                if (typeOfFile == "CODE") :
                    # créer une instance de la classe 'Indicateur' qui est utile quand 
                    # plusieurs vérif doivent retourner True pour une validation
                    self.i = Indicateur(1)

                    # 4b.1) fichier CODE/MC sa taille < 5000 def verifTailleFichier(self):
                    # vérifier l'extension du fichier, est-elle acceptable ? 

                    if(self.i.getIndicateur()):
                        if not (oFile.verifTaille_tf()):
                            self.i.indicateur_serie(False)
                            oFile.setProperty("errormsg",oFile.verifTaille_data())
                        else:
                            self.i.indicateur_serie(True)

                    # 4b.2) lire le texte et le stocker dans les clés "listeLigne" et "stringTexte"
                    if(self.i.getIndicateur()):   
                        if not(oFile.readText4b2_ToArray_tf()):  
                            self.i.indicateur_serie(False)
                            messageErreur = oFile.readText4b2_ToArray_data()   
                            oFile.setProperty("errormsg",messageErreur)
                        if not(oFile.readText4b2_ToString_tf()):  
                            self.i.indicateur_serie(False)
                            messageErreur = oFile.readText4b2_ToString_data()
                            oFile.setProperty("errormsg",messageErreur)

                    # 4b.3) rechercher la présence de TOUTES les balises obligatoires
                    for motCleBalise in mcObligatoire:
                        # On utilise et parcours la liste "mcObligatoire"
                        if(self.i.getIndicateur()):
                            if not(oFile.verifBaliseObligatoirePresent_tf(motCleBalise)):  
                                self.i.indicateur_serie(False)
                                messageErreur = oFile.verifBaliseObligatoirePresent_data(motCleBalise)
                                oFile.setProperty("errormsg",messageErreur)

                    # 4b.4) lire le contenu des balises obligatoires
                    r = Regex() # 4b4) lire le contenu des balises obligatoires
                    for motCleBalise in mcObligatoire:
                        if(self.i.getIndicateur()):  
                            if not (r.texteEntreBalises_tf(motCleBalise, oFile.getProperty("stringTexte")) ):
                                self.i.indicateur_serie(False)
                                messageErreur = self.textePresentEntreBalises_data(motCleBalise)
                                oFile.setProperty("errormsg",messageErreur)
                            else: 
                                # stocker la data 
                                texte = oFile.texteEntreBalises (motCleBalise, oFile.getProperty("stringTexte"))
                                oFile.setProperty(motCleBalise, texte)
                    # 4b.5) si fichier MC recherche du fichier IMAGE associé

                else: # "NONCODE"
                    self.i = Indicateur(1)
                    # 4c.1) rechercher les fichiers IMAGE sans fichier MC def fichierMcManquant(self):
                    fichier = oFile.getProperty("fichier")

                    if(self.i.getIndicateur()):
                        elementIsPresent_tf(self, p_property, p_value)
                        a = 100

                    # 4c.2) rechercher les fichiers MC sans fichier IMAGE def fichierImageManquant(self):
                    if(self.i.getIndicateur()):
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
            
            ff = d.getValideFiles()
            for file in ff:
                print("fichier VALIDE : ",file,"\n")

            print("Voici TOUS les fichiers INVALIDE")
            ff = d.getInvalideFiles()
            for file in ff:
                print("fichier INVALIDE : ",file,"\n")

class Dossier(object):
    def __init__(self, p_path):
    	"""
    	Vérifier le 'PATH'. Est-il valide ? 
    	Créer un objet fichier pour chaque fichier présent dans le 'path'

	
    	"""
    	self.path = p_path
    	self.dossierFichier = []


    def pathIsValid_tf(self):
    	# vérifier si le dossier self.path existe
        try:
            t = os.stat(self.path)
            # print("os.stat(self.path) : ",os.stat(self.path))
            print(self.path, " is a VALID path !")
            return True
        except FileNotFoundError:
            # print("FileNotFoundError \n")
            return False
        except OSError:
            # print("OSError \n")
            return False

    def pathIsValid_data(self):
        # la méthode 'pathIsValid_tf()' a retourné False. 
        # Ici l'information sur la raison du False.
        try:
            t = os.stat(self.path)
            return " is a VALID path !"
        except FileNotFoundError:
            return "FileNotFoundError"
        except OSError:
            return "OSError"

    def getFiles(self):
        # retourner une liste de dict ( 1 dict par fichier présent dans le dossier)
        # enregistrer les datas sur TOUS les fichiers présents dans un dict 
        # avec les clés issues des liste 'fileKeys' et 'mcObligatoire'
        tempList = []
        # n = 0
        with os.scandir(self.path) as iterator:
            for file in iterator:
                # création du dict avec les clés données dans 
                # les listes 'fileKeys' et  et 'mcObligatoire'
                d = {}
                for key in fileKeys:
                    d[key] = ""
                for key in mcObligatoire:
                    d[key] = ""
                # n = n + 1 
                # print("N° passage : ",n)
                # type(file) : De quel 'type' est file ? 
                # Réponse :  <class 'nt.ScandirIterator'>

                if not file.name.startswith('.') and file.is_file():
                    statinfo = os.stat(file)
                    
                    data =  os.path.splitext(file.name)
                    nom = file.name
                    fichier = data[0]
                    extension = data[1]
                    
                    path = file.path
                    
                    stat = file.stat
                    
                    taille = file.stat()[6]
                    timeA = statinfo[7]
                    timeM = statinfo[8]
                    timeC = statinfo[9]
                    
                    d['nom'] = file.name
                    d["fichier"] = fichier
                    d["extension"] = extension
                    d["path"] = path
                    d["invalide"] = 0
                    d["taille"] = taille
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
                    tempList.append(d)
                    
                    
        iterator.close()
        print("Ce dossier contient ",str(len(tempList))," fichiers.\n")
        return tempList

    def addFile(self, p_oFichier):
    	# Stocker p_oFichier dans la liste 'dossierFichier' de la classe 'Dossier' 
    	# PS : la classe 'Data' n'est PLUS utilisée
    	self.dossierFichier.append(p_oFichier)

    def getAllFiles(self):
    	# retourner TOUS les oFichier sans condition
    	return self.dossierFichier

    def getValideFiles(self):
    	# retourner les oFichier pour valide = 1
    	tempList = []
    	for o in self.dossierFichier : 
    		if o.dict['invalide']==0:
    			tempList.append({'nom':o.dict['nom'],'fichier':o.dict['fichier'],"errormsg":o.dict["errormsg"]})
    	return tempList

    def getInvalideFiles(self):
    	# retourner les oFichier pour valide = 0
    	tempList = []
    	for o in self.dossierFichier : 
    		if o.dict['invalide']==1:
    			tempList.append(o.dict['nom'])
    	return tempList    	

    def deleteFile(self, p_valideFile):
    	# supprimer du disque le fichier associé
    	os.remove(p_valideFile['path']) 

    def elementIsPresent_tf(self, p_property, p_value):
        for o in self.dossierFichier : 
            if o.dict[p_property]==p_value:
                return True
        return False





	
class Fichier(object):
    def __init__(self, p_dict):
        """
        # Les clés FICHIER : 
        fileKeys = ["nom", "fichier", "extension", "path", "taille", 
        "errormsg", "mc_extAssocie", "type", "invalide", "listeLigne", "stringTexte"]

        "mc_extAssocie" : permet à un fichier 'mc' de spécifier l'extension de son fichier associé; 
        toutefois ceci ne sert à RIEN car il est impossible de placer 2 fichiers de même nom avec
        ext différente car le fichier mc ne peut pas être en double ! 

        # Les clés de dictionnaire obligatoires ( et les champs du STOCKAGE dans table mySQL ) : 
        mcObligatoire = ["id","deleted","priorId","langage","categorie","souscategorie",
        "commentaire","nom","code","creationDate","modificationDate","auteur"]


        """
        self.dict = p_dict
        """
        self.dict = {"nom":"", "fichier":"", "extension":"", "path":p_path, "taille":"", 
        "errormsg":"", "mc_extAssocie":"", "type":"", "invalide":"", "listeLigne":"", 
        "stringTexte":"", "id":"","deleted":"","priorId":"","langage":"",
        "categorie":"","souscategorie":"","commentaire":"","nom":"","code":"",
        "creationDate":"","modificationDate":"","auteur":""}
        """
        self.baliseObligatoire = ["langage","categorie","souscategorie","commentaire",
        "nom","code","creationDate","modificationDate","auteur"]

        self.texteFichier = ""
        self.ligneTexteFichier =[]
        self.valide = 1
        self.messageErreur = ""

        self.extensionCode = ['.C','.H','.JS','.PY','.HTML','.HTM','.TXT','.MC']
        self.extensionNonCode = ['.BMP','.JPG','.JPEG','.JPG','.PNG','.SVG','.ICO']
        self.tailleMaxiFichierCode = 5000
        self.balises = []


    def setTypeInvalide(self):

    	""" 4a) marquer les proprités TYPE et INVALIDE basée sur l'extension

    		extension est 		Type	invalide
    		présente dans 		
    		la liste : 

    		extensionCode 		CODE 	0
    		extensionNonCode	NONCODE 0
    		aucune			NON 	1
    	"""
    	if self.verifIsCode_tf():
    		self.setProperty("type", "CODE")
    		self.setProperty("invalide", False)
    	if self.verifIsNonCode_tf():
    		self.setProperty("type", "NONCODE")
    		self.setProperty("invalide", False)
    	if not (self.verifIsNonCode_tf() or self.verifIsCode_tf()):
    		self.setProperty("type", "NON")
    		self.setProperty("invalide", True)
    		self.setProperty("errormsg", "extension de fichier NON acceptée")

    def readText4b2_ToArray_tf(self):
        # la clé "listeLigne" contient un array 
        self.setProperty("listeLigne", [])
        f = open(self.getProperty("path"), "r")
        for line in f:
            self.dict['listeLigne'].append(line)
        return True

    def readText4b2_ToArray_data(self):
    	return ("erreur durant la lecture du fichier pour en extraire un array des lignes.")

    def readText4b2_ToString_tf(self):
        a = 100
        # b.2) lire le texte et le stocker dans les clés "listeLigne" et "stringTexte" 
        # convertir le contenu du fichier en un grand string : 
        f = open(self.getProperty("path"), "r")
        with f as file:
            myString = file.read().replace('\n', '')
        self.setProperty("stringTexte", myString)
        return True

    def readText4b2_ToString_data(self):
    	return ("erreur durant la lecture du fichier pour en extraire un seul string.")

    def verifTaille_tf(self):
        # Pour les extensions de type CODE ou MC : 
        if (self.verifIsCode_tf()):
            if self.dict["taille"] <  self.tailleMaxiFichierCode:
                return True
            else:
                return False
        else:
            return True
            

    def verifTaille_data(self):
        return "La taille du fichier est supérieure à la taille maximale."



    def verifIsCode_tf(self):
    	if self.dict["extension"].upper() in self.extensionCode:
    		return True
    	return False

    def verifIsNonCode_tf(self):
    	if self.dict["extension"].upper() in self.extensionNonCode:
    		return True
    	return False


    def getProperty (self, p_property):
    	# return self.p_property
    	return (self.dict[p_property])


    def setProperty(self, p_property, p_value):
    	# self.p_property = p_value
    	self.dict[p_property]=p_value


    def verifBalise_tf(self):
        a = 100

    def verifBaliseObligatoirePresent_tf(self, p_motCle):
        motCleStart = '<mccd_'+p_motCle+'>'
        motCleEnd = '</mccd_'+p_motCle+'>'
        nbrStart = self.compteMc_data(motCleStart, self.dict["stringTexte"])
        nbrEnd = self.compteMc_data(motCleStart, self.dict["stringTexte"])
        if nbrStart==0 or nbrStart>1 or nbrEnd==0 or nbrEnd>1:
            return False
        else:
            return True

    def verifBaliseObligatoirePresent_data(self, p_motCle):
        motCleStart = '<mccd_'+p_motCle+'>'
        motCleEnd = '</mccd_'+p_motCle+'>'
        nbrStart = self.compteMc_data(motCleStart, self.dict["stringTexte"])
        nbrEnd = self.compteMc_data(motCleStart, self.dict["stringTexte"])
        if nbrStart==0 :
            return ("Ce mot-clé est manquant : "+ motCleStart)
        if nbrStart>1 :
            return ("Ce mot-clé est multiple ... : "+motCleStart)
        if nbrStart==1 :
            return ("Ce mot-clé est bien présent ... : "+motCleStart)
        if nbrEnd==0 :
            return ("Ce mot-clé est manquant : "+motCleEnd)
        if nbrEnd>1 :
            return ("Ce mot-clé est multiple ... : "+motCleEnd)
        if nbrEnd==1 :
            return ("Ce mot-clé est bien présent ... : "+motCleEnd)


    def verifBaliseObligatoirePresent_tfOLD(self):
        """ 4b3
        Les balises obligatoires sont-elles TOUTES présentes
        dans le texte du fichier ? 
        """
        textString = self.readFile2String_data()
        missing = False
        for motcle in mcObligatoire:
            motCleStart = '<mccd_'+motcle+'>'
            motCleEnd = '</mccd_'+motcle+'>'

            nbrStart = self.compteMc_data(motCleStart, textString)
            # print(motCleStart, " nbrStart : ",str(nbrStart))

            if nbrStart==0 :
                return ("Ce mot-clé est manquant : "+ motCleStart)

            if nbrStart>1 :
                return ("Ce mot-clé est multiple ... : "+motCleStart)

            if nbrStart==1 :
                print("Voici le mot-clé : ",motCleStart)
                
            nbrEnd = self.compteMc_data(motCleEnd, textString)
            # print(motCleEnd, " nbrEnd : ",str(nbrEnd))

            if nbrEnd==0 :
                return ("Ce mot-clé est manquant : "+motCleEnd)

            if nbrEnd>1 :
                return ("Ce mot-clé est multiple ... : "+motCleEnd)

            if nbrEnd==1 :
                print("Voici le mot-clé : ",motCleEnd)

        if not missing:
            print("Tous les mot-clé OBLIGATOIRES sont présents :) ")
            return True
        
	
    def verifBaliseObligatoirePresent_dataOLD(self):
    	return ("Certaines balises OBLIGATOIRES sont manquantes :( ")



    def verifFichierAssocie_tf(self):
    	self.a = 100


    def get_pairs(self):
    	return (self.dict.items())

    def get_keys(self):
    	return (self.dict.keys())
        
    def get_values(self):
    	return (self.dict.values())


    def mcIsPresent_tf(self, p_mc, p_text):
        """Le mot-clé est présent dans le texte ? """
        text = re.findall(p_mc,p_text)
        print("text : ",text)
        if text:
            return(True)
        return(False)
            

    def compteMc_data(self, p_mc, p_text):
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

    def indicateur_serie( self, p_value):
        # Si True est recherché alors toutes les 
        # valeurs doivent être les même que p_valueInit=1
        # print("Dans la classe, valeur passée à indicateur_serie : ",p_value)
        # print("self.indicateur : ",self.indicateur)
        self.indicateur = self.indicateur * p_value
        # print("Dans la classe, APRES self.indicateur : ",self.indicateur,"\n")

    def indicateur_para( self, p_value):
        # Si au moins un True est recherché alors au moins
        # l'une des valeurs doit être à True
        self.indicateur = self.indicateur | p_value

    def getIndicateur(self):
        return self.indicateur

    def setIndicateur(self, p_value):
        self.indicateur = p_value

class Regex(object):
    def __init__(self):
        self.regex = ""
    def textIsPresent_tf(self, p_text): # OK 30/11 11h51
        # 'p_text' est le texte à parcourir pour y rechercher une réponse. 
        # répondre T/F si le texte de la regex ('self.regex') est présent/absent.
        # self.regex est utilisé
        text = re.findall(self.regex,p_text)
        print("text : ",text)
        if text:
            return(True)
        return(False)

    def countWords(self, p_text): # OK 30/11 13h38
        # Compter le nbr de mots dans le texte 'p_text'
        # self.regex n'est PAS utilisé
        # 'p_text' est un string
        return len(re.findall("\s+",p_text))

    def countLines(self, p_text): # OK 30/11 13h49
        # compter les lignes dans le texte
        # self.regex n'est PAS utilisé
        tr = re.findall("\n",p_text)
        return len(tr)

    def countLetters(self, p_text): # OK 30/11 13h47
        # compter les lettres dans le texte
        # self.regex n'est PAS utilisé
        tr = re.findall(r".",p_text)
        return len(tr)
        
    def replaceText(self, p_text, p_replacementText): # OK 30/11 12h05
        # 'self.regex' est utilisée pour rechercher du texte dans 'p_text'
        # qui est remplacé par le texte 'p_replacementText'
        # To replace a string in Python, the regex sub() method is used.
        # 'flags' info : https://docs.python.org/3/library/re.html#flags
        return re.sub(self.regex,p_replacementText, p_text, count=0, flags=0)

    def createBaliseStart(self, p_text):
        return "<mccd_"+p_text+">"

    def createBaliseEnd(self, p_text):
        return "</mccd_"+p_text+">"

    def textePresentEntreBalises_tf(self, p_balise, p_text): # OK 30/11 12h47
    	# Vérifier si du texte est présent entre les balises données. 
        # Exemple p_balise='categorie' : <mccd_categorie> texte à retourner </mccd_categorie>
        # 'self.regex' n'est pas à renseigner
        # p_text le texte qui est parcouru pour recherche

        # créer les deux balises : 
        start_balise = "<mccd_"+p_balise+">"
        end_balise = "</mccd_"+p_balise+">"
        self.regex = "(?<=" + start_balise + ")(.*)(?=" +end_balise + ")"
        tr = re.findall(self.regex,p_text)
        if len(tr)>0:
        	return True
        else:
        	return False


    def textePresentEntreBalises_data(self, p_balise):
    	# la fonction 'textePresentEntreBalises_tf' a retourné False car aucun 
    	# texte est trouvé entres les balises
    	# Retourner le message d'erreur à stocker

        # créer les deux balises : 
        start_balise = "<mccd_"+p_balise+">"
        end_balise = "</mccd_"+p_balise+">"
        msg = "Les balises "+start_balise+" et"+end_balise+" ne contiennent pas de texte."
        return msg



    def texteEntreBalises (self, p_balise, p_text): # OK 30/11 12h47
        # retourner les texte compris entre deux balises 'mccd'. 
        # Exemple p_balise='categorie' : <mccd_categorie> texte à retourner </mccd_categorie>
        # 'self.regex' n'est pas à renseigner
        # p_text le texte qui est parcouru pour recherche

        # créer les deux balises : 
        start_balise = "<mccd_"+p_balise+">"
        end_balise = "</mccd_"+p_balise+">"
        self.regex = "(?<=" + start_balise + ")(.*)(?=" +end_balise + ")"
        tr = re.findall(self.regex,p_text)
        return (tr[0])

    def compterOccurences(self, p_text): # OK 30/11 12h52
        # Compter les occurences de self.regex dans le texte en 'p_text'
        # 'self.regex' est utilisée
        tr = re.findall(self.regex,p_text)
        return len(tr)

    def extractText(self, p_text): # OK 30/11 12h56
        # 'self.regex' est utilisée pour extraire toutes les occurences dans le texte 'p_text'
        # finditer : return re.finditer(self.regex,p_text)
        return re.findall(self.regex,p_text)
        
    def deleteText(self, p_text): # OK 30/11 12h30
        # 'self.regex' est utilisée pour effacer toutes les occurences dans le texte 'p_text'
        return re.sub(self.regex,"", p_text, count=0, flags=0)