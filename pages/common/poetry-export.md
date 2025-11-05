# poetry export

> Export Poetry's lock file to other formats.
> Provided by the Export Poetry Plugin.
> More information: <https://github.com/python-poetry/poetry-plugin-export#usage>.

- Export dependencies to a `requirements.txt` file:

`poetry export {{[-o|--output]}} {{requirements.txt}}`

- Export dependencies including development dependencies:

`poetry export {{[-o|--output]}} {{requirements-dev.txt}} --dev`

- Export dependencies without hashes:

`poetry export {{[-o|--output]}} {{requirements.txt}} --without-hashes`

- Export dependencies for a specific format:

`poetry export {{[-f|--format]}} {{requirements.txt}} {{[-o|--output]}} {{requirements.txt}}`

- Export only specific dependency groups:

`poetry export --only {{main}} {{[-o|--output]}} {{requirements.txt}}`

- Display help:

`poetry export {{[-h|--help]}}`
