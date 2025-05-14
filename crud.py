from sqlalchemy import Engine

from sqlalchemy.orm import Session
from models import Client, Commande, Produit, Ligne_Commande
from fastapi import HTTPException
from typing import List
import shemas

def create_client(engine:Engine, client:shemas.ClientCreate)->bool:
    with Session(engine) as session:
        create_client = Client(**client.model_dump())
        session.add(create_client)
        session.commit()
    return True

def get_client(engine:Engine, client_id:int)->Client:
    with Session(engine) as session:
        client = session.query(Client).filter(Client.id_client == client_id).first()
        if client is None:
            raise HTTPException(status_code=404, detail=f"Le client avec l'id={client_id} n'existe pas")
        return client

def get_clients(engine:Engine, skip: int = 0, limit: int = 100)->List[Client]:
    with Session(engine) as session:
        clients = session.query(Client).all()
        return clients[skip:skip+limit]
    
def update_client(engine:Engine, client_id:int, client:shemas.ClientUpdate):
    with Session(engine) as session:
        client_data = session.query(Client).filter(Client.id_client == client_id).first()
        if not client_data:
            raise HTTPException(status_code=404, detail=f"Le client avec l'id={client_id} n'existe pas")
        client_data.nom = client.nom
        client_data.prenom = client.prenom
        client_data.adresse = client.adresse
        client_data.email = client.email
        client_data.telephone = client.telephone
        session.commit()

def delete_client(engine: Engine, client_id:int):
    with Session(engine) as session:
        client_data = session.query(Client).filter(Client.id_client == client_id).first()
        if not client_data:
            raise HTTPException(status_code=404, detail=f"Le client avec l'id={client_id} n'existe pas")
        session.delete(client_data)
        session.commit()

def read_client_commende(engine:Engine, client_id:int):
    with Session(engine) as session:
        client_data = session.query(Client).filter(Client.id_client == client_id).first()
        if not client_data:
            raise HTTPException(status_code=404, detail=f"Le client avec l'id={client_id} n'existe pas")
        return client_data.commandes
    
#--------------------------------------------------------------------------------------------------------------

def create_produit(engine:Engine, produit:shemas.ProduitCreate)->bool:
    with Session(engine) as session:
        create_produit = Produit(**produit.model_dump())
        session.add(create_produit)
        session.commit()
    return True

def get_produit(engine:Engine, produit_id:int)->Produit:
    with Session(engine) as session:
        produit = session.query(Produit).filter(Produit.id_produit == produit_id).first()
        if produit is None:
            raise HTTPException(status_code=404, detail=f"Le produit avec l'id={produit_id} n'existe pas")
        return produit

def get_produits(engine:Engine, skip: int = 0, limit: int = 100)->List[Produit]:
    with Session(engine) as session:
        produits = session.query(Produit).all()
        return produits[skip:skip+limit]
    
def update_produit(engine:Engine, produit_id:int, produit:shemas.ProduitUpdate):
    with Session(engine) as session:
        produit_data = session.query(Produit).filter(Produit.id_produit == produit_id).first()
        if not produit_data:
            raise HTTPException(status_code=404, detail=f"Le client avec l'id={produit_id} n'existe pas")
        produit_data.nom = produit.nom
        produit_data.prenom = produit.prenom
        produit_data.adresse = produit.adresse
        produit_data.email = produit.email
        produit_data.telephone = produit.telephone
        session.commit()

def delete_produit(engine: Engine, produit_id:int):
    with Session(engine) as session:
        produit_data = session.query(Produit).filter(Client.id_produit == produit_id).first()
        if not produit_data:
            raise HTTPException(status_code=404, detail=f"Le client avec l'id={produit_id} n'existe pas")
        session.delete(produit_data)
        session.commit()

def search_produits(engine:Engine, query:str, skip: int =0, limit: int = 100)->list[shemas.Produit]:
    with Session(engine) as session:
        produits = session.query(Produit).filter()


#--------------------------------------------------------------------------------------------------------------

def create_commande(engine:Engine, commande:shemas.CommandeCreate)->bool:
    with Session(engine) as session:
        create_commande = Commande(**commande.model_dump())
        session.add(create_commande)
        session.commit()
    return True

def get_commande(engine:Engine, commande_id:int)->Commande:
    with Session(engine) as session:
        commande = session.query(Commande).filter(Commande.id_commande == commande_id).first()
        if commande is None:
            raise HTTPException(status_code=404, detail=f"La commande avec l'id={commande_id} n'existe pas")
        return commande

def get_commandes(engine:Engine, skip: int = 0, limit: int = 100)->List[Commande]:
    with Session(engine) as session:
        commandes = session.query(Commande).all()
        return commandes[skip:skip+limit]

def update_commande(engine:Engine, commande_id:int, commande:shemas.Commande):
    with Session(engine) as session:
        commande_data = session.query(Commande).filter(Commande.id_commande == commande_id).first()
        if not commande_data:
            raise HTTPException(status_code=404, detail=f"La commande avec l'id={commande_id} n'existe pas")
        commande_data.nom = commande.nom
        commande_data.prenom = commande.prenom
        commande_data.adresse = commande.adresse
        commande_data.email = commande.email
        commande_data.telephone = commande.telephone
        session.commit()

def delete_commande(engine: Engine, commande_id:int):
    with Session(engine) as session:
        commande_data = session.query(Commande).filter(Client.id_commande == commande_id).first()
        if not commande_data:
            raise HTTPException(status_code=404, detail=f"Le commande avec l'id={commande_id} n'existe pas")
        
        session.delete(commande_data)
        session.commit()

#--------------------------------------------------------------------------------------------------------------

def create_ligne_commande(engine:Engine, ligne_commande:shemas.LigneCommandeCreate)->bool:
    with Session(engine) as session:
        create_ligne_commande = Ligne_Commande(**ligne_commande.model_dump())
        session.add(create_ligne_commande)
        session.commit()
    return True

def get_ligne_commande(engine:Engine, ligne_commande_id:int)->Ligne_Commande:
    with Session(engine) as session:
        ligne_commande = session.query(Ligne_Commande).filter(Ligne_Commande.id_ligne == ligne_commande_id).first()
        if ligne_commande is None:
            raise HTTPException(status_code=404, detail=f"La ligne_commande avec l'id={ligne_commande_id} n'existe pas")
        return ligne_commande

def get_ligne_commandes(engine:Engine, skip: int = 0, limit: int = 100)->List[Ligne_Commande]:
    with Session(engine) as session:
        ligne_commandes = session.query(Ligne_Commande).all()
        return ligne_commandes[skip:skip+limit]

def update_ligne_commande(engine:Engine, ligne_commande_id:int, ligne_commande:shemas.LigneCommande):
    with Session(engine) as session:
        ligne_commande_data = session.query(Ligne_Commande).filter(Ligne_Commande.id_ligne == ligne_commande_id).first()
        if not ligne_commande_data:
            raise HTTPException(status_code=404, detail=f"La ligne_commande avec l'id={ligne_commande} n'existe pas")
        ligne_commande_data.nom = ligne_commande.nom
        ligne_commande_data.prenom = ligne_commande.prenom
        ligne_commande_data.adresse = ligne_commande.adresse
        ligne_commande_data.email = ligne_commande.email
        ligne_commande_data.telephone = ligne_commande.telephone
        session.commit()

def delete_ligne_commande(engine: Engine, ligne_commande_id:int):
    with Session(engine) as session:
        ligne_commande_data = session.query(Commande).filter(Client.id_commande == ligne_commande_id).first()
        if not ligne_commande_data:
            raise HTTPException(status_code=404, detail=f"La ligne_commande avec l'id={ligne_commande_id} n'existe pas")
        
        session.delete(ligne_commande_data)
        session.commit()
