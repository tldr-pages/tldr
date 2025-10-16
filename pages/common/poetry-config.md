# poetry config

> Edit poetry config settings and repositories.
> More information: <https://python-poetry.org/docs/cli/#config>.

- List current configuration:

`poetry config --list`

- Remove the a previously set setting named by `setting-key`:

`poetry config {config_key}} --unset`

- See the value of a specific setting:

`poetry config {config_key}}`

- Change or add a new configuration setting by passing a value after the setting’s name:

`poetry config {config_key}} {{config_value}}`

- Migrate outdated configuration settings:

`poetry config --migrate`

- Set/Get settings that are specific to a project:

`poetry config --local`
