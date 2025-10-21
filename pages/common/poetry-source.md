# poetry source

> Add source configurations to your Poetry project.
> See also: `asdf`.
> More information: <https://python-poetry.org/docs/cli/#source>.

- Add a source configuration:

`poetry source add {{source_name}} {{source_url}}`

- Set the priority of a source:

`poetry source add --priority {{primary|supplemental|explicit}} {{source_name}} {{source_url}}`

- Display info for all sources:

`poetry source show`

- Display info for a specific source:

`poetry source show {{source_name}}`

- Remove a source from your `pyproject.toml` file:

`poetry source remove {{source_name}}`
