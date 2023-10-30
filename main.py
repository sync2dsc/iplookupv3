from colorama import Fore, init
import requests
from ipwhois import IPWhois
import os

# Initialise Colorama pour la coloration du texte dans la console
init(autoreset=True)

# Clé API ipinfo.io
api_key = "461a2087be663e"

# Fonction pour afficher le menu
def display_menu():
    print(Fore.YELLOW + "Menu:")
    print("1. Ping une adresse IP")
    print("2. Informations sur une adresse IP")
    print("3. Quitter")

# Fonction pour pinger une adresse IP
def ping_ip(ip_address):
    print(Fore.GREEN + "Pinging l'adresse IP : " + ip_address)
    
    # Utilisation de la commande ping pour pinger l'adresse IP
    response = os.system(f"ping -c 4 {ip_address}")  # Exécute 4 requêtes de ping

    if response == 0:
        print(Fore.GREEN + "L'adresse IP est accessible.")
    else:
        print(Fore.RED + "L'adresse IP n'a pas répondu au ping.")

# Fonction pour obtenir des informations sur une adresse IP
def get_ip_info():
    ip_address = input("Entrez l'adresse IP que vous souhaitez cibler : ")
    url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(Fore.GREEN + "Informations sur l'adresse IP : " + ip_address)
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
            ipwhois = IPWhois(ip_address)
            result = ipwhois.lookup_rdap()
            if "allocationStatus" in result:
                if result["allocationStatus"] == "assigned":
                    print("IP statique (approximativement).")
                else:
                    print("IP dynamique (approximativement).")
        except Exception as e:
            print(Fore.RED + f"Erreur lors de la vérification de l'IP : {str(e)}")

# Boucle du menu
while True:
    display_menu()
    choice = input("Entrez le numéro de votre choix : ")

    if choice == "1":
        ip_address = input("Entrez l'adresse IP à pinger : ")
        ping_ip(ip_address)
    elif choice == "2":
        get_ip_info()
    elif choice == "3":
        print(Fore.RED + "Sortie du programme.")
        break
    else:
        print(Fore.RED + "Choix invalide. Veuillez entrer 1, 2 ou 3.")
