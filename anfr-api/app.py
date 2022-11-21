from fastapi import FastAPI, Request
from psycopg2.extras import RealDictCursor
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from fastapi.openapi.utils import get_openapi
import psycopg2
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.middleware("http")
def initConnection(request: Request, call_next):
    HOST = os.environ.get("POSTGRES_HOST") or "marcpartensky.com"
    PORT = os.environ.get("POSTGRES_PORT") or "5433"
    DATABASE = os.environ.get("POSTGRES_DB") or "db"
    USER = os.environ.get("POSTGRES_USER") or "user"
    PASSWORD = os.environ.get("POSTGRES_PASSWORD") or "password"
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))
    request.state.connection = conn
    response = call_next(request)
    return response


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/clusters")
async def getClusters(request: Request):
    try:
        conn = request.state.connection
        cur = conn.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM captor_cluster"
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception:
        print("Erreur")
        return


@app.get("/captors")
def getCaptors(request: Request):
    try:
        conn = request.state.connection
        cur = conn.cursor(cursor_factory=RealDictCursor)
        sql = "SELECT * FROM captor FULL JOIN captor_cluster ON captor.name = captor_cluster.numero"
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception:
        print("Erreur")
        return


@app.get("/captors/{id}")
def getCaptorsResults(request: Request, id: int):
    try:
        conn = request.state.connection
        cur = conn.cursor(cursor_factory=RealDictCursor)
        sql = "SELECT * FROM captor_cluster WHERE " + id
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        conn.close()

        return result
    except Exception:
        print("Erreur")
        return


@app.get("/antennas")
def getAntennas(request: Request):
    conn = request.state.connection
    cur = conn.cursor(cursor_factory=RealDictCursor)
    sql = "SELECT * FROM antenna"
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return results


@app.get("/antennas/{id}")
def getAntenna(request: Request, id: int):
    try:
        conn = request.state.connection
        cur = conn.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM antenna WHERE id = " + str(id)
        cur.execute(sql)
        results = cur.fetchone()
        cur.close()
        conn.close()

        return results
    except Exception:
        print("Erreur")


@app.get("/transmitters/{id_antenna}")
async def getTransmitter(request: Request, id_antenna: int):
    try:
        conn = request.state.connection
        cur = conn.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM transmitter FULL JOIN system_telecom ON transmitter.system = system_telecom.id WHERE CAST(transmitter.antenna AS INT) = " + id_antenna
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception:
        print("Erreur")
        return

@app.get("/results/{name}")
def getResults(request: Request, name: str):
    request.state.connection.close()
    return FileResponse("../prep/week_derive_plots/" + name + ".png")


@app.get("/results-cluster/{id}")
def getResults(request: Request, id: str):
    request.state.connection.close()
    return FileResponse("../prep/plots/cluster/" + id + ".png")

@app.get("/raw-results/{name}")
def getResults(request: Request, name: str):
    request.state.connection.close()
    return FileResponse("../prep/plots/week_absolute/" + name + ".png")
