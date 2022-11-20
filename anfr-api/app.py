from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from database import conn, checkIfConnectionIsAlive



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
global connection

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/clusters")
async def getClusters():
    global connection
    connection = checkIfConnectionIsAlive(connection)
    cur = connection.cursor(cursor_factory=RealDictCursor)

    sql = "SELECT * FROM captor_cluster"
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    return results
@app.get("/captors")
def getCaptors():
    global connection
    connection = checkIfConnectionIsAlive(connection)
    cur = connection.cursor(cursor_factory=RealDictCursor)

    sql = "SELECT * FROM captor FULL JOIN captor_cluster ON captor.name = captor_cluster.numero"
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    return result


@app.get("/captors/{id}")
def getCaptorsResults(id: int):
    global connection
    connection = checkIfConnectionIsAlive(connection)
    cur = connection.cursor(cursor_factory=RealDictCursor)

    sql = "SELECT * FROM captor_cluster WHERE " + id
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    return result


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
    global connection
    connection = checkIfConnectionIsAlive(connection)
    cur = connection.cursor(cursor_factory=RealDictCursor)

    sql = "SELECT * FROM antenna WHERE " + id
    cur.execute(sql)
    results = cur.fetchone()
    cur.close()
    return results


@app.get("/results/{name}")
def getResults(name: str):
    return FileResponse("../prep/week_derive_plots/" + name + ".png")


@app.get("/results-cluster/{id}")
def getResults(id: str):
    return FileResponse("../prep/plots/cluster/" + id + ".png")

@app.get("/raw-results/{name}")
def getResults(name: str):
    return FileResponse("../prep/plots/week_absolute/" + name + ".png")