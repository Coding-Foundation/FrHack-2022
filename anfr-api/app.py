import base64

from fastapi import FastAPI
from starlette.responses import FileResponse
from database import conn, cur

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/clusters")
async def getClusters():
    sql = "SELECT * FROM captor_cluster"

    return cur.execute(sql).fetchAll()
@app.get("/captors")
def getCaptors():
    sql = "SELECT * FROM captor"
    # Récupérer tous les capteurs, y ajouter aussi leurs profil type
    return cur.execute(sql)


@app.get("/captors/{id}")
def getCaptorsResults(id: int):
    sql = "SELECT * FROM captor_cluster WHERE " + id
    # Récupérer les informations du capteur ainsi que les résultats
    return cur.execute(sql)


@app.get("/antennas")
def getAntennas():
    sql = "SELECT * FROM antenna"
    return cur.execute(sql)


@app.get("/antennas/{id}")
def getAntennas(id: int):
    sql = "SELECT * FROM antenna WHERE " + id
    return cur.execute(sql)


@app.get("/results/{name}")
def getResults(name: str):
    decoded_string = base64.b64decode(name)
    image_name = decoded_string.decode("utf-8")
    return FileResponse("../prep/week_derive_plots/" + image_name + ".png")
