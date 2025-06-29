# fastapi

> CLI tool to run FastAPI apps which uses Uvicorn under the hood.
> More information: <https://fastapi.tiangolo.com/tutorial/>.

- Run a FastAPI app with automatic reload (for development):

`fastapi run {{main.py}} --reload`

- Serve your app in both development or production mode using the `dev` command:

`fastapi dev {{main.py}}`

- Specify the host and port to run on:

`fastapi run {{main.py}} --host {{0.0.0.0}} --port {{8000}}`

- Set the app variable name (if not `app`) or specify a custom app directory:

`fastapi run {{main.py}} --app-dir {{path/to/app}} --app {{custom_app_name}}`

- Display global help:

`fastapi --help`

- Display help for a subcommand:

`fastapi run --help`
