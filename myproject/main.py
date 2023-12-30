from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import crud
import models
import schemas
from database import SessionLocal, engine
import os
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import auth


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


security = HTTPBasic()


origins = [
    "https://michielkuyken.github.io/fomula1_api.github.io/",
    "file:///C:/Users/Eigenaar/Documents/2CCS/API%20development/API%20website/index.html"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    eigenaar = auth.authenticate_eigenaar(db, form_data.username, form_data.password)
    if not eigenaar:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": eigenaar.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/managers/")
def create_manager(manager: schemas.ManagerCreate, db: Session = Depends(get_db)):
    managers = crud.get_manager(db, manager_nummer=manager.manager_nummer)
    if managers:
        raise HTTPException(status_code=400, detail="Manager already registred")
    return crud.create_manager(db=db, manager=manager)


@app.get("/managers/", response_model=list[schemas.Manager])
def read_managers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    managers = crud.get_managers(db, skip=skip, limit=limit)
    return managers


@app.get("/managers/{manager_nummer}", response_model=schemas.Manager)
def read_manager(manager_nummer: str, db: Session = Depends(get_db)):
    manager = crud.get_manager(db, manager_nummer=manager_nummer)
    if manager is None:
        raise HTTPException(status_code=404, detail="Manager not found")
    return manager


@app.delete("/managers/{manager_nummer}")
def delete_manager(manager_nummer: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_eigenaar = auth.get_current_eigenaar(db, token)
    if not current_eigenaar:
        raise HTTPException(status_code=401, detail="Eigenaar not authenticated")
    manager = crud.get_manager(db, manager_nummer=manager_nummer)
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")
    return crud.delete_manager(db=db, manager=manager)


@app.put("/managers/{manager_nummer}")
def update_manager(manager_nummer: str, manager_update: schemas.ManagerCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_eigenaar = auth.get_current_eigenaar(db, token)
    if not current_eigenaar:
        raise HTTPException(status_code=401, detail="Eigenaar not authenticated")
    manager = crud.get_manager(db, manager_nummer=manager_nummer)
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")
    updated_manager = crud.update_manager(db, manager, manager_update)
    return updated_manager


@app.post("/regios/")
def create_regio(regio: schemas.RegioCreate, db: Session = Depends(get_db)):
    regios = crud.get_regio(db, regionaam=regio.regionaam)
    if regios:
        raise HTTPException(status_code=400, detail="Regio already exists")
    return crud.create_regio(db=db, regio=regio)


@app.get("/regios/", response_model=list[schemas.Regio])
def read_regios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    regios = crud.get_regios(db, skip=skip, limit=limit)
    return regios


@app.get("/regios/{regionaam}", response_model=schemas.Regio)
def read_regio(regionaam: str, db: Session = Depends(get_db)):
    regio = crud.get_regio(db, regionaam=regionaam)
    if regio is None:
        raise HTTPException(status_code=404, detail="Regio not found")
    return regio


@app.delete("/regios/{regionaam}")
def delete_regio(regionaam: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_eigenaar = (auth.get_current_eigenaar(db, token))
    if not current_eigenaar:
        raise HTTPException(status_code=401, detail="Eigenaar not authenticated")
    regio = crud.get_regio(db, regionaam=regionaam)
    if not regio:
        raise HTTPException(status_code=404, detail="Regio not found")
    return crud.delete_regio(db=db, regio=regio)


@app.put("/regios/{regionaam}")
def update_regio(regionaam: str, regio_update: schemas.RegioCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_eigenaar = auth.get_current_eigenaar(db, token)
    if not current_eigenaar:
        raise HTTPException(status_code=401, detail="Eigenaar not authenticated")
    regio = crud.get_regio(db, regionaam=regionaam)
    if not regio:
        raise HTTPException(status_code=404, detail="Regio not found")
    updated_regio = crud.update_regio(db, regio, regio_update)
    return updated_regio


@app.post("/dieren/")
def create_dier(dier: schemas.DierCreate, db: Session = Depends(get_db)):
    dieren = crud.get_dier(db, diersoort=dier.diersoort)
    if dieren:
        raise HTTPException(status_code=400, detail="Animal already exists")
    return crud.create_dier(db=db, dier=dier)


@app.get("/dieren/", response_model=list[schemas.Dier])
def read_dieren(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dieren = crud.get_dieren(db, skip=skip, limit=limit)
    return dieren


@app.get("/dieren/{diersoort}", response_model=schemas.Dier)
def read_dier(diersoort: str, db: Session = Depends(get_db)):
    dier = crud.get_dier(db, diersoort=diersoort)
    if dier is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    return dier


@app.get("/dier/{regio_id}", response_model=list[schemas.Dier])
def read_dier_by_regio(regio_id: int, db: Session = Depends(get_db)):
    dieren = crud.get_dier_by_regio(db, regio_id=regio_id)
    return dieren


@app.delete("/dieren/{diersoort}")
def delete_dier(diersoort: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_eigenaar = auth.get_current_eigenaar(db, token)
    if not current_eigenaar:
        raise HTTPException(status_code=401, detail="Eigenaar not authenticated")
    dier = crud.get_dier(db, diersoort=diersoort)
    if not dier:
        raise HTTPException(status_code=404, detail="Animal not found")
    return crud.delete_dier(db=db, dier=dier)


@app.put("/dieren/{diersoort}")
def update_dier(diersoort: str, dier_update: schemas.DierCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_eigenaar = auth.get_current_eigenaar(db, token)
    if not current_eigenaar:
        raise HTTPException(status_code=401, detail="Eigenaar not authenticated")
    dier = crud.get_dier(db, diersoort=diersoort)
    if not dier:
        raise HTTPException(status_code=404, detail="Animal not found")
    updated_dier = crud.update_dier(db, dier, dier_update)
    return updated_dier


@app.post("/eigenaar/")
def create_eigenaar(eigenaar: schemas.EigenaarCreate, db: Session = Depends(get_db)):
    login = crud.get_eigenaar(db, email=eigenaar.email)
    if login:
        raise HTTPException(status_code=400, detail="Eigenaar already registred")
    return crud.create_eigenaar(db=db, eigenaar=eigenaar)


@app.delete("/eigenaar/{eigenaar_email}")
def delete_eigenaar(email: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_eigenaar = auth.get_current_eigenaar(db, token)
    if not current_eigenaar:
        raise HTTPException(status_code=404, detail="Admin not found")
    if current_eigenaar.email != email:
        raise HTTPException(status_code=404, detail="Admin not found")
    return crud.delete_eigenaar(db=db, eigenaar=current_eigenaar)
