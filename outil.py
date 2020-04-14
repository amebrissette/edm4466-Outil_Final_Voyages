# coding : utf-8

# Bonjour Jean-Hugues! Voici mon travail final qui consiste à la création d'un outil permettant de répertorier tous les avertissements mondiaux en temps réel.
# Vous trouverez ma démarche justifiée en #commentaires. Bonne lecture! Amélie :-) 

import requests, csv, time
from bs4 import BeautifulSoup
# Importation des fichiers nécessaires à la création du .csv. 

url = "https://voyage.gc.ca/voyager/avertissements"
# Travail de moissonnage fait à partir de cette URL choisie. 

fichier = "avertissements-voyages.csv"
# Création du futur fichier.csv. 

entetes = {
    "User-Agent": "Amélie Brissette - 5147780087 : requête envoyée dans le cadre du cours de journalisme EDM4466 à l'UQAM", 
    "From": "amelie-brissette@hotmail.com"
} 
# Création d'une carte de visite informatique (pas obligatoire à la réussite de ce travail final, mais c'est éthique)
#print(entetes) Petit test print pour confirmer que l'entêtes s'affiche correctement [réussi].

n = 0
# Création d'un compteur

site = requests.get(url, headers=entetes)
print(site.status_code)

page = BeautifulSoup(site.text, "html.parser")
# print(page) Petit test pour vérifier que tout le script contenu dans l'url s'imprime correctement [réussi].
print(page.original_encoding)

destinations = page.find_all("tr", class_="gradeX")
# Création de la variable [destinations] qui va me permettre de sélectionner le script désiré à partir de l'URL.
#print(destinations) Petit test pour voir si le scipt s'imprime au complet [réussi]. 

for destination in destinations:
    time.sleep(1)
    # Création d'une pause pour faciliter l'accès à la page Web. 
    affairesmondiales = []
    # Création d'une liste vide. 
    n += 1
    nomsPays = destination.find("a")["href"]
    urlPays = "https://voyage.gc.ca" + nomsPays
    # Création de la nouvelle URL [urlPays] qui permet de trouver toutes les URLS des différentes destinations séparément. 
    #print(urlPays) Petit test pour voir si les URLS s'impriment [réussi]. 

    items = destination.find_all("td")
    # Création de l'élément [items] qui recense toutes les données voulues, soient le nom des pays, le type d'avertissement ainsi que la date de la dernière mise à jour.
    #print(items[1].text.strip())
    #print(items[2].text.strip())
    #print(items[3].text.strip())
    # Petit test pour voir si tous les éléments voulus s'impriment sans erreur [réussi].

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

    #print("."*20)
    # Création d'un séparateur qui vient effectuer une distinction entre les groupes de données seulement dans le terminal. 

    texte = ""
    texte = texte.replace("\u2011", "")
    # Remplacement de la variable nuisant à l'impression du code; problème qui se glissait sans cesse dans l'impression de mon code, mais qui semble être lié aux ordinateurs Windows, car tout fonctionne sur un Mac. 

    affairesmondiales.append(n)
    affairesmondiales.append(urlPays)
    affairesmondiales.append(nomPays)
    affairesmondiales.append(avertissement)
    affairesmondiales.append(miseJour)
    affairesmondiales.append(infoSupp)
    print(affairesmondiales) #Petit test pour voir si le contenu de la liste s'imprime correctement [réussi].

    voyage = open(fichier,"a", encoding="utf-8")
    outil_voyage = csv.writer(voyage)
    outil_voyage.writerow(affairesmondiales) 
    # Ouverture du fichier csv contenant toutes les données sélectionnées. 

    # Fin de la création de l'outil (partie 1) en guise de projet final. 


# Je laisse ci-dessous mes démarches antérieures infructueuses qui m'ont aidée à comprendre erreurs et à arriver au code créé ci-haut. 

# Essais de création de la variable [destinations]: 
#destinations = page.find("div", class_="dataTables_wrapper").find_all
#destinations = page.find("main", class_="container").find_all
#destinations = page.find("html", class_="js backgroundsize borderimage csstransitions fontface svg details progressbar meter no-mathml cors wb-enable xsmallview").find_all 
# ERREUR: Objet introuvable à chaque fois.

#Essai de création des éléments pays, avertissement, et mise à jour:
# avertissements = pageDestination.find("tr", class_="gradeX").find_all("td")
# print(avertissements[2].text.strip())
# print(avertissements[3].text.strip())
# print(avertissements[0].text.strip())
# print(avertissements[1].text.strip())
# ERREUR : Imprime toutes les destinations, mais avec le nom de pays Acores (le premier).


