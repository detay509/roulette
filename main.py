import random
import pickle
def chaine(nom):
    for i in nom:
        if i.isupper():
            return True
    return False

def enregistrer():
    nom_utilisateur=input("Entrer votre nom sans espace ni de lettre majuscule: ")
    while True:
            if " " in nom_utilisateur or chaine(nom_utilisateur):
                nom_utilisateur = input("Votre nom doit respecter les consigne! Merci d'avoir reesayer :")
                continue
                 
            return nom_utilisateur

try:
    with open('database.pkl', 'rb') as file:
        database = pickle.load(file)
except (FileNotFoundError, EOFError):
    database = {}

nom_utilisateur=enregistrer()         
    
if nom_utilisateur in database:
    
            ancien_score = database[nom_utilisateur]['score']
            print(f"Bon retour, {nom_utilisateur} ! Votre score précédent était {ancien_score}.")
else:
    ancien_score=0

reponse=" "
if nom_utilisateur not in database:
        database[nom_utilisateur] = {'score': 0}
        ancien_score=0

while ( not reponse.lower()=="k"):
    nombre_ordi=random.randint(0,48)
    essais=5
    while(essais>0):

        try:
            nombre_utilisateur=int(input("Entrez un nombre entre 0-48 ou gen "+str(essais)+" essais :"))
            if 0 <= nombre_utilisateur <=48 :
                if(nombre_utilisateur < nombre_ordi):
                    print("Vous avez perdu car vous avez choisi un nombre inferieur")
                elif(nombre_utilisateur > nombre_ordi):
                    print("Vous avez perdu car vous avez choisi un nombre superieur")


                else:
                    print("Vous avez gagne .Bravo")
                    score_gagne = essais  * 30
                    database[nom_utilisateur]['score'] += score_gagne
                    
                    
                    
                    break
                essais-=1
                
            else:
                print("Le nombre doit etre entre  0 a 48")
        except ValueError:
            print("Entrer un entier")
    score_gagne=essais*30
   
    if(essais==0):
        print("Plus de chance.")
        print("Le nombre cache etait :"+str(nombre_ordi))
    print(f"Votre score actuel  : {database[nom_utilisateur]['score']}")

        
    
    reponse=input("Voulez-vous continuez? pressez n'importe touche pour oui K pour nom :")
    
    if(reponse.lower() =="k"):
        with open('database.pkl', 'wb') as file:
                pickle.dump(database, file)
        print("Merci !!!!")
        break
                    
