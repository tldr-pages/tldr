# poetry export

> Export Poetry's lock file to other formats.
> More information: <https://python-poetry.org/docs/cli/#export>.

- Export dependencies to a requirements.txt file:

`poetry export --output {{requirements.txt}}`

- Export dependencies including development dependencies:

`poetry export --dev --output {{requirements-dev.txt}}`

- Export dependencies without hashes:

`poetry export --without-hashes --output {{requirements.txt}}`

- Export dependencies for a specific format:

`poetry export --format {{requirements.txt}} --output {{requirements.txt}}`

- Export only specific dependency groups:

`poetry export --only {{main}} --output {{requirements.txt}}`

- Display help:

`poetry export --help`
