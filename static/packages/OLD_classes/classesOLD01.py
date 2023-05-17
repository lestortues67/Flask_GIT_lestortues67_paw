"""
Source : 
Date : 30/01/2019
Auteur : Christian Doriath
Dossier : /Python34/MesDEv/Flask/FlaskBootstrap_BASE
Fichier : classes.py
Description : Module des classes uniquement et PAS des fonctions db SQLAlchemy;
trop compliqué à ce jour.



classes.py contient TOUTES les classes sauf les classes mySQL. 


"""



from starter import * 
  
arr = [{'nom':'NONTAILLE1', 'fichier':'NONTAILLE1.txt' ,'extension':'.txt', 'path':'D:',       'taille':22554},      
        {'nom':'TUTU', 'fichier':'TUTU.mc' ,'extension':'.mc', 'path':'D:\temp\TUTU.mc', 'taille':124554},
        {'nom':'okTaille1', 'fichier':'okTaille1.py' ,'extension':'.py', 'path':'D:\temp\okTaille1.py', 'taille':2554},
        {'nom':'TUTU', 'fichier':'TUTU.bmp' ,'extension':'.bmp', 'path':'D:\temp\TUTU.bmp', 'taille':124554},
        {'nom':'okTaille2', 'fichier':'okTaille2.c' ,'extension':'.c', 'path':'D:\temp\okTaille2.c', 'taille':2554},
        {'nom':'NONTAILLE2', 'fichier':'NONTAILLE2.txt' ,'extension':'.txt', 'path':'D:\temp_NONTAILLE2.txt', 'taille':12554},
       {'nom':'noEXT1', 'fichier':'noEXT1.vvv' ,'extension':'.vvv', 'path':'D:\temp_noEXT1.vvv', 'taille':12554},
        {'nom':'okTaille1', 'fichier':'okTaille1.py' ,'extension':'.py', 'path':'D:\temp\okTaille1.py', 'taille':2554},
        {'nom':'OWWO', 'fichier':'OWWO.bmp' ,'extension':'.bmp', 'path':'D:\temp\OWWO.bmp', 'taille':124554},
        {'nom':'ZAZA', 'fichier':'ZAZA.bmp' ,'extension':'.bmp', 'path':'D:\temp\ZAZA.bmp', 'taille':124554},
        {'nom':'okTaille3', 'fichier':'okTaille3.c' ,'extension':'.c', 'path':'D:\temp\okTaille3.c', 'taille':2554},
        {'nom':'OWWO', 'fichier':'OWWO.mc' ,'extension':'.mc', 'path':'D:\temp\OWWO.mc', 'taille':124554},
        {'nom':'okTaille4', 'fichier':'okTaille4.mc' ,'extension':'.mc', 'path':'D:\temp\okTaille4.mc', 'taille':154} ]



# List all the fieldtypes in MySQL for the date & self.path:
# CREATE  TABLE `test`.`ban01` (

#   `idban01` INT NOT NULL AUTO_INCREMENT ,

#   `name` VARCHAR(45) NULL ,

#   `mydate` DATE NULL ,

#   `mydatetime` DATETIME NULL ,

#   `mytime` TIME NULL ,

#   `mytimestamp` TIMESTAMP NULL ,

#   `myyear` YEAR NULL ,


#   PRIMARY KEY (`idban01`) );




class MasterLogic(object):
    def __init__(self):
        """
        Cette classe a besoin d'indicateurs donc je crée une instance 'self.i'
        
        """
    def pairsArePresent_tf(self, p_dict, p_list):
        """
        Pour 'p_dict' c'est en général quelques une ou deux paires qui sont utilisées 
        pour rechercher la présence d'un dict dans une liste de dict. 
        Si, par exemple, la liste 'p_list' contient des dict 
        d'informations sur des fichiers dans un dossier comme celui-ci : 
        {'nom':'okTaille1', 'fichier':'okTaille1.py' ,'extension':'.py', 
        'path':'D:\temp\okTaille1.py', 'taille':2554},

        alors on pourrait vérifier sa présence avec ces paires : 
        p_dict = {'fichier':'okTaille1.py' ,'extension':'.py'}

        p_dict : dict, TOUTES ses paires sont présentes dans un dict de la liste 'p_list' ? 
        p_list : la liste à parcourir pour rechercher un dict qui contient TOUTE les paires de 'p_dict'
        p_instanceIndicateur : une instance de la classe 'Indicateur'

        """
        self.i = Indicateur(1)
        # Sortir de 'p_dict' les paires :
        self.lesPaires = p_dict.items()
        # self.indicatorClass = p_instanceIndicateur

        # Une boucle sur 'p_list'
        for dictionnaire in p_list:
            # self.indicatorClass.setIndicateur(1)
            self.i.setIndicateur(1)
                # Une boucle sur TOUTES les paires : 
            for key, value in self.lesPaires:
                # La clé existe ? 
                # self.indicatorClass.indicateur_serie(key in dictionnaire)
                self.i.indicateur_serie(key in dictionnaire)
                if (self.i.getIndicateur()):
                    # oui, elle existe
                    # Cette paire est présente dans le dict ? 
                    self.i.indicateur_serie(dictionnaire[key]==value)
            if (self.i.getIndicateur()):
                return True
        return False
        
    def verifTailleFichier(self, p_dict):
        # fichier CODE sa taille < 5000
        if p_dict['taille']>5000:
            return True
        return False

    def extensionInvalide(self, p_dict):
        # rechercher extension INVALIDE 
        if not ( (p_dict['extension'].upper() in extensionCode) or 
            (p_dict['extension'].upper() in extensionNonCode) or 
            (p_dict['extension'].upper() in extensionMc) ):
            return True
        return False

    def fichierImageManquant(self, p_dict, p_listOfFiles):
        # rechercher les fichiers MC sans fichier IMAGE 
        # 4) Rechercher si un fichier de type MC possède son équivalent en fichier IMAGE
        self.i = Indicateur(1)
        if (p_dict['extension'].upper() in extensionMc):
            # print("998 Voici le type de fichier qui recherche son ami : ",p_dict['extension'].upper())
            # print("Voici son dict : ",p_dict)
            d = {'fichier':p_dict['fichier']}
            # Parcourir les 'extensions' de type IMAGE 
            for ext in extensionNonCode:
                # Rechercher si un fichier avec cette ext existe
                d['extension'] = ext.lower()
                # print("Extension recherchée : ",ext.lower())
                # Rechercher si un dict dans la liste p_listOfFiles contient les paires dans 'd'
                # print("Le dict recherché est : ",d)
                r = self.pairsArePresent_tf(d, p_listOfFiles)
                # print("Résultat de la recherche du fichier IMAGE : ", self.getIndicateur(),"\n")
                if (self.i.getIndicateur()==True):
                    return False
            return True

    def fichierMcManquant(self, p_dict, p_listOfFiles):
        # rechercher les fichiers IMAGE sans fichier MC 
        # 5) Rechercher si un fichier de type IMAGE possède son équivalent en fichier MC
        self.i = Indicateur(1)
        if (p_dict['extension'].upper() in extensionNonCode):
            # print("999 Voici le type de fichier qui recherche son ami : ",p_dict['extension'].upper())
            # print("Voici son dict : ",p_dict)
            d = {'fichier':p_dict['fichier'],'extension':'.mc'}
            # Parcourir les dict pour rechercher un fichier '.mc'
            self.i.setIndicateur(1)
            r = self.pairsArePresent_tf(d, p_listOfFiles)
            # print("Résultat de la recherche du fichier IMAGE : ", self.getIndicateur(),"\n")
            if (self.i.getIndicateur()==True):
                return False
            return True

    def fileIsCode(self, p_dict):
        # si le type du fichier est CODE retourne True
        if(p_dict['extension'].upper() in extensionCode):
            return True
        return False

    def fileIsNonCode(self, p_dict):
        # si le type du fichier est NONCODE retourne True
        if(p_dict['extension'].upper() in extensionNonCode):
            return True
        return False

    def fileIsMc(self, p_dict):
        # si le type du fichier est MC retourne True
        if(p_dict['extension'].upper() in extensionMc):
            return True
        return False
        
    def checkWithFunction(self, p_function, p_args):
        # 'p_function' est la fonction utilisée pour faire la vérification
        # 'p_args' DOIT être un ITERABLE (liste)
        if (p_function(*p_args)):
            return True
        return False

class Data(MasterLogic):
    def __init__(self):
        """
        J'hérite de TOUTES les méthodes (PAS les propriétés) de la classe 'MasterLogic' !

        Les paramètres : PPPPPPPPPPPPPPPPPPPPPPPPPPPPP
        
        # Les preffixes (ajoutés aux méthodes) utilisés : FFFFFFFFFFFFFFFFFFFFF
        Ils sont 1 : 
        errorIfNot_ : une autre méthode a retourné False. Si l'on souhaite en avoir la raison 
        on appelle cette méthode. 

        # Les suffixes (ajoutés aux méthodes) utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'msg':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        """
        self.valide = []
        self.invalide = []
        self.dict = {}
        self.listOfFiles = [] 


    def checkValidity(self):
        # Parcourir la liste des fichiers VALIDE et déplacer les fichiers
        # vers INVALIDE si invalide =1
        lIndex = []
        for index, d in enumerate(self.valide):
            print("if d['invalide']==1: ",d['invalide'])
            if d['invalide']==1:
                lIndex.append(d)
        
        for d in lIndex:
            i = self.dictGetMyIndexValide(d)
            self.moveToInvalide(i)

    def appendToListOfFiles(self, p_value):
        # print("J'ajoute dans listOfFiles ...")
        # self.listOfFiles.append({'nom':'tata.txt','fichier':'tata','extension':'.txt'})
        self.listOfFiles.append(p_value)

    def appendList_tf(self, p_list):
        # Une liste est passée dans 'p_list'
        if isinstance(p_list,list):
            for item in p_list:
                self.listOfFiles.append(item)
            return True
        return False

    def getListOfFiles(self):
        return self.listOfFiles

    def convert2Tuple_data(self, p_listOfDict):
        """
        Convertir une liste de dict en une liste de tuples. 
        """
        l = []
        for d in p_listOfDict:
            tKeys = tuple(d.keys())
            tValues = tuple(d.values())
            l.append((tKeys, tValues))
        return l

    def convertTuple2Dict (self, p_tuple):
        # p_tuple[0] =  p_tupleKeys
        # p_tuple[1] =  p_tupleValues
        d = {}
        print("length of tuple : ",len(p_tuple))
        print("length of tuple[0] : ",len(p_tuple[0]))
        print("length of tuple[1] : ",len(p_tuple[1]))
        for index, entry in enumerate(p_tuple[0]):
            print("Key : ",entry)
            print("Value : ",p_tuple[1][index])
            print("index : ",index)
            d[entry] = p_tuple[1][index]
        return d


    def moveToInvalide(self, p_index):
        # déplacer un élément de la liste 'valide' vers la liste 'invalide'
        self.invalide.append(self.valide[p_index])
        # print("AVANT len(self.valide) : ",len(self.valide))
        self.valide.pop(p_index)
        # print("APRES len(self.valide) : ",len(self.valide))


    def dictGetMyIndexValide(self, p_dict):
        # retourner l'index dans la liste 'valide' pour le dict passé en p_
        # index() Returns the index of the first element with the specified value
        return self.valide.index(p_dict)

    def getValideTuple(self):
        return self.convert2Tuple_data(self.valide)

    def getValide(self):
        return (self.valide)

    def getInvalideTuple(self):
        return self.convert2Tuple_data(self.invalide)

    def getInvalide(self):
        return (self.invalide)
    
    def addToValide(self, p_dict):
        self.valide.append(p_dict)

    def addToInvalide(self, p_dict):
        self.invalide.append(p_dict)

    def getDictValide(self, p_index):
        # retourner un dict de VALIDE pour un index donné
        return self.valide[p_index]

    def getDictInvalide(self, p_index):
        # retourner un dict de INVALIDE pour un index donné
        return self.invalide[p_index]

    def newDict(self):
        self.dict = {}

    def addToDict(self, p_key, p_value):
        """
        Voici le format du dict : 
        {'nom':nom, 'fichier':fichier ,'extension':extension, 'invalide':0, 
           'path':path, 'taille':taille, 'errormsg' :"",'mc_extAssocie':'',
           'type':'','listeLigne':'','stringTexte':''}
        """
        self.dict[p_key] = p_value

    def isInList(self, p_value, p_list):
        if(p_value in p_list):
            return True
        return False


    def lessThen(self, p_value, p_limit):
        if(p_value < p_limit):
            return True
        return False

class MainNew(MasterLogic):
    """
    J'hérite de TOUTES les méthodes (PAS les propriétés) de la classe 'MasterLogic' !

    Cette classe est la maitresse pour faire fonctionner TOUTE l'app.

    Les paramètres : PPPPPPPPPPPPPPPPPPPPPPPPPPPPP
        'p_path' est du genre "path/to/the/filename"
        exemple 'p_path' : D:\\Python39\\MesDEv\\Flask\\Flask_codebase2023\\'

        # Les preffixes (ajoutés aux méthodes) utilisés : FFFFFFFFFFFFFFFFFFFFF
        Ils sont 1 : 
        errorIfNot_ : une autre méthode a retourné False. Si l'on souhaite en avoir la raison 
        on appelle cette méthode. 

        # Les suffixes (ajoutés aux méthodes) utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'msg':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        Cette classe prend en entrée un PATH.  
        Elle fournit en sortie 2 listes de DICT : 
        les fichiers 'VALIDE'
        les fichiers 'INVALIDE'

        Utilisation : o = Main("path")

    """
    def __init__(self, p_path):
        # Grâce à l'instance 'self.data' j'ai accès à la liste 'listOfFiles' dans la classe 'Data'
        self.data = DataNew()
        self.path = p_path
        # Les informations sur TOUS les fichiers du dossier 'app.config['UPLOAD_FOLDER']'
        # sont stockées dans une liste. 
        

        # classe 'Dossier'
        self.d = Dossier(app.config['UPLOAD_FOLDER'])       

        if not (self.d.pathIsValid_tf()):
            print("Une erreur s'est produite sur le dossier fourni : ", self.d.pathIsValid_data())
            exit()
        else:
            # Le path est valide on continue

            # créer un objet 'file' instance de FichierNew

            # stocker cet objet dans 'data' instance de DataNew






            self.listeFichiers = self.d.recordAllFiles()
            """
            # recordAllFiles() fait ceci : 
            # enregistrer les datas sur TOUS les fichiers présents dans un dict 
            # au format de la liste 'fileKeys'
            fileKeys = ["nom", "fichier", "extension", "path", "taille", 
            "errormsg", "mc_extAssocie", "type", "invalide", "listeLigne", "stringTexte"]
            Tous les fichiers sont de type VALIDE (invalide = 0)

            """

        self.d.verificatorDossier(self.listeFichiers)

        #ajouter la liste 'self.listeFichiers' dans l'instance de la classe 'Data' (sa liste listOfFiles) : 
        self.data.appendList_tf(self.listeFichiers)

        """
        d.verificatorDossier : 
        A l'aide de méthodes de la classe 'Verify' ces vérifications sont faites : 
            fichier CODE sa taille < 5000 def verifTailleFichier(self):
            rechercher extension INVALIDE def extensionInvalide(self):
            rechercher les fichiers IMAGE sans fichier MC def fichierMcManquant(self):
            rechercher les fichiers MC sans fichier IMAGE def fichierImageManquant(self):
        """

        # Trier entre VALIDE / INVALIDE
        print("Les dict sont repartis entre VALIDE / INVALIDE")
        for dict in self.data.getListOfFiles():
            if dict['invalide']==False:     
                self.data.addToValide(dict)
            else:
                self.data.addToInvalide(dict)

        print("A l'aide de la liste VALIDE afficher les ",len(self.data.getValide()), "dict ")
        for dict in self.data.getValide():
            print(dict['invalide']," | ",dict['nom']," | ",dict['errormsg']," | ",dict['type'])
        print("\n")

        print("A l'aide de la liste INVALIDE afficher les ",len(self.data.getInvalide()), "dict ")
        for dict in self.data.getInvalide():
            print(dict['invalide']," | ",dict['nom']," | ",dict['errormsg']," | ",dict['type'])
        print("\n")

        # FIN des opérations dans la classe 'Dossier'
        """
        classe 'Fichier' : 
        Les dict des fichiers se trouvent ici : self.data.getListOfFiles()
        """
        indexRecorder = []

        #Une boucle sur TOUS les fichiers CODE et MC de la liste VALIDE : 
        for dict in self.data.getValide():
            if dict['type']=='CODE' or dict['type']=='MC' :     
                print("Nom fichier : ",dict['nom'])
                # créer une instance de la classe 'Fichier'
                file = Fichier(dict['path'])
                baliseOK = file.baliseObligatoirePresent_tf()
                if (baliseOK == True):
                    print("Les MC sont TOUS présents")
                else:
                    indexRecorder.append(dict)
                    print("Message erreur balise : ",baliseOK)
                    print("dict AVANT modif : ",dict)
                    dict["errormsg"] = baliseOK
                    print("dict APRES modif : ",dict)

        for dict in indexRecorder:
            i = self.data.dictGetMyIndexValide(dict)
            self.data.moveToInvalide(i)

        

        print("Après FICHIER ")
        print("Voici les fichiers INVALIDE")
        for dict in self.data.getInvalide(): 
            print("fichier INVALIDE : ",dict['nom']," | ",dict["errormsg"])
        print("\n")
        print("Voici les fichiers VALIDE")
        for dict in self.data.getValide():
            print("fichier VALIDE : ",dict['nom'])
        
        print("\n")


       # mcObligatoirePresent_tf(self): 


        # 1) On entre pour vérifier que les balises OBLIGATOIRES sont présentes 

        # FIN des opérations dans la classe 'Fichier'

        # classe 'Balise'

        # 1) On entre pour extraire les datas dans les balises <mccd_xyz> datas </mccd_xyz> 

        # FIN des opérations dans la classe 'Balise'


class Main(MasterLogic):
    """
    J'hérite de TOUTES les méthodes (PAS les propriétés) de la classe 'MasterLogic' !

    Cette classe est la maitresse pour faire fonctionner TOUTE l'app.

    Les paramètres : PPPPPPPPPPPPPPPPPPPPPPPPPPPPP
        'p_path' est du genre "path/to/the/filename"
        exemple 'p_path' : D:\\Python39\\MesDEv\\Flask\\Flask_codebase2023\\'

        # Les preffixes (ajoutés aux méthodes) utilisés : FFFFFFFFFFFFFFFFFFFFF
        Ils sont 1 : 
        errorIfNot_ : une autre méthode a retourné False. Si l'on souhaite en avoir la raison 
        on appelle cette méthode. 

        # Les suffixes (ajoutés aux méthodes) utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'msg':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        Cette classe prend en entrée un PATH.  
        Elle fournit en sortie 2 listes de DICT : 
        les fichiers 'VALIDE'
        les fichiers 'INVALIDE'

        Utilisation : o = Main("path")

    """
    def __init__(self, p_path):
        # Grâce à l'instance 'self.data' j'ai accès à la liste 'listOfFiles' dans la classe 'Data'
        self.data = Data()
        self.path = p_path
        # Les informations sur TOUS les fichiers du dossier 'app.config['UPLOAD_FOLDER']'
        # sont stockées dans une liste. 
        

        # classe 'Dossier'
        self.d = Dossier(app.config['UPLOAD_FOLDER'])       

        if not (self.d.pathIsValid_tf()):
            print("Une erreur s'est produite sur le dossier fourni : ", self.d.pathIsValid_data())
            exit()
        else:
            # Le path est valide on continue
            self.listeFichiers = self.d.recordAllFiles()
            """
            # recordAllFiles() fait ceci : 
            # enregistrer les datas sur TOUS les fichiers présents dans un dict 
            # au format de la liste 'fileKeys'
            fileKeys = ["nom", "fichier", "extension", "path", "taille", 
            "errormsg", "mc_extAssocie", "type", "invalide", "listeLigne", "stringTexte"]
            Tous les fichiers sont de type VALIDE (invalide = 0)

            """

        self.d.verificatorDossier(self.listeFichiers)

        #ajouter la liste 'self.listeFichiers' dans l'instance de la classe 'Data' (sa liste listOfFiles) : 
        self.data.appendList_tf(self.listeFichiers)

        """
        d.verificatorDossier : 
        A l'aide de méthodes de la classe 'Verify' ces vérifications sont faites : 
            fichier CODE sa taille < 5000 def verifTailleFichier(self):
            rechercher extension INVALIDE def extensionInvalide(self):
            rechercher les fichiers IMAGE sans fichier MC def fichierMcManquant(self):
            rechercher les fichiers MC sans fichier IMAGE def fichierImageManquant(self):
        """

        # Trier entre VALIDE / INVALIDE
        print("Les dict sont repartis entre VALIDE / INVALIDE")
        for dict in self.data.getListOfFiles():
            if dict['invalide']==False:     
                self.data.addToValide(dict)
            else:
                self.data.addToInvalide(dict)

        print("A l'aide de la liste VALIDE afficher les ",len(self.data.getValide()), "dict ")
        for dict in self.data.getValide():
            print(dict['invalide']," | ",dict['nom']," | ",dict['errormsg']," | ",dict['type'])
        print("\n")

        print("A l'aide de la liste INVALIDE afficher les ",len(self.data.getInvalide()), "dict ")
        for dict in self.data.getInvalide():
            print(dict['invalide']," | ",dict['nom']," | ",dict['errormsg']," | ",dict['type'])
        print("\n")

        # FIN des opérations dans la classe 'Dossier'
        """
        classe 'Fichier' : 
        Les dict des fichiers se trouvent ici : self.data.getListOfFiles()
        """
        indexRecorder = []

        #Une boucle sur TOUS les fichiers CODE et MC de la liste VALIDE : 
        for dict in self.data.getValide():
            if dict['type']=='CODE' or dict['type']=='MC' :     
                print("Nom fichier : ",dict['nom'])
                # créer une instance de la classe 'Fichier'
                file = Fichier(dict['path'])
                baliseOK = file.baliseObligatoirePresent_tf()
                if (baliseOK == True):
                    print("Les MC sont TOUS présents")
                else:
                    indexRecorder.append(dict)
                    print("Message erreur balise : ",baliseOK)
                    print("dict AVANT modif : ",dict)
                    dict["errormsg"] = baliseOK
                    print("dict APRES modif : ",dict)

        for dict in indexRecorder:
            i = self.data.dictGetMyIndexValide(dict)
            self.data.moveToInvalide(i)

        

        print("Après FICHIER ")
        print("Voici les fichiers INVALIDE")
        for dict in self.data.getInvalide(): 
            print("fichier INVALIDE : ",dict['nom']," | ",dict["errormsg"])
        print("\n")
        print("Voici les fichiers VALIDE")
        for dict in self.data.getValide():
            print("fichier VALIDE : ",dict['nom'])
        
        print("\n")


       # mcObligatoirePresent_tf(self): 


        # 1) On entre pour vérifier que les balises OBLIGATOIRES sont présentes 

        # FIN des opérations dans la classe 'Fichier'

        # classe 'Balise'

        # 1) On entre pour extraire les datas dans les balises <mccd_xyz> datas </mccd_xyz> 

        # FIN des opérations dans la classe 'Balise'


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


class Dossier(MasterLogic):
    def __init__(self, p_path):
        """
        J'hérite de TOUTES les méthodes (PAS les propriétés) de la classe 'MasterLogic' !

        Les paramètres : PPPPPPPPPPPPPPPPPPPPPPPPPPPPP
        'p_path' est du genre "path/to/the/filename"
        exemple 'p_path' : D:\\Python39\\MesDEv\\Flask\\Flask_codebase2023\\'

        # Les preffixes (ajoutés aux méthodes) utilisés : FFFFFFFFFFFFFFFFFFFFF
        Ils sont 1 : 
        errorIfNot_ : une autre méthode a retourné False. Si l'on souhaite en avoir la raison 
        on appelle cette méthode. 

        # Les suffixes (ajoutés aux méthodes) utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'msg':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        Cette classe prend en entrée un PATH.  
        Elle fournit en sortie UNE LISTE de dictionnaires qui utilisent les clés de la liste 'fileKeys'


        """
        self.path = p_path
        # self.data = Data()
        # self.v = Verify()

    def pathIsValid_tf(self):
        # analyse si le dossier self.path existe
        try:
            t = os.stat(self.path)
            # print("os.stat(self.path) : ",os.stat(self.path))
            print(self.path, " is a VALID path !")
            return True
        except FileNotFoundError:
            print("FileNotFoundError \n")
            return False
        except OSError:
            print("OSError \n")
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


    def recordAllFiles(self):
        # enregistrer les datas sur TOUS les fichiers présents dans un dict 
        # au format de la liste 'fileKeys'
        tempList = []
        scanIterator = os.scandir(path=self.path)
        with scanIterator as item:
            # création du dict avec les clés données dans liste 'fileKeys'
            d = {}
            for key in fileKeys:
                d[key] = ""
            for entry in item:
                if not entry.name.startswith('.') and entry.is_file():
                    nom = entry.name
                    data =  os.path.splitext(entry.name)
                    fichier = data[0]
                    extension = data[1]
                    path = entry.path
                    stat = entry.stat
                    taille = entry.stat()[6]

                    # fileKeys = ["nom", "fichier", "extension", "path", "taille", 
                    # "errormsg", "mc_extAssocie", "type", "invalide", "listeLigne", "stringTexte"]

                    d = {'nom':nom, 'fichier':fichier ,'extension':extension, 
                    'path':path, 'taille':taille, 'errormsg' :"",'mc_extAssocie':'',
                    'type':'','listeLigne':'','stringTexte':'','invalide':0}
                    tempList.append(d)
        print("Ce dossier contient ",str(len(tempList))," fichiers.\n")
        return tempList

    def verificatorDossier(self, p_liste):
        """
        A l'aide de méthodes de la classe 'Verify' ces vérifications sont faites : 
            fichier CODE sa taille < 5000 def verifTailleFichier(self):
            rechercher extension INVALIDE def extensionInvalide(self):
            rechercher les fichiers IMAGE sans fichier MC def fichierMcManquant(self):
            rechercher les fichiers MC sans fichier IMAGE def fichierImageManquant(self):

            Beaucoup des méthodes qui suivent appartiennent à la classe 'MasterLogic'
        """

        # Parcourir TOUS les dict de la liste 'p_liste'
        for dictionnaire in p_liste: 
            # fichier CODE sa taille < 5000 
            if self.fileIsCode(dictionnaire): 
                dictionnaire['type']='CODE'
                if self.verifTailleFichier(dictionnaire):
                    dictionnaire['invalide'] = 1 
                    dictionnaire['errormsg'] = "La taille du fichier est supérieure à la taille maximale autorisée."
            if self.extensionInvalide(dictionnaire):
                dictionnaire['invalide'] = 1 
                msg = "L'extension du fichier "+dictionnaire['extension']+" n'est PAS reconnue"
                dictionnaire['errormsg'] = msg
            if self.fichierImageManquant(dictionnaire, p_liste):
                msg = "Il manque le fichier IMAGE pour ce fichier *.mc  " + dictionnaire['nom']
                dictionnaire['invalide'] = 1  
                dictionnaire['errormsg'] = msg
            if self.fichierMcManquant(dictionnaire, p_liste):
                dictionnaire['invalide'] = 1  
                msg = "Il manque le fichier mot clé pour ce fichier IMAGE  " + dictionnaire['nom']
                dictionnaire['errormsg'] = msg
            if self.fileIsNonCode(dictionnaire): 
                dictionnaire['type'] = "NONCODE"
            if self.fileIsMc(dictionnaire): 
                dictionnaire['type'] = "MC"
            # ajouter le dictionnaire dans la classe 'Data' 
            # self.appendToListOfFiles('dictionnaire')


class FichierNew(MasterLogic):
    def __init__(self, p_path):
        """
        # Les clés FICHIER : 
        fileKeys = ["nom", "fichier", "extension", "path", "taille", 
        "errormsg", "mc_extAssocie", "type", "invalide", "listeLigne", "stringTexte"]

        # Les clés de dictionnaire obligatoires ( et les champs du STOCKAGE dans table mySQL ) : 
        mcObligatoire = ["id","deleted","priorId","langage","categorie","souscategorie",
        "commentaire","nom","code","creationDate","modificationDate","auteur"]


        """
        self.dict = {"nom":"", "fichier":"", "extension":"", "path":"", "taille":"", 
        "errormsg":"", "mc_extAssocie":"", "type":"", "invalide":"", "listeLigne":"", 
        "stringTexte":"", "id":"","deleted":"","priorId":"","langage":"",
        "categorie":"","souscategorie":"","commentaire":"","nom":"","code":"",
        "creationDate":"","modificationDate":"","auteur":""}


class Fichier(MasterLogic):
    def __init__(self, p_path):
        """
        J'hérite de TOUTES les méthodes (PAS les propriétés) de la classe 'MasterLogic' !

        On entre dans le fichier pour vérifier que TOUTES les balises obligatoires sont
        présentes pour les fichiers de type 'CODE' et 'MC'. 

        à installer : 
        # utilisation des regex 
        import re 

        # avoir accès au système
        import os
        import os.path
        # créer des string aléatoires
        import string
        from random import choice

        # horodater
        import datetime
        import locale
        import time
        locale.setlocale(locale.LC_TIME, "fr_FR")

        # Les paramètres : PPPPPPPPPPPPPPPPPPPPPPPPPPPPP
        p_path est du genre "path/to/the/filename"
        exemple 'p_path' : D:\\Python39\\MesDEv\\Flask\\Flask_codebase2023\\file01.py'

        # Les suffixes utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'msg':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        Reste à faire : 

        Fermer les fichiers ouverts avec 'os.close(f)' ? 

        """
        self.fichier = p_path
        self.extension = ""
        self.taille = 0
        self.nom = ""
        self.fileLines = []

        """

        Les choix possibles pour les MC obligatoires sont imposés 
        pour : 
        "langage" : autre, css, javascript, html, python, c, jinja, 
        
        Chaque entrée dans "catégorie" possède ses propres choix limités. 
        Par exemple pour langage 'css' les seuls choix pour l'instant sont : 
        auutre et bootstrap. 

        

        <mccd_langage> </mccd_langage>
        <mccd_categorie> </mccd_categorie>
        <mccd_souscategorie> </mccd_souscategorie>
        <mccd_commentaire> </mccd_commentaire>
        <mccd_code_texte> </mccd_code_texte>
        <mccd_code2run> </mccd_code2run>
        """

        # Les mots-clés facultatifs : 
        self.mcFacultatif = ["nom","deleted","visuel","datecreation","datecreation_texte",
        "ficheImageAssocie","datemodification","datemodification_texte","auteur"]
        """
        <mccd_nom> </mccd_nom> : le nom du fichier n'est pas important 
        c'est son contenu qui sera nommé et stocké dans la table
        <mccd_deleted> </mccd_deleted> : est utilisé par l'app quand un element est 'effacé'
        <mccd_visuel> </mccd_visuel>
        <mccd_datecreation> </mccd_datecreation>
        <mccd_datecreation_texte> </mccd_datecreation_texte>
        <mccd_datemodification> </mccd_datemodification>
        <mccd_datemodification_texte> </mccd_datemodification_texte>
        <mccd_auteur> </mccd_auteur>
        """

        print("self.fichier : ",self.fichier)

    def fileOk_tf(self):
        """Class method docstrings go here."""
        # vérifier si le path est un fichier valide
        return(os.path.isfile(self.fichier))

    def errorIfNot_fileOk_tf(self):
        #Informe sur les raisons de l'exception
        # Cette méthode est appelé si la méthode 'fileOk_tf' a retourné False
        # A FINIR avec des exceptions comme : FileNotFoundError, etc ...
        try:
            f = open(self.fichier, "r")
            print("file is VALID")
            close(f)
            d = {'succes':True, 'msg':'OK file', 'data':""}
            return d
        except FileNotFoundError:
            print("FileNotFoundError \n")
            d = {'succes':False, 'msg':'path error : FileNotFoundError', 'data':""}
            return d
        except OSError:
            print("OSError \n")
            print("OSError \n")
            d = {'succes':False, 'msg':'path error : OSError', 'data':""}
            return d

    def fileInfo(self):
        """

        # utiliser le fichier log01.py

        f = open("for01.py", "r")

        p = os.stat("for01.py")

        print(len(p))


        for item in p:
            print(item)

        print("====================")

        """
        # lire les infos 
        fileData = os.stat(self.fichier)


        """
        os.stat_result(
        st_mode=33206, 
        st_ino=3377699720830231, 
        st_dev=1681274704, 
        st_nlink=1, 
        st_uid=0, 
        st_gid=0, 
        size : st_size=149, 
        st_atime=1669226049, 
        mod time : st_mtime=1669225012, 
        create time : st_ctime=1668845315)
        """

        # fileData[0] à fileData[9]




    def apresOpenTagRegex_data(self, p_mc):
        """Class method docstrings go here."""
        # Un nouveau REGEX est renvoyé. 
        # Si le texte est : "abc<mccd_code>mccd_code</mccd_code>defghijklmnopqrstuvwxyz"
        # Avec ce REGEX la f_ 'readMcData' retourne : "mccd_code</mccd_code>defghijklmnopqrstuvwxyz"
        # C'est la partie du texte APRES la balise d'OUVERTURE <mccd_code>
        txt = "(?<=<mccd>)(.*)"
        newRegex = txt.replace("mccd", p_mc)
        return newRegex

    def avantCloseTagRegex_data(self, p_mc):
        """Class method docstrings go here."""
        # Un nouveau REGEX est renvoyé. 
        # Si le texte est : "abc<mccd_code>mccd_code</mccd_code>defghijklmnopqrstuvwxyz"
        # Avec ce REGEX la f_ 'readMcData' retourne : "abc<mccd_code>mccd_code"
        # C'est la partie du texte AVANT la balise de FERMETURE </mccd_code>
        txt = "(.*?)(?=</mccd>)"
        newRegex = txt.replace("mccd", p_mc)
        return newRegex


        # à améliorer !!!!!!!! pour une lecture des datas pour 'code'
        # sur plusieurs lignes
    def readMcData_data(self, p_regex, p_text):
        """Class method docstrings go here."""
        tr = re.findall(p_regex,p_text)
        print("recherche : ",tr)
        return tr

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


    def readFileToArray_data(self):
        if(self.fileOk()):
            f = open(self.fichier, "r")
            for line in f:
                self.fileLines.append(line)
                print("Ligne : ",line)
            close(f)
            return self.fileLines 
        print("wrong file...")

    def readFile2String_data(self):
        # convertir le contenu du fichier en un grand string : 
        f = open(self.fichier, "r")
        with f as file:
            myString = file.read().replace('\n', '')
        # os.close(f)
        return myString


    def baliseObligatoirePresent_tf(self):
        """ Les balises obligatoires sont-elles TOUTES présentes
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
        

class Balise(MasterLogic):
    def __init__(self, p_path):
        """
        J'hérite de TOUTES les méthodes (PAS les propriétés) de la classe 'MasterLogic' !

        Les paramètres : PPPPPPPPPPPPPPPPPPPPPPPPPPPPP
        'p_path' est du genre "path/to/the/filename"
        exemple 'p_path' : D:\\Python39\\MesDEv\\Flask\\Flask_codebase2023\\'

        # Les preffixes (ajoutés aux méthodes) utilisés : FFFFFFFFFFFFFFFFFFFFF
        Ils sont 1 : 
        errorIfNot_ : une autre méthode a retourné False. Si l'on souhaite en avoir la raison 
        on appelle cette méthode. 

        # Les suffixes (ajoutés aux méthodes) utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'msg':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        Cette classe prend en entrée un PATH.  
        Elle fournit en sortie 2 listes de DICT : 
        les fichiers 'VALIDE'
        les fichiers 'INVALIDE'


        """
        self.path = p_path
        self.extensionCode = ['.c','.h','.js','.py','.html','.htm','.txt']
        self.extensionNonCode = ['.bmp','.jpg','.jpeg','.jpg','.png','.svg','.ico']
        self.extensionMc = [".mc"]
        self.tailleMaxiFichierCode = 5000

    def getWorkDir_data(self):
        return os.getcwd()


class DatabaseStorage(MasterLogic):
    def __init__(self, p_path):
        """
        J'hérite de TOUTES les méthodes (PAS les propriétés) de la classe 'MasterLogic' !

        Les paramètres : PPPPPPPPPPPPPPPPPPPPPPPPPPPPP
        'p_path' est du genre "path/to/the/filename"
        exemple 'p_path' : D:\\Python39\\MesDEv\\Flask\\Flask_codebase2023\\'

        # Les preffixes (ajoutés aux méthodes) utilisés : FFFFFFFFFFFFFFFFFFFFF
        Ils sont 1 : 
        errorIfNot_ : une autre méthode a retourné False. Si l'on souhaite en avoir la raison 
        on appelle cette méthode. 

        # Les suffixes (ajoutés aux méthodes) utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'msg':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        Cette classe prend en entrée un PATH.  
        Elle fournit en sortie 2 listes de DICT : 
        les fichiers 'VALIDE'
        les fichiers 'INVALIDE'


        """
        self.path = p_path
        self.extensionCode = ['.c','.h','.js','.py','.html','.htm','.txt']
        self.extensionNonCode = ['.bmp','.jpg','.jpeg','.jpg','.png','.svg','.ico']
        self.extensionMc = [".mc"]
        self.tailleMaxiFichierCode = 5000

    def getWorkDir_data(self):
        return os.getcwd()


class Mail(MasterLogic):
    def __init__(self, p_configMailFile):
        """
        J'hérite de TOUTES les méthodes (PAS les propriétés) de la classe 'MasterLogic' !

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
        _dict : la méthode retourne ce dict {'succes':True, 'msg':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        """

        

        self.a = 100

    def connectTest(self):
        # mail.connect()
        a = 100

    def sendMail_dict(self, p_object, p_message, p_ListeDestinataires, p_type):
        # p_object : ex : "Une erreur de LOG"
        # p_message : ex : "Le LOG n'est PAS conforme à la norme ..."
        # p_ListeDestinataires est un ARRAY de string des destinataires
        # p_type indique si le corps du mail est constitué de code HTML ou pas
        # seles 2 valeurs sont acceptées : 'html' ou TOUT autre string comme 'texte'

        #mailDestinataires=["commercial01@bio220.fr","cd062@free.fr"]
        destinataires = ', '.join(p_ListeDestinataires)

        msg= Message(subject=p_object, sender="serveur@codebase.fr",
        recipients=p_ListeDestinataires) 

        msg.body = p_message
        if p_type.upper() == 'HTML' :
            msg.html = render_template('MyTable.html')

        try:
            mail.send(msg)
            msg = 'e-mail envoyé à ' + destinataires +" à " + str(datetime.datetime.now())
            return ({'succes':True, 'msg':msg, 'data':""})                  

        except smtplib.SMTPAuthenticationError:
            print(" smtplib.SMTPAuthenticationError")
            return ({'succes':False, 'msg':'smtplib.SMTPAuthenticationError', 'data':""})                        
        except smtplib.SMTPException:
            print(" smtplib.SMTPException")
            return ({'succes':False, 'msg':'smtplib.SMTPException', 'data':""})                        

class Log(MasterLogic):
    def __init__(self, p_logFile):
        """
        J'hérite de TOUTES les méthodes (PAS les propriétés) de la classe 'MasterLogic' !

        Ecriture dans le fichier de LOG
        
        A installer : 
        import logging
        import datetime
        import locale
        import time
        locale.setlocale(locale.LC_TIME, "fr_FR")

        # Les paramètres : PPPPPPPPPPPPPPPPPPPPPPPPPPPPP
        'p_logFile' : 
        Quel est le fichier utilisé pour écrire tous les LOG ? 
        p_logFile est du genre "path/to/the/filename"
        exemple 'p_logFile' : D:\\Python39\\MesDEv\\Flask\\Flask_codebase2023\\file01.py'

        # Les suffixes (ajoutés aux méthodes) utilisés : SSSSSSSSSSSSSSSSSSSSS
        Ils sont 3 : 
        _tf : la méthode retourne True ou False
        _dict : la méthode retourne ce dict {'succes':True, 'msg':'fichier valide', 'data':""}
        _data : la méthode retourne une data 

        # Utilisation : UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
        # création d'une instance de la classe : 
        # l = Log('example.log')

        # Enregistrement d'un LOG : 
        # l.storeLogMessage("This is a DEBUG message ...","DEBUG")


        """
        self.logFile = p_logFile
        # Configuration du système des LOG : 
        logging.basicConfig(filename=p_logFile, encoding='utf-8', 
            format='%(levelname)s:%(message)s', level=logging.DEBUG)
        # level=logging.DEBUG
        # le niveau minimun du message pour être écrit dans le fichier de LOG est DEBUG

    def storeLogMessage_dict(self, p_message, p_level):
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

        if p_level.upper()=="DEBUG":
            logging.debug(dateLog+' '+p_message)
  
        elif p_level.upper()=="INFO":
            logging.info(dateLog+' '+p_message)

        elif p_level.upper()=="WARNING":
            logging.warning(dateLog+' '+p_message)

        elif p_level.upper()=="ERROR":
            logging.error(dateLog+' '+p_message)

        elif p_level.upper()=="CRITICAL":
            logging.critical(dateLog+' '+p_message)

        else:
            msg = "LOGGING ERROR : Le niveau de LOG utilisé " +p_level.upper()+" est inconnu. Vous devez utiliser un niveau parmi : DEBUG, INFO, WARNING, ERROR, CRITICAL"
            logging.critical(dateLog+' '+msg)
            msg = "LOGGING ERROR : Le message à enregistrer était : "+p_message
            logging.critical(dateLog+' '+msg)
            return ({'succes':False, 'msg':msg, 'data':""})                        
        return ({'succes':True, 'msg':'LOG effectué', 'data':""})
    def logFile_data(self):
        """ Retourne LE NOM du fichier des LOG. 
        Il pourra ainsi être utilisé par une instance de la classe 'Fichier'
        pour en afficher ses lignes. """
        return self.logFile


class Regex(MasterLogic):
    def __init__(self):
        # J'hérite de TOUTES les méthodes (PAS les propriétés) de la classe 'MasterLogic' !

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

    def texteEntreBalises(self, p_balise, p_text): # OK 30/11 12h47
        # retourner les texte compris entre deux balises 'mccd'. 
        # Exemple p_balise='categorie' : <mccd_categorie> texte à retourner </mccd_categorie>
        # 'self.regex' n'est pas à renseigner

        # créer les deux balises : 
        start_balise = "<mccd_"+p_balise+">"
        end_balise = "</mccd_"+p_balise+">"
        self.regex = "(?<=" + start_balise + ")(.*)(?=" +end_balise + ")"
        tr = re.findall(self.regex,p_text)
        if len(tr)>0:
            return (tr[0])
        else:
            return ("Aucun texte  à retourner entre les balises ")

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

class Poubelle(object):
    def __init__(self):
        """
        Les éléments mis au rebus vont ici 
        """
    def returnListOfFiles_dataOLD(self, p_dir):
        # un path est fourni et on retourne TOUS ses fichiers dans une liste
        listOfFiles = []


class IndicateurOLD(object):
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
        print("Dans la classe, self.indicateur : ",self.indicateur)

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
        self.indicateur = self.indicateur + p_value
    def getIndicateur(self):
        return self.indicateur
    def setIndicateur(self, p_value):
        self.indicateur = p_value

class VerifyOLD(object):
    def __init__(self):

        """
        Cette classe, avec sa méthode 'checkWithFunction', permet TOUS types de
        vérification car elle accepte en paramètre le nom d'une fonction. Elle 
        fournit une réponse True/False. 

        Exemple : 
        Savoir si une liste 'extensionCode' contient une valeur (ici '.HTML') : 
        extensionCode = ['.C','.H','.JS','.PY','.HTML','.HTM','.TXT']
        v = Verify() # créer son instance

        # créer la fonction de vérification à passer
        def isInList(p_value, p_list):
            if(p_value in p_list):
                return True
            return False

        ext = v.checkWithFunction( isInList, ['.HTML', extensionCode])

        if ext==True:
            print("Yes it contains it !")

        """  

    def pairsArePresent_tf(self, p_dict, p_list, p_instanceIndicateur):
        """
        Pour 'p_dict' c'est en général quelques une ou deux paires qui sont utilisées 
        pour rechercher la présence d'un dict dans une liste de dict. 
        Si, par exemple, la liste 'p_list' contient des dict 
        d'informations sur des fichiers dans un dossier comme celui-ci : 
        {'nom':'okTaille1', 'fichier':'okTaille1.py' ,'extension':'.py', 
        'path':'D:\temp\okTaille1.py', 'taille':2554},

        alors on pourrait vérifier sa présence avec ces paires : 
        p_dict = {'fichier':'okTaille1.py' ,'extension':'.py'}

        p_dict : dict, TOUTES ses paires sont présentes dans un dict de la liste 'p_list' ? 
        p_list : la liste à parcourir pour rechercher un dict qui contient TOUTE les paires de 'p_dict'
        p_instanceIndicateur : une instance de la classe 'Indicateur'

        """
        # Sortir de 'p_dict' les paires :
        self.lesPaires = p_dict.items()
        self.indicatorClass = p_instanceIndicateur

        # Une boucle sur 'p_list'
        for dictionnaire in p_list:
            self.indicatorClass.setIndicateur(1)
                # Une boucle sur TOUTES les paires : 
            for key, value in self.lesPaires:
                # La clé existe ? 
                self.indicatorClass.indicateur_serie(key in dictionnaire)
                if (self.indicatorClass.getIndicateur()):
                    # oui, elle existe
                    # Cette paire est présente dans le dict ? 
                    self.indicatorClass.indicateur_serie(dictionnaire[key]==value)
            if (self.indicatorClass.getIndicateur()):
                return True
        return False
        
    def verifTailleFichier(self, p_dict):
        # fichier CODE sa taille < 5000
        if p_dict['taille']>5000:
            return True
        return False

    def extensionInvalide(self, p_dict):
        # rechercher extension INVALIDE 
        if not ( (p_dict['extension'].upper() in extensionCode) or 
            (p_dict['extension'].upper() in extensionNonCode) or 
            (p_dict['extension'].upper() in extensionMc) ):
            return True
        return False

    def fichierImageManquant(self, p_dict, p_listOfFiles):
        # rechercher les fichiers MC sans fichier IMAGE 
        # 4) Rechercher si un fichier de type MC possède son équivalent en fichier IMAGE
        if (p_dict['extension'].upper() in extensionMc):
            print("Voici le type de fichier qui recherche son ami : ",p_dict['extension'].upper())
            print("Voici son dict : ",p_dict)
            d = {'fichier':p_dict['fichier']}
            # Parcourir les 'extensions' de type IMAGE 
            for ext in extensionNonCode:
                # Rechercher si un fichier avec cette ext existe
                d['extension'] = ext.lower()
                print("Extension recherchée : ",ext.lower())
                # Rechercher si un dict dans la liste p_listOfFiles contient les paires dans 'd'
                print("Le dict recherché est : ",d)
                i = Indicateur(1)
                r = self.pairsArePresent_tf(d, p_listOfFiles, i)
                print("Résultat de la recherche du fichier IMAGE : ", i.getIndicateur(),"\n")
                if (i.getIndicateur()==True):
                    return False
            return True

    def fichierMcManquant(self, p_dict, p_listOfFiles):
        # rechercher les fichiers IMAGE sans fichier MC 
        # 5) Rechercher si un fichier de type IMAGE possède son équivalent en fichier MC
        if (p_dict['extension'].upper() in extensionNonCode):
            print("Voici le type de fichier qui recherche son ami : ",p_dict['extension'].upper())
            print("Voici son dict : ",p_dict)
            d = {'fichier':p_dict['fichier'],'extension':'.mc'}
            # Parcourir les dict pour rechercher un fichier '.mc'
            i = Indicateur(1)
            r = self.pairsArePresent_tf(d, p_listOfFiles, i)
            print("Résultat de la recherche du fichier IMAGE : ", i.getIndicateur(),"\n")
            if (i.getIndicateur()==True):
                return False
            return True

    def fileIsCode(self, p_dict):
        # si le type du fichier est CODE retourne True
        if(p_dict['extension'].upper() in extensionCode):
            return True
        return False

    def fileIsNonCode(self, p_dict):
        # si le type du fichier est NONCODE retourne True
        if(p_dict['extension'].upper() in extensionNonCode):
            return True
        return False

    def fileIsMc(self, p_dict):
        # si le type du fichier est MC retourne True
        if(p_dict['extension'].upper() in extensionMc):
            return True
        return False
        
    def checkWithFunction(self, p_function, p_args):
        # 'p_function' est la fonction utilisée pour faire la vérification
        # 'p_args' DOIT être un ITERABLE (liste)
        if (p_function(*p_args)):
            return True
        return False


"""

Tester cette app : utiliser le fichier test.app



"""




