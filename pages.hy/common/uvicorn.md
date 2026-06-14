# Uvichorn

> Python ASGI HTTP սերվեր, ասինխրոն նախագծերի համար:.
> Լրացուցիչ տեղեկություններ. <https://www.uvicorn.org/settings/>:.

- Գործարկել Python վեբ հավելվածը.:

`uvicorn {{import.path:app_object}}`

- Լսեք 8080 նավահանգստում localhost-ում.:

`uvicorn --host {{localhost}} --port {{8080}} {{import.path:app_object}}`

- Միացնել կենդանի վերաբեռնումը.:

`uvicorn --reload {{import.path:app_object}}`

- Օգտագործեք 4 աշխատանքային գործընթաց՝ հարցումները մշակելու համար.:

`uvicorn --workers {{4}} {{import.path:app_object}}`

- Գործարկեք հավելվածը HTTPS-ով.:

`uvicorn --ssl-certfile {{cert.pem}} --ssl-keyfile {{key.pem}} {{import.path:app_object}}`
