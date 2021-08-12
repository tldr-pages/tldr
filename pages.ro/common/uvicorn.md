# uvicorn

> Python ASGI HTTP Server, pentru proiecte asincrone.
> Mai multe informaţii: <https://www.uvicorn.org/>

- Rulați aplicația web Python:

`uvicorn {{import.path:app_object}}`

- Ascultă pe portul 8080 pe localhost:

`uvicorn --host {{localhost}} --port {{8080}} {{import.path:app_object}}`

- Porniți reîncărcați în direct:

`uvicorn --reload {{import.path:app_object}}`

- Utilizați 4 procese de lucrători pentru gestionarea cererilor:

`uvicorn --workers {{4}} {{import.path:app_object}}`

- Rulați aplicația peste HTTPS:

`uvicorn --ssl-certfile {{cert.pem}} --ssl-keyfile {{key.pem}} {{import.path:app_object}}`
