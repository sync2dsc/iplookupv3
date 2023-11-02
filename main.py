from colorama import Fore, init
from ping3 import ping
import os

# Initialisation de Colorama pour la coloration du texte dans la console
init(autoreset=True)

# Fonction pour afficher le menu
def afficher_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Effacer la console
    print(Fore.YELLOW + "Menu :")
    print("1. Pinger une adresse IP")
    print("2. Informations sur une adresse IP")
    print("3. Quitter")

# Fonction pour pinger une adresse IP en utilisant la bibliothèque ping3
def pinger_ip(adresse_ip):
    os.system('cls' if os.name == 'nt' else 'clear')  # Effacer la console
    print(Fore.GREEN + "Ping de l'adresse IP : " + adresse_ip)
    temps_de_reponse = ping(adresse_ip)
    
    if temps_de_reponse is not None:
        print(Fore.GREEN + f"Temps de réponse : {temps_de_reponse} ms")
        print(Fore.GREEN + "L'adresse IP est accessible.")
    else:
        print(Fore.RED + "L'adresse IP n'a pas répondu au ping.")
    input("Appuyez sur Entrée pour continuer...")

# Fonction pour obtenir des informations sur une adresse IP
def obtenir_informations_ip():
    os.system('cls' if os.name == 'nt' else 'clear')  # Effacer la console
    adresse_ip = input("Entrez l'adresse IP que vous souhaitez cibler : ")
    url = f"https://ipinfo.io/{adresse_ip}/json?token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(Fore.GREEN + "Informations sur l'adresse IP : " + adresse_ip)
        print("Pays :", data.get("country"))
        print("Ville :", data.get("city"))
        print("Région :", data.get("region"))
        print("Code Postal :", data.get("postal"))
        print("Longitude :", data.get("loc").split(",")[1])
        print("Latitude :", data.get("loc").split(",")[0])

        isp = data.get("org")
        if "vpn" in isp.lower():
            print("VPN détecté.")
        elif "proxy" in isp.lower():
            print("Proxy détecté.")
        else:
            print("Pas de VPN ou de proxy détecté.")

        # Vérification approximative de l'utilisation d'un relais IP (TOR si tu préfères)
        if "relay" in isp.lower():
            print("Utilisation d'un relais IP détectée (approximativement).")
    else:
        print(Fore.RED + "Erreur lors de la récupération des informations de l'adresse IP.")

        # Vérification approximative de l'IP dynamique ou statique
        try:
            ipwhois = IPWhois(adresse_ip)
            result = ipwhois.lookup_rdap()
            if "allocationStatus" in result:
                if result["allocationStatus"] == "assigned":
                    print("IP statique (approximativement).")
                else:
                    print("IP dynamique (approximativement).")
        except Exception as e:
            print(Fore.RED + f"Erreur lors de la vérification de l'IP : {str(e)}")
    input("Appuyez sur Entrée pour continuer...")

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
        input("Appuyez sur Entrée pour continuer...")
            
