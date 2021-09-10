from pathlib import Path
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BOOK_LIST = Path() / "book/"


@app.get("/")
def get_book_list():

    result = []
    orders = dict()
    for book in BOOK_LIST.iterdir():
        with open(book, "r") as fp:
            loaded = json.load(fp)

            name = loaded["meta"]["name"]
            order = loaded["meta"]["order"]

            result.append(name)
            orders[name] = order

    result.sort(key=lambda key: orders[key])

    return result


@app.get("/verset/{name}")
def book(name:str):
    book = BOOK_LIST / f"{name}.json"
    with open(book, "r") as fp:
        loaded = json.load(fp)

    return loaded

@app.get("/verset/{name}/{chapter}")
def chap(name:str, chapter:int):
    return book(name)[str(chapter)]

@app.get("/verset/{name}/{chapter}/{verset}")
def vers(name:str, chapter:int, verset:int):
    return chap(name, chapter)[str(verset)]


@app.get("/meta/{book_name}")
def meta(book_name: str):
    book = BOOK_LIST / f"{book_name}.json"
    with open(book, "r") as fp:
        loaded = json.load(fp)

        return loaded["meta"]


@app.get("/testament/{n}")
def get_book_list_with_testament(n: int):
    book_list = get_book_list()

    first = book_list[:39]
    last = book_list[39:]

    return first if n == 1 else last


class PointerModel(BaseModel):
    book: str
    chapter: int
    verset: int


to_show_screen = None

@app.post("/screen")
def set_verset_list(model:PointerModel):
    global to_show_screen
    to_show_screen = model
    return to_show_screen

@app.get("/screen")
def get_verset_list():
    global to_show_screen
    return to_show_screen

@app.post("/clear-screen")
def clear_show_screen():
    global to_show_screen
    to_show_screen = None
    return to_show_screen
