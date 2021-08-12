# gunicorn

> Server HTTP Python WSGI.
> Mai multe informaţii: <https://gunicorn.org/>

- Rulați aplicația web Python:

`gunicorn {{import.path:app_object}}`

- Ascultă pe portul 8080 pe localhost:

`gunicorn --bind {{localhost}}:{{8080}} {{import.path:app_object}}`

- Porniți reîncărcați în direct:

`gunicorn --reload {{import.path:app_object}}`

- Utilizați 4 procese de lucrători pentru gestionarea cererilor:

`gunicorn --workers {{4}} {{import.path:app_object}}`

- Utilizați 4 fire de lucru pentru manipularea solicitărilor:

`gunicorn --threads {{4}} {{import.path:app_object}}`

- Rulați aplicația peste HTTPS:

`gunicorn --certfile {{cert.pem}} --keyfile {{key.pem}} {{import.path:app_object}}`
