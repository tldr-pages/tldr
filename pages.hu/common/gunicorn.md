# gunicorn

> Python WSGI HTTP-kiszolgáló. További információ: <https://gunicorn.org/>.

- Python webes alkalmazás futtatása:

`gunicorn {{import.path:app_object}}`

- Figyeljen a 8080-as porton a localhost-on:

`gunicorn --bind {{localhost}}:{{8080}} {{import.path:app_object}}`

- Kapcsolja be az élő újratöltést:

`gunicorn --reload {{import.path:app_object}}`

- Használjon 4 munkafolyamatot a kérések kezelésére:

`gunicorn --workers {{4}} {{import.path:app_object}}`

- Használjon 4 munkaszálat a kérelmek kezeléséhez:

`gunicorn --threads {{4}} {{import.path:app_object}}`

- Az alkalmazás futtatása HTTPS-en keresztül:

`gunicorn --certfile {{cert.pem}} --keyfile {{key.pem}} {{import.path:app_object}}`
