# հրացան

> Python WSGI HTTP սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://docs.gunicorn.org/en/latest/run.html>:.

- Գործարկել Python վեբ հավելվածը.:

`gunicorn {{import.path:app_object}}`

- Լսեք 8080 նավահանգստում localhost-ում.:

`gunicorn {{[-b|--bind]}} {{localhost}}:{{8080}} {{import.path:app_object}}`

- Միացնել կենդանի վերաբեռնումը.:

`gunicorn --reload {{import.path:app_object}}`

- Օգտագործեք 4 աշխատանքային գործընթաց՝ հարցումները մշակելու համար.:

`gunicorn {{[-w|--workers]}} {{4}} {{import.path:app_object}}`

- Օգտագործեք 4 աշխատանքային թելեր՝ հարցումները մշակելու համար.:

`gunicorn --threads {{4}} {{import.path:app_object}}`

- Գործարկեք հավելվածը HTTPS-ով.:

`gunicorn --certfile {{cert.pem}} --keyfile {{key.pem}} {{import.path:app_object}}`
