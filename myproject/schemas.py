from pydantic import BaseModel


class ManagerBase(BaseModel):
    voornaam: str
    achternaam: str
    manager_nummer: str


class ManagerCreate(ManagerBase):
    pass


class Manager(ManagerBase):
    id: int

    class Config:
        orm_mode = True


class RegioBase(BaseModel):
    regionaam: str
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
