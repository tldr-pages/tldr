# gunicorn

> Python WSGI HTTP Server for UNIX.

- Run Python web app:

`gunicorn {{import.path:app_object}}`

- Listen on port 8080 on localhost:

`gunicorn --bind {{localhost}}:{{8080}} {{import.path:app_object}}`

- Turn on live reload:

`gunicorn --reload {{import.path:app_object}}`

- Use 4 worker processes for handling requests:

`gunicorn --workers {{4}} {{import.path:app_object}}`

- Use 4 worker threads for handling requests:

`gunicorn --threads {{4}} {{import.path:app_object}}`
