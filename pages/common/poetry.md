# poetry

> Manage Python packages and dependencies.
> More information: <https://python-poetry.org/docs>.

- Create a new Poetry project in the directory {{project-name}}:

`poetry new {{project-name}}`

- Install {{dependency}} and its subdependencies:

`poetry add {{dependency}}`

- Interactively initialize the current directory as a new Poetry project:

`poetry init`

- Get the latest version of all dependencies and update poetry.lock:

`poetry update`

- Execute {{command}} inside the project's virtualenv:

`poetry run {{command}}`
