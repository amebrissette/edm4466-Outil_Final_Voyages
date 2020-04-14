# coding : utf-8

# Bonjour Jean-Hugues! Voici la suite de mon travail final qui consiste à la création d'un deuxième script me permettant de relever les changements dans les avertissements mondiaux. 
# Vous trouverez ma démarche justifiée en #commentaires. Bonne lecture! Amélie :-) 

import csv, requests, time 
from bs4 import BeautifulSoup
# Importation des fichiers nécessaires à la création de l'outil complémentaire. 

entetes = {
    "User-Agent": "Amélie Brissette - 5147780087 : requête envoyée dans le cadre du cours de journalisme EDM4466 à l'UQAM", 
    "From": "amelie-brissette@hotmail.com"
} 
# Création d'une carte de visite informatique (pas obligatoire à la réussite de ce travail final, mais c'est éthique)
#print(entetes) Petit test print pour confirmer que l'entêtes s'affiche correctement [réussi].

url = "https://voyage.gc.ca/voyager/avertissements"
# Travail de moissonnage fait à partir de cette URL choisie précédemment. 

fichier2 = "nouveaux-avertissements-voyages.csv"
# Création du futur fichier.csv. 

moisson = "avertissements-voyages.csv"
# Importation du fichier.csv créé à l'aide du code contenu dans [outil.py].

f = open(moisson)
alertes = csv.reader(f)
# Ouverture du fichier.csv.

n = 0
#Création d'un compteur

site = requests.get(url, headers=entetes)
print(site.status_code)

page = BeautifulSoup(site.text, "html.parser")
# print(page) Petit test pour vérifier que tout le script contenu dans l'url s'imprime correctement [réussi].

destinations = page.find_all("tr", class_="gradeX")
# Création de la variable [destinations] qui va me permettre de sélectionner le script désiré à partir de l'URL.
#print(destinations) Petit test pour voir si le scipt s'imprime au complet [réussi]. 

for destination in destinations:
    time.sleep(1)
    # Création d'une pause pour faciliter l'accès à la page Web. 
    n += 1
    nomsPays = destination.find("a")["href"]
    urlPays = "https://voyage.gc.ca" + nomsPays
    # Création de la nouvelle URL [urlPays] qui permet de trouver toutes les URLS des différentes destinations séparément. 

    items = destination.find_all("td")
    # Création de l'élément [items] qui recense toutes les données pertinentes, soient le nom des pays, le type d'avertissement (l'élément que nous souhaitons extraire), ainsi que la date de la dernière mise à jour.

    nomPays = items[1].text.strip()
    # Création de l'élément [nomPays] qui correspond au nom de la destination. 
    avertissement = items[2].text.strip()
    # Création de l'élément [avertissement] qui correspond au type d'avertissement.
    miseJour = items[3].text.strip()
    # Création de l'élément [miseJour] qui correspond à la date de la dernière mise à jour effectuée. 

    siteDestination = requests.get(urlPays, headers=entetes)
    pageDestination = BeautifulSoup(siteDestination.text, "html.parser")

    try: 
        infoSupp = pageDestination.find("div", class_="AdvisoryContainer RegionalAdv").find("p").text.strip()
    except: 
        infoSupp = "Aucune information supplémentaire."
    # Création de l'élément [infoSupp] dans une boucle qui apporte des informations supplémentaires quant aux régions touchées et au danger présenté.
    #print(infoSupp) Petit test pour voir si les informations supplémentaires s'impriment [réussi].

    f = open(moisson, encoding="utf-8")
    alertes = csv.reader(f)
    # Réouverture du fichier.csv.

    for alerte in alertes:
        # Création de la boucle qui permet de sélectionner les données voulues, ici les caractères "2" et "3" qui correspondent au nom du pays et au type d'avertissement.
        nouvelAvertissement = []
        # Création d'une liste vide.
        
        try:
            if alerte[2] == nomPays:
                if alerte[3] != avertissement:
                    print(nomPays, alerte[3], avertissement, "Un changement noté pour ce pays.")
                if alerte[3] == avertissement:
                    print(nomPays, alerte[3], avertissement, "Aucun changement.")

                nouvelAvertissement.append(n)
                nouvelAvertissement.append(urlPays)
                nouvelAvertissement.append(nomPays)
                nouvelAvertissement.append(avertissement)
                nouvelAvertissement.append(miseJour)
                nouvelAvertissement.append(infoSupp)
                print(nouvelAvertissement) #Petit test pour voir si le contenu de la liste s'imprime correctement [réussi].
                # Création de la liste avec toutes les nouvelles données actualisées. 

        except:
            x = 0
        # Création de la veille qui permettra de noter lorsque le type d'avertissement a été modifié ou supprimé en plus de noter la destination correspondante. 
        
        alertes = open(fichier2,"a", encoding="utf-8")
        outil2voyage = csv.writer(alertes)
        outil2voyage.writerow(nouvelAvertissement) 
        # Ouverture du fichier csv contenant toutes données actualisées. 


        # Fin de la création de l'outil (partie 2) en guise de projet final. 

