from fastapi import FastAPI
import requests

app = FastAPI()

@app.on_event("startup")
def startup():
    print("Bonjour")


@app.on_event("shutdown")
def shutdown():
    print("Arrive Derchi")


@app.get("/{Nombre}")
async def root(Nombre: str):
    lista = []
    response = requests.get('https://api.publicapis.org/entries')
    response = response.json()
    items = response['entries']
    item_list = list(items)
    for item in item_list:
        posicion = item["API"].find(Nombre)
        if posicion != -1:
            lista.append(item)
    return lista

@app.get("/")
async def root():
    response = requests.get('https://api.publicapis.org/entries')
    response = response.json()
    items = response['entries']
    item_list = list(items)
    return item_list