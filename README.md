# NwtScreen (backend)
Frontend: [https://github.com/Unviray/nwtscreen-frontend](https://github.com/Unviray/nwtscreen-frontend)
## Installing

### Using poetry (recommended)
```shell
$ git clone https://github.com/Unviray/nwtscreen-backend
$ cd nwtscreen-backend/
$ poetry install
```

### Using pip
```shell
$ git clone https://github.com/Unviray/nwtscreen-backend
$ cd nwtscreen-backend/
$ pip install -r requirements.txt
```

## Run

### Using poetry (recommended)
```shell
$ poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000
```

### If you used pip
```shell
$ uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## Documentation

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
