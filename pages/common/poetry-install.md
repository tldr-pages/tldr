# poetry install

> Install all dependencies for a Python project as defined in the pyproject.toml file.
> More information: <https://python-poetry.org/docs/cli/#install>.

- Install dependencies:

`poetry install`

- Skip installing the project itself as a dependency:

`poetry install --no-root`

- Install only production dependencies:

`poetry install --without dev`

- Install optional dependenciy groups:

`poetry install --with test,docs`
