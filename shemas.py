from pydantic import BaseModel, EmailStr
from typing import Optional, List, Literal
import models


#-------------------------------------------------------
class ClientBase(BaseModel):
    nom: str
    prenom: str
    email: EmailStr
    telephone: str
    adresse: str
    
    class Config:
        orm_mode = True # type: ignore

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    pass

class Client(ClientBase):
    id_client:int
    commandes:list[models.Commande] = []
    
    

#-------------------------------------------------------

class ProduitBase(BaseModel):
    nom_produit: str
    categorie: str
    prix: float
    stock: int

class ProduitCreate(ProduitBase):
    pass

class ProduitUpdate(ProduitBase):
    pass

class Produit(ProduitBase):
    id_produit:int
    class Config:
        orm_mode = True 

#-------------------------------------------------------

class CommandeBase(BaseModel):
    id_client: int
    date_commande: str
    montant_total: float
    statut: Literal["Livré", "Expédié", "En préparation", "En attente"]


class CommandeCreate(CommandeBase):
    pass

class CommandeUpdate(CommandeBase):
    pass

class Commande(CommandeBase):
    id_commande:int
    class Config:
        orm_mode = True 

#-------------------------------------------------------

class LigneCommandeBase(BaseModel):
    id_commande: int
    id_produit: int
    quantite: int
    prix_unitaire: float

class LigneCommandeCreate(LigneCommandeBase):
    pass

class LigneCommandeUpdate(LigneCommandeBase):
    pass

class LigneCommande(LigneCommandeBase):
    id_ligne:int
    class Config:
        orm_mode = True 

#-------------------------------------------------------

