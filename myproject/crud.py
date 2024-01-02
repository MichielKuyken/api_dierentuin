from sqlalchemy.orm import Session

import models
import schemas
import auth


def get_manager(db: Session, manager_nummer: str):
    return db.query(models.Manager).filter(models.Manager.manager_nummer == manager_nummer).first()


def get_managers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Manager).offset(skip).limit(limit).all()


def create_manager(db: Session, manager: schemas.ManagerCreate):
    db_manager = models.Manager(**manager.dict())
    db.add(db_manager)
    db.commit()
    db.refresh(db_manager)
    return "Manager successfully created!"


def delete_manager(db: Session, manager: schemas.Manager):
    db.delete(manager)
    db.commit()
    return "Manager successfully deleted!"


def update_manager(db: Session, existing_manager: models.Manager, manager_update: schemas.ManagerCreate):
    for key, value in manager_update.dict().items():
        setattr(existing_manager, key, value)
    db.commit()
    db.refresh(existing_manager)
    return "Manager successfully updated!"


def get_regio(db: Session, regionaam: str):
    return db.query(models.Regio).filter(models.Regio.regionaam == regionaam).first()


def get_regios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Regio).offset(skip).limit(limit).all()


def create_regio(db: Session, regio: schemas.RegioCreate):
    db_regio = models.Regio(**regio.dict())
    db.add(db_regio)
    db.commit()
    db.refresh(db_regio)
    return "Regio successfully created!"


def delete_regio(db: Session, regio: schemas.Regio):
    db.delete(regio)
    db.commit()
    return "Regio successfully deleted!"


def update_regio(db: Session, existing_regio: models.Regio, regio_update: schemas.RegioCreate):
    for key, value in regio_update.dict().items():
        setattr(existing_regio, key, value)
    db.commit()
    db.refresh(existing_regio)
    return "Regio successfully updated!"


def get_dier(db: Session, diersoort: str):
    return db.query(models.Dier).filter(models.Dier.diersoort == diersoort).first()


def get_dier_by_regio(db: Session, regio_id: int):
    return db.query(models.Dier).filter(models.Dier.regio_id == regio_id).all()


def get_dieren(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dier).offset(skip).limit(limit).all()


def create_dier(db: Session, dier: schemas.DierCreate):
    db_dier = models.Dier(**dier.dict())
    db.add(db_dier)
    db.commit()
    db.refresh(db_dier)
    return "Dier successfully created!"


def delete_dier(db: Session, dier: schemas.Dier):
    db.delete(dier)
    db.commit()
    return "Dier successfully deleted!"


def update_dier(db: Session, existing_dier: models.Dier, dier_update: schemas.DierCreate):
    for key, value in dier_update.dict().items():
        setattr(existing_dier, key, value)
    db.commit()
    db.refresh(existing_dier)
    return "Dier successfully updated!"


def get_eigenaar(db: Session, email: str):
    return db.query(models.Eigenaar).filter(models.Eigenaar.email == email).first()


def get_eigenaars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Eigenaar).offset(skip).limit(limit).all()


def create_eigenaar(db: Session, eigenaar: schemas.EigenaarCreate):
    hashed_password = auth.get_password_hash(eigenaar.password)
    db_eigenaar = models.Eigenaar(email=eigenaar.email, password=hashed_password, voornaam=eigenaar.voornaam, achternaam=eigenaar.achternaam)
    db.add(db_eigenaar)
    db.commit()
    db.refresh(db_eigenaar)
    return "Eigenaar successfully created!"


def delete_eigenaar(db: Session, eigenaar: schemas.Eigenaar):
    db.delete(eigenaar)
    db.commit()
    return "Eigenaar successfully deleted"
