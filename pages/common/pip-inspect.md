# pip inspect

> Inspect the Python environment and produce a report in JSON format.
> More information: <https://pip.pypa.io/en/stable/cli/pip_inspect/>.

- Inspect the current environment:

`pip inspect`

- Inspect and save output to a file:

`pip inspect > {{environment_report.json}}`

- Inspect only locally installed packages (not global):

`pip inspect --local`

- Inspect only user-installed packages:

`pip inspect --user`

- Inspect packages in a specific path:

`pip inspect --path {{path/to/environment}}`

- Inspect with verbose output (Note: the `-v` flag can be repeated to increase verbosity):

`pip inspect {{[-v|--verbose]}}`
