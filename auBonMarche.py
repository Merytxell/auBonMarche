import sys
from abc import ABC, abstractmethod

client_list : list["Client"]=[]
stock_list: list["Produce"]=[]

#definir une classe fruit/legumes
class Produce(ABC):
    def __init__ (self,name : str,price : float,quantity : int, unit :str ="kg" )-> None :
        self.name : str= name
        self.price : float =price
        self.quantity : int=quantity
        self.unit : str=unit

    @abstractmethod
    def get_category(self):
        pass

    def __str__(self):
        return f"{self.name}-{self.price}€,{self.quantity} {self.unit}"

    def __repr__(self):
        return self.__str__()

    def update_quantity(self,quantity):
        if quantity > self.quantity:
            return False
        self.quantity -= quantity
        return True


# Classes enfants
class Fruit(Produce):
    def get_category(self):
        return "Fruit"

class Vegetable (Produce):
    def get_category(self):
        return "Légume"



#créer une liste de fruits et légumes
stock_list =[
    Fruit("Clémentine",2.90, 6,"kg"),
    Fruit("Datte", 3.50,4,"kg"),
    Fruit("Grenade",3.50,3,"kg"),
    Fruit("Kaki",4.50,3,"kg"),
    Fruit("Kiwi",3.50,5,"kg"),
    Fruit("Mandarine",2.80,6,"kg"),
    Fruit("Orange",1.50,8,"kg"),
    Fruit("Pamplemousse",2,8,"pc"),
    Fruit("Poire", 2.50, 5,"kg"),
    Fruit("Pomme", 1.50,8,"kg"),
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

#class client , ajout panier, paiement
class Client:
    def __init__(self,name: str) -> None:
        self.name :str=name
        self.cart: list=[]
        self.total_price : float=0.0

    def add_to_cart(self,produce:Produce, quantity:int):
        if produce.update_quantity(quantity):
            self.cart.append((produce,quantity))
            self.total_price += produce.price * quantity
            print(f"{quantity}{produce.name} ajouté dans le panier")
        else:
            print(f"pas de stock de {produce.name}")

    def show_cart(self):
        print(f"{self.name}, voici votre panier")
        for produce, quantity in self.cart:
            print(f"{produce.name}: {quantity} {produce.unit} - {produce.price}€")
            # mettre le prix à jour en fonction de la commande
        print(f"Votre panier revient à : {self.total_price}€")



#choisir les produits en fonction de l'index
def display_produce() :
    print("Voici les fruits et légumes disponibles :")
    for index, produce in enumerate(stock_list,1):
        print(f"{index}. {produce}")


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
                if any(choice < 1 or choice > len(stock_list) for choice in arguments):
                    print("Choix invalide. Veuillez entrer des numéros valides.")
                else:
                    break
            except ValueError:
                print("Veuillez entrer des numéros valides.")

    return arguments


#ajout client et choix quantité
def achat() -> None:

    display_produce()
    chosen_vegetable_index=get_user_choice()

    # enregistrer client
    client_name=input("Entrez votre nom")
    client=Client(client_name)
    client_list.append(client)
    for choice in chosen_vegetable_index:
        produce = stock_list[choice - 1]
        print(f"\nVous avez choisi : {produce}")
        quantity = int(input(f"Combien de {produce.name} voulez-vous acheter ? "))
        client.add_to_cart(produce, quantity)

    client.show_cart()


#mettre à jour le stock pour chaque produit
print("Stock restant")
for produce in stock_list:
    print(produce)

#afficher les clients et les commandes
def display_client() -> None:
    if not client_list:
        print("aucun client enregistré")
        return
    print("Liste des clients et leurs commandes :")
    for client in client_list:
        for client in client_list:
            print(f"client : {client.name}")
            for produce, quantity in client.cart:
                print(f"{quantity} {produce.unit} de {produce.name} ({produce.price}€ ")
            print(f"total dépensé : {client.total_price}€")

def display_stock():
    print("\nStock actuel des fruits et légumes :")
    for produce  in stock_list:
        print(produce)


#afficher le menu :
if __name__ == "__main__":
    while True:
        print("Menu")
        print("1. faire des achats")
        print("2. Voir la liste des clients et leurs commandes")
        print("3. Voir le stock")
        print("4. Quitter")

        select = input("sélectionnez une option :")
        if select == "1":
            achat()
        if select == "2":
            display_client()
        elif select =="3":
            display_stock()
        elif select =="4":
            print("au revoir !")
        else:
            print("choix invalide")



#stock total de chaque légumes

