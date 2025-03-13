import sys

client_list : list["Client"]=[]
stock_list: list["Vegetable"]=[]

#definir une classe fruit/legumes
class Vegetable:
    def __init__ (self,name : str,price : float,quantity : int, unit :str ="kg" )-> None :
        self.name : str= name
        self.price : float =price
        self.quantity : int=quantity
        self.unit : str=unit

    def __str__(self):
        return f"{self.name}-{self.price}€,{self.quantity} {self.unit}"

    def __repr__(self):
        return self.__str__()

    def update_quantity(self,quantity):
        if quantity > self.quantity:
            return False
        self.quantity -= quantity
        return True


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

#class client , ajout panier, paiement
class Client:
    def __init__(self,name: str) -> None:
        self.name :str=name
        self.cart: list=[tuple[Vegetable, int]]
        self.total_price : float=0.0

    def add_to_cart(self,vegetable:Vegetable,quantity:int):
        if vegetable.update_quantity(quantity):
            self.cart.append((vegetable,quantity))
            self.total_price += vegetable.price * quantity
            print(f"{quantity}{vegetable.name} ajouté dans le panier")
        else:
            print(f"pas de stock de {vegetable.name}")

    def show_cart(self):
        print(f"{self.name}, voici votre panier")
        for vegetable, quantity in self.cart:
            print(f"{vegetable.name}: {quantity} {vegetable.unit} - {vegetable.price}€")
            # mettre le prix à jour en fonction de la commande
        print(f"Votre panier revient à : {self.total_price}€")



#choisir les produits en fonction de l'index
def display_vegetables() :
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

    return arguments


#ajout client et choix quantité
def achat() -> None:

    display_vegetables()
    chosen_vegetable_index=get_user_choice()

    # enregistrer client
    client_name=input("Entrez votre nom")
    client=Client(client_name)
    client_list.append(client)
    for choice in chosen_vegetable_index:
        vegetable = vegetables_list[choice - 1]
        print(f"\nVous avez choisi : {vegetable}")
        quantity = int(input(f"Combien de {vegetable.name} voulez-vous acheter ? "))
        client.add_to_cart(vegetable, quantity)

    client.show_cart()


#mettre à jour le stock pour chaque produit
print("Stock restant")
for vegetable in vegetables_list:
    print(vegetable)

#afficher les clients et les commandes
def display_client() -> None:
    if not client_list:
        print("aucun client enregistré")
        return
    print("Liste des clients et leurs commandes :")
    for client in client_list:
        for client in client_list:
            print(f"client : {client.name}")
            for vegetable, quantity in client.cart:
                print(f"{quantity} {vegetable.unit} de {vegetable.name} ({vegetable.price}€ ")
            print(f"total dépensé : {client.total_price}€")

def display_stock():
    print("\nStock actuel des fruits et légumes :")
    for vegetable in vegetables_list:
        print(vegetable)


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

