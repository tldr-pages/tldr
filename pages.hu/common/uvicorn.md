# uvicorn

> Python ASGI HTTP Server, aszinkron projektekhez. További információ: <https://www.uvicorn.org/>.

- Python webes alkalmazás futtatása:

`uvicorn {{import.path:app_object}}`

- Figyeljen a 8080-as porton a localhost-on:

`uvicorn --host {{localhost}} --port {{8080}} {{import.path:app_object}}`

- Kapcsolja be az élő újratöltést:

`uvicorn --reload {{import.path:app_object}}`

- Használjon 4 munkafolyamatot a kérések kezelésére:

`uvicorn --workers {{4}} {{import.path:app_object}}`

- Az alkalmazás futtatása HTTPS-en keresztül:

`uvicorn --ssl-certfile {{cert.pem}} --ssl-keyfile {{key.pem}} {{import.path:app_object}}`
