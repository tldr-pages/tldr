# poetry install

> Install the dependencies of the current Poetry project.
> More information: <https://python-poetry.org/docs/cli/#install>.

- Install all default dependency groups:

`poetry install`

- Include additional dependency groups (comma-separated):

`poetry install --with {{dev,docs}}`

- Exclude dependency groups:

`poetry install --without {{dev}}`

- Only install a specific dependency group:

`poetry install --only {{main}}`

- Sync the environment to match the lockfile exactly (remove extras):

`poetry install --sync`

- Install dependencies but skip installing the current project as a package:

`poetry install --no-root`
