from pydantic import BaseModel


class ManagerBase(BaseModel):
    voornaam: str
    achternaam: str
    manager_nummer: str
    foto: str | None = "new_manager.jpg"


class ManagerCreate(ManagerBase):
    pass


class Manager(ManagerBase):
    id: int

    class Config:
        orm_mode = True


class RegioBase(BaseModel):
    regionaam: str
    foto: str | None = "new_regio.jpg"
    manager_id: int


class RegioCreate(RegioBase):
    pass


class Regio(RegioBase):
    id: int

    class Config:
        orm_mode = True


class DierBase(BaseModel):
    diersoort: str
    hoeveelheid: int
    foto: str | None = "new_dier.jpg"
    regio_id: int


class DierCreate(DierBase):
    pass


class Dier(DierBase):
    id: int

    class Config:
        orm_mode = True


class EigenaarBase(BaseModel):
    voornaam: str
    achternaam: str
    email: str


class EigenaarCreate(EigenaarBase):
    password: str


class Eigenaar(EigenaarBase):
    id: int

    class Config:
        orm_mode = True
