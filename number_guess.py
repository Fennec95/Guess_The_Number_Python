import random
import winsound
import time


start_time = time.time()
def play_win_sound():
    winsound.Beep(1000, 500)  # Fréquence 1000 Hz, durée 500ms
def play_wrong_sound():
    winsound.Beep(400, 200)  # Son plus grave pour mauvaise réponse

print("""Bienvenue à Devine Le Nombre ! 
Tu dois deviner le chiffre entre 1 et 100, pas de limite d'essai.
bon courage !""")

def choisir_difficulte():
    while True:
        choix = input("""Choisis la difficulté : 
(1) Facile 
(2) Normal 
(3) Difficile : """)
        if choix == "1":
            return random.randint(1, 50)
        elif choix == "2":
            return random.randint(1, 100)
        elif choix == "3":
            return random.randint(1, 500)
        else:
            print("❗ Choix invalide, entre 1, 2 ou 3.")


def intro():
    """Détermine le chiffre à deviner"""
secret_number = choisir_difficulte()


"""Demande un premier nombre avec vérification"""
while True:
        try:
            user_number = int(input("Tape un chiffre : "))
            break  # Sort de la boucle si c'est un nombre valide
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

"""Boucle du jeu"""
while user_number != secret_number:
        if user_number < secret_number:
            print("C'est plus !")
            play_wrong_sound()
        else:
            print("C'est moins !")
            play_wrong_sound()
        
        # Demander un nouveau nombre pour éviter la boucle infinie
        user_number = int(input("Tape un chiffre : "))

elapsed_time = time.time() - start_time
print(f"\n⏳ Temps écoulé : {elapsed_time:.2f} secondes !")
print("Bravo ! Tu as deviné le chiffre !")
play_win_sound()



while True:  # Boucle principale pour réessayer
    intro()
    
    # Demande si l'utilisateur veut rejouer
    while True:
        retry = input("🔄 Veux-tu réessayer ? [y/n] ").lower()
        if retry == "y":
            print("\n🔁 Redémarrage...\n")
            break  # Relance `intro`
        elif retry == "n":
            print("\n👋 Merci d'avoir joué ! À bientôt !")
            quit()
        else:
            print("❗ Y ou N, c'est pas compliqué !")

