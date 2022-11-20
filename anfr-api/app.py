import base64
from typing import Union
from fastapi import FastAPI
from starlette.responses import FileResponse

from database import SessionLocal
from import_service import ImportService
from models import *

app = FastAPI()

database = SessionLocal()

importService = ImportService(database)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/captors")
def getCaptors():
    # Récupérer tous les capteurs, y ajouter aussi leurs profil type
    return database.query(Captor).all()


@app.get("/captors/{id}")
def getCaptorsResults(id: int):
    # Récupérer les informations du capteur ainsi que les résultats
    return database.query(Captor).get(id)


@app.get("/antennas")
def getAntennas():
    # Récupérer toutes les antennes
    return database.query(Antenna).all()


@app.get("/antennas/{id}")
def getAntennas(id: int):
    # Récupérer toutes les antennes
    return database.query(Antenna).get(id)


@app.get("/results/{name}")
def getResults(name: str):
    decoded_string = base64.b64decode(name)
    image_name = decoded_string.decode("utf-8")
    return FileResponse("../prep/week_derive_plots/" + image_name + ".png")
