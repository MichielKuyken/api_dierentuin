from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


from database import Base


class Manager(Base):
    __tablename__ = "managers"
    id = Column(Integer, primary_key=True, index=True)
    voornaam = Column(String)
    achternaam = Column(String)
    manager_nummer = Column(String, unique=True, index=True)

    dieren = relationship("Dier", back_populates="managers", foreign_keys="[Dier.manager_id]")


class Regio(Base):
    __tablename__ = "regios"
    id = Column(Integer, primary_key=True, index=True)
    regionaam = Column(String, unique=True)

    dieren = relationship("Dier", back_populates="regios", foreign_keys="[Dier.regio_id]")


class Dier(Base):
    __tablename__ = "dieren"
    id = Column(Integer, primary_key=True, index=True)
    diersoort = Column(String, unique=True)
    hoeveelheid = Column(Integer)
    regio_id = Column(Integer, ForeignKey("regios.id"))
    manager_id = Column(Integer, ForeignKey("managers.id"))

    regios = relationship("Regio", back_populates="dieren", foreign_keys="[Dier.regio_id]")
    managers = relationship("Manager", back_populates="dieren", foreign_keys="[Dier.manager_id]")


class Eigenaar(Base):
    __tablename__ = "eigenaars"
    id = Column(Integer, primary_key=True, index=True)
    voornaam = Column(String)
    achternaam = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
