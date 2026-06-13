# fastapi

> Run FastAPI apps which uses Uvicorn under the hood.
> More information: <https://manned.org/fastapi>.

- Run a FastAPI app with automatic reload (for development):

`fastapi run {{path/to/file.py}} --reload`

- Serve your app in both development mode:

`fastapi dev {{path/to/file.py}}`

- Specify the host and port to run on:

`fastapi run {{path/to/file.py}} --host {{host_address}} --port {{port}}`

- Set the app variable name (if not `app`) or specify a custom app directory:

`fastapi run {{path/to/file.py}} --app-dir {{path/to/app}} --app {{custom_app_name}}`

- Display help:

`fastapi --help`

- Display help for a subcommand:

`fastapi {{subcommand}} --help`
