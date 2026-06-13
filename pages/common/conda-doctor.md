# conda doctor

> Display a health report for your environment.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/doctor.html>.

- View report for the currently active environment:

`conda doctor`

- Specify an environment by name:

`conda doctor {{[-n|--name]}} {{environment_name}}`

- Specify an environment by its path:

`conda doctor {{[-p|--prefix]}} {{path/to/environment}}`

- Enable verbose output (Note: the `-v` flag can be repeated to increase verbosity):

`conda doctor {{[-v|--verbose]}}`
