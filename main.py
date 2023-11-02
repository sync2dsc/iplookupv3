from colorama import Fore, init
from ping3 import ping, verbose_ping

# Initialisation de Colorama pour la coloration du texte dans la console
init(autoreset=True)

# Fonction pour afficher le menu
def afficher_menu():
    print(Fore.YELLOW + "Menu :")
    print("1. Pinger une adresse IP")
    print("2. Informations sur une adresse IP")
    print("3. Quitter")

# Fonction pour pinger une adresse IP en utilisant la bibliothèque ping3
def pinger_ip(adresse_ip):
    print(Fore.GREEN + "Ping de l'adresse IP : " + adresse_ip)
    temps_de_reponse = ping(adresse_ip)
    
    if temps_de_reponse is not None:
        print(Fore.GREEN + f"Temps de réponse : {temps_de_reponse} ms")
        print(Fore.GREEN + "L'adresse IP est accessible.")
    else:
        print(Fore.RED + "L'adresse IP n'a pas répondu au ping.")

# Fonction pour obtenir des informations sur une adresse IP
def obtenir_informations_ip():
    adresse_ip = input("Entrez l'adresse IP que vous souhaitez cibler : ")
    # Ajoutez votre code pour obtenir des informations sur l'adresse IP ici.

# Boucle du menu principal
while True:
    afficher_menu()
    choix = input("Entrez votre choix (1, 2 ou 3) : ")

    if choix == "1":
        adresse_ip = input("Entrez l'adresse IP à pinger : ")
        pinger_ip(adresse_ip)
    elif choix == "2":
        obtenir_informations_ip()
    elif choix == "3":
        print(Fore.RED + "Fermeture du programme.")
        break
    else:
        print(Fore.RED + "Choix invalide. Veuillez entrer 1, 2 ou 3.")
        
