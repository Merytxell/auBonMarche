#definir une classe fruit/legumes
class Vegetable:
    def __init__ (self,name,price,stock):
        self.name= name
        self.price=price
        self.stock=stock

    def __str__(self):
        return f"{self.name}-{self.price}€,{self.stock}kg en stock"

    def __repr__(self):
        return self.__str__()


#créer une liste de fruits et légumes
vegetables_list =[
    Vegetable("Clémentine",2.90, 6),
    Vegetable("Datte", 3.50,4),
    Vegetable("Grenade",3.50,3),
    Vegetable("Kaki",4.50,3),
    Vegetable("Kiwi",3.50,5),
    Vegetable("Mandarine",2.80,6),
    Vegetable("Orange",1.50,8),
    Vegetable("Pamplemousse",2,8),
    Vegetable("Poire", 2.50, 5),
    Vegetable("Pomme", 1.50,8),
    Vegetable("Carotte",1.30,7),
    Vegetable("Choux de Bruxelles", 4, 4),
    Vegetable("Chou vert",2.5,12),
    Vegetable("Courge Butternut", 2.50, 6),
    Vegetable("Endive",2.50,5),
    Vegetable("Epinard",2.60,4),
    Vegetable("Poireau",1.20,5),
    Vegetable("Potiron", 2.50,6),
    Vegetable("Radis noir",5,10),
    Vegetable("Salsifis",2.5,3)
]


#créer un menu où l'utilisateur pourra choisir ses achats


#mettre à jour un stock pour chaque produit
for vegetable in vegetables_list:
    print(vegetable)
#afficher la liste des clients avec total achat
#stock total de chaque légumes

