from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from database import conn, checkIfConnectionIsAlive
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
global connection


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/clusters")
async def getClusters():
    global connection
    try:
        connection = checkIfConnectionIsAlive(connection)
        cur = connection.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM captor_cluster"
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        return results
    except Exception:
        print("Erreur")


@app.get("/captors")
def getCaptors():
    try:
        global connection
        connection = checkIfConnectionIsAlive(connection)
        cur = connection.cursor(cursor_factory=RealDictCursor)
        sql = "SELECT * FROM captor FULL JOIN captor_cluster ON captor.name = captor_cluster.numero"
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result
    except Exception:
        print("Erreur")


@app.get("/captors/{id}")
def getCaptorsResults(id: int):
    try:
        global connection
        connection = checkIfConnectionIsAlive(connection)
        cur = connection.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM captor_cluster WHERE " + id
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        return result
    except Exception:
        print("Erreur")


@app.get("/antennas")
def getAntennas():
    global connection
    connection = checkIfConnectionIsAlive(connection)
    cur = connection.cursor(cursor_factory=RealDictCursor)

    sql = "SELECT * FROM antenna"
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return results


@app.get("/antennas/{id}")
def getAntennas(id: int):
    try:
        global connection
        connection = checkIfConnectionIsAlive(connection)
        cur = connection.cursor(cursor_factory=RealDictCursor)
        sql = "SELECT * FROM antenna WHERE id = " + str(id)
        cur.execute(sql)
        results = cur.fetchone()
        cur.close()
        return results
    except Exception:
        print("Erreur")


@app.get("/results/{name}")
def getResults(name: str):
    return FileResponse("../prep/week_derive_plots/" + name + ".png")


@app.get("/results-cluster/{id}")
def getResults(id: str):
    return FileResponse("../prep/plots/cluster/" + id + ".png")

@app.get("/raw-results/{name}")
def getResults(name: str):
    return FileResponse("../prep/plots/week_absolute/" + name + ".png")
