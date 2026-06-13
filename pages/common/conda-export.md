# conda export

> Export environment details.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/export.html>.

- Export the current environment details to `stdout`:

`conda export`

- Export the current environment details to a `YAML` file:

`conda export {{[-f|--file]}} {{path/to/environment.yaml}}`

- Export details in a specific format:

`conda export --format {{environment-json|environment-yaml|explicit|json|reqs|requirements|txt|yaml|yml}}`

- Target an environment by name:

`conda export {{[-n|--name]}} {{environment_name}}`

- Target an environment by its path:

`conda export {{[-p|--prefix]}} {{path/to/environment}}`

- Include a specific channel:

`conda export {{[-c|--channel]}} {{channel_name}}`
