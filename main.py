from fastapi import FastAPI, APIRouter, HTTPException, Depends

from database import engine
from sqlalchemy.orm import Session
from models import Client, Commande, Produit, Ligne_Commande, Base
import shemas

def get_db():
    with Session(engine) as session:
        yield session


app = FastAPI()
Base.metadata.create_all(engine)
client_router = APIRouter(
    tags=["CLIENTS"],
    prefix="/clients"
)

@client_router.get("/")
def get_clients(skip: int = 0, limit: int = 100, db=Depends(get_db))->list[Client]:
    clients = []
    clients = db.query(Client).all()
    return clients[skip:skip+limit]

@client_router.get("/{client_id}/commandes")
def read_client_commende(client_id:int, db=Depends(get_db)):
        client_data = db.query(Client).filter(Client.id_client == client_id).first()
        if not client_data:
            raise HTTPException(status_code=404, detail=f"Le client avec l'id={client_id} n'existe pas")
        return client_data.commandes

@client_router.get("/{client_id}")
def get_client(client_id:int, db=Depends(get_db))->Client:
    
        client = db.query(Client).filter(Client.id_client == client_id).first()
        if client is None:
            raise HTTPException(status_code=404, detail=f"Le client avec l'id={client_id} n'existe pas")
        return client

@client_router.post("/")
def create_client(client:shemas.ClientCreate, db=Depends(get_db))->bool:
    
    create_client = Client(**client.model_dump())
    db.add(create_client)
    db.commit()
    return True

@client_router.put("/{client_id}")
def update_client(client_id:int, client:shemas.ClientUpdate, db=Depends(get_db)):
    
    client_data = db.query(Client).filter(Client.id_client == client_id).first()
    if not client_data:
        raise HTTPException(status_code=404, detail=f"Le client avec l'id={client_id} n'existe pas")
    client_data.nom = client.nom
    client_data.prenom = client.prenom
    client_data.adresse = client.adresse
    client_data.email = client.email
    client_data.telephone = client.telephone
    db.commit()

@client_router.delete("/{client_id}")
def delete_client(client_id:int, db=Depends(get_db)):
 
    client_data = db.query(Client).filter(Client.id_client == client_id).first()
    if not client_data:
        raise HTTPException(status_code=404, detail=f"Le client avec l'id={client_id} n'existe pas")
    db.delete(client_data)
    db.commit()


#---------------------------------------------------------------------------------------------------

produit_router = APIRouter(
    tags=[" PRODUITS"],
    prefix="/produits"
)

@produit_router.get("/")
def get_produits(skip: int = 0, limit: int = 100, db=Depends(get_db))->list[Produit]:

        produits = db.query(Produit).all()
        return produits[skip:skip+limit]

@produit_router.get("/{produit_id}")
def get_produit(produit_id:int, db=Depends(get_db))->Produit:

        produit = db.query(Produit).filter(Produit.id_produit == produit_id).first()
        if produit is None:
            raise HTTPException(status_code=404, detail=f"Le produit avec l'id={produit_id} n'existe pas")
        return produit

@produit_router.post("/")
def create_produit(produit:shemas.ProduitCreate, db=Depends(get_db))->bool:
    
    create_produit = Produit(**produit.model_dump())
    db.add(create_produit)
    db.commit()
    return True

@produit_router.put("/{produit_id}")
def update_produit(produit_id:int, produit:shemas.ProduitUpdate, db=Depends(get_db)):
 
        produit_data = db.query(Produit).filter(Produit.id_produit == produit_id).first()
        if not produit_data:
            raise HTTPException(status_code=404, detail=f"Le client avec l'id={produit_id} n'existe pas")
        produit_data.nom = produit.nom
        produit_data.prenom = produit.prenom
        produit_data.adresse = produit.adresse
        produit_data.email = produit.email
        produit_data.telephone = produit.telephone
        db.commit()

@produit_router.delete("/{produit_id}")
def delete_produit(produit_id:int, db=Depends(get_db)):

    produit_data = db.query(Produit).filter(Client.id_produit == produit_id).first()
    if not produit_data:
        raise HTTPException(status_code=404, detail=f"Le client avec l'id={produit_id} n'existe pas")
    db.delete(produit_data)
    db.commit()

#---------------------------------------------------------------------------------------------------

commande_router = APIRouter(
    tags=[" COMMANDES"],
    prefix="/commandes"
)

@commande_router.get("/")
def get_commandes(skip: int = 0, limit: int = 100, db=Depends(get_db))->list[Commande]:
    
        commandes = db.query(Commande).all()
        return commandes[skip:skip+limit]

@commande_router.get("/{commande_id}")
def get_commande(commande_id:int, db=Depends(get_db))->Commande:
        commande = db.query(Commande).filter(Commande.id_commande == commande_id).first()
        if commande is None:
            raise HTTPException(status_code=404, detail=f"La commande avec l'id={commande_id} n'existe pas")
        return commande

@commande_router.post("/")
def create_commande(commande:shemas.CommandeCreate, db=Depends(get_db))->bool:
    
    create_commande = Commande(**commande.model_dump())
    db.add(create_commande)
    db.commit()
    return True

@commande_router.put("/{commande_id}")
def update_commande(commande_id:int, commande:shemas.Commande, db=Depends(get_db)):

        commande_data = db.query(Commande).filter(Commande.id_commande == commande_id).first()
        if not commande_data:
            raise HTTPException(status_code=404, detail=f"La commande avec l'id={commande_id} n'existe pas")
        commande_data.nom = commande.nom
        commande_data.prenom = commande.prenom
        commande_data.adresse = commande.adresse
        commande_data.email = commande.email
        commande_data.telephone = commande.telephone
        db.commit()

@commande_router.delete("/{commande_id}")
def delete_commande(commande_id:int, db=Depends(get_db)):

        commande_data = db.query(Commande).filter(Client.id_commande == commande_id).first()
        if not commande_data:
            raise HTTPException(status_code=404, detail=f"Le commande avec l'id={commande_id} n'existe pas")
        
        db.delete(commande_data)
        db.commit()

#---------------------------------------------------------------------------------------------------

ligne_commande_router = APIRouter(
    tags=[" LIGNE_COMMANDE"],
    prefix="/lignes"
)

@ligne_commande_router.post('/')
def create_ligne_commande(ligne_commande:shemas.LigneCommandeCreate, db=Depends(get_db))->bool:

    create_ligne_commande = Ligne_Commande(**ligne_commande.model_dump())
    db.add(create_ligne_commande)
    db.commit()
    return True

app.include_router(client_router)
app.include_router(commande_router)
app.include_router(ligne_commande_router)
app.include_router(produit_router)