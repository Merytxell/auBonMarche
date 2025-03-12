import sys

#definir une classe fruit/legumes
class Vegetable:
    def __init__ (self,name,price,quantity, unit="kg"):
        self.name= name
        self.price=price
        self.quantity=quantity
        self.unit=unit

    def __str__(self):
        return f"{self.name}-{self.price}€,{self.quantity} {self.unit}"

    def __repr__(self):
        return self.__str__()


#créer une liste de fruits et légumes
vegetables_list =[
    Vegetable("Clémentine",2.90, 6,"kg"),
    Vegetable("Datte", 3.50,4,"kg"),
    Vegetable("Grenade",3.50,3,"kg"),
    Vegetable("Kaki",4.50,3,"kg"),
    Vegetable("Kiwi",3.50,5,"kg"),
    Vegetable("Mandarine",2.80,6,"kg"),
    Vegetable("Orange",1.50,8,"kg"),
    Vegetable("Pamplemousse",2,8,"pc"),
    Vegetable("Poire", 2.50, 5,"kg"),
    Vegetable("Pomme", 1.50,8,"kg"),
    Vegetable("Carotte",1.30,7,"kg"),
    Vegetable("Choux de Bruxelles", 4, 4,"kg"),
    Vegetable("Chou vert",2.5,12,"pc"),
    Vegetable("Courge Butternut", 2.50, 6,"pc"),
    Vegetable("Endive",2.50,5,"kg"),
    Vegetable("Epinard",2.60,4, "kg"),
    Vegetable("Poireau",1.20,5,"kg"),
    Vegetable("Potiron", 2.50,6,"pc"),
    Vegetable("Radis noir",5,10,"pc"),
    Vegetable("Salsifis",2.5,3,"kg")
]

class Client:
    def __init__(self,name):
        self.name=name

#créer un menu où l'utilisateur pourra choisir ses achats
def display_vegetables(vegetables_list):
    print("Voici les fruits et légumes disponibles :")
    for index, vegetable in enumerate(vegetables_list,1):
        print(f"{index}. {vegetable}")



def get_user_choice():
    arguments = []
    if len(sys.argv) > 1:
        # Si des arguments sont passés, on les récupère et on fait une liste
        arguments = sys.argv[1:]
    else:
        # Sinon, on demande à l'utilisateur de saisir ses choix
        while True:
            try:
                choice_input = input("Servez-vous (saisir des numéros séparés par des espaces) : ")
                choice_list = choice_input.split()  # Séparer les numéros par des espaces
                arguments = [int(choice) for choice in choice_list]  # Convertir en int
                if any(choice < 1 or choice > len(vegetables_list) for choice in arguments):
                    print("Choix invalide. Veuillez entrer des numéros valides.")
                else:
                    break
            except ValueError:
                print("Veuillez entrer des numéros valides.")

    # Afficher les articles choisis
    print("\nVous avez choisi :")
    for choice in arguments:
        print(f"- {vegetables_list[choice - 1]}")

    return arguments


display_vegetables(vegetables_list)
chosen_vegetable_index=get_user_choice()

#demander à l'utilisateur quelle quantité il prend
#enregistrer client
#mettre le prix à jour en fonction de la commande
#mettre à jour le stock pour chaque produit


#afficher la liste des clients avec total achat
#stock total de chaque légumes

