from sqlalchemy import String, ForeignKey, Enum
from sqlalchemy.orm import (
    DeclarativeBase,
    MappedAsDataclass,
    Mapped,
    mapped_column,
    relationship
)
from datetime import datetime
from typing import List


class Base(MappedAsDataclass, DeclarativeBase):
    """

    """
    pass

class Client(Base):
    """
        This represent a Client Model
    """
    __tablename__ = "client"         
    id_client: Mapped[int] = mapped_column(init=False, primary_key=True, repr=False)    
    nom: Mapped[str] = mapped_column(String(20))
    prenom: Mapped[str] = mapped_column(String(30))
    email: Mapped[str]
    telephone: Mapped[str] = mapped_column(String(10))
    adresse: Mapped[str]

    commandes: Mapped[List["Commande"]] = relationship(back_populates="client",
                                                              cascade="all, delete-orphan", init=False, default_factory=list) 

class Produit(Base):
    """
        This represent Product Model
    """
    __tablename__ = "produit"
    id_produit: Mapped[int] = mapped_column(init=False, primary_key=True, repr=False)
    nom_produit: Mapped[str]
    categorie: Mapped[str]
    prix: Mapped[float]
    stock: Mapped[int]

    ligne_commandes: Mapped[list["Ligne_Commande"]] = relationship(back_populates="produit", 
                                                                cascade="all, delete-orphan", 
                                                                init=False)
    lignes: Mapped[list["Ligne_Commande"]] = relationship(back_populates="produit", 
                                                                cascade="all, delete-orphan", 
                                                                init=False)

class Commande(Base):
    """
        This represent Order Model
    """
    __tablename__ = "commande"
    id_commande: Mapped[int] = mapped_column(init=False, primary_key=True, repr=False)
    id_client: Mapped[int] = mapped_column(ForeignKey("client.id_client"))
    date_commande: Mapped[datetime] = mapped_column(default=None, insert_default=datetime.now())
    montant_total: Mapped[float]
    statut: Mapped[str] = mapped_column(
        Enum("Livré", "Expédié", "En préparation", "En attente"),
        default="En attente"
    )

    client: Mapped["Client"] = relationship(back_populates="commandes", init=False)
    lignes: Mapped[list["Ligne_Commande"]] = relationship(back_populates="commande", 
                                                                cascade="all, delete-orphan", 
                                                                init=False)

class Ligne_Commande(Base):
    """
        This represent Line-Order Model
    """
    __tablename__ = "ligne_Commande"
    id_ligne: Mapped[int] = mapped_column(init=False, primary_key=True, repr=False)
    id_commande: Mapped[int] = mapped_column(ForeignKey("commande.id_commande"))
    id_produit: Mapped[int] = mapped_column(ForeignKey("produit.id_produit"))
    quantite: Mapped[int]
    prix_unitaire: Mapped[float]
                                                                                                                                                                                                               
    commande: Mapped["Commande"] = relationship(back_populates="lignes")
    produit: Mapped["Produit"] = relationship(back_populates="lignes")


