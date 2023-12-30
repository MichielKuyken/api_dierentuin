from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


from database import Base


class Manager(Base):
    __tablename__ = "managers"
    id = Column(Integer, primary_key=True, index=True)
    voornaam = Column(String)
    achternaam = Column(String)
    manager_nummer = Column(String)

    regios = relationship("Regio", back_populates="managers")


class Regio(Base):
    __tablename__ = "regios"
    id = Column(Integer, primary_key=True, index=True)
    regionaam = Column(String)
    manager_id = Column(Integer, ForeignKey("managers.id"))

    dieren = relationship("Dier", back_populates="regios")
    managers = relationship("Manager", back_populates="regios")


class Dier(Base):
    __tablename__ = "dieren"
    id = Column(Integer, primary_key=True, index=True)
    diersoort = Column(String)
    hoeveelheid = Column(Integer)
    regio_id = Column(Integer, ForeignKey("regios.id"))

    regios = relationship("Regio", back_populates="dieren")



class Eigenaar(Base):
    __tablename__ = "eigenaars"
    id = Column(Integer, primary_key=True, index=True)
    voornaam = Column(String)
    achternaam = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
