# conda config

> Modify configuration values in `.condarc`.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/config.html>.

- Show all configuration values:

`conda config --show`

- Show current value of a configuration option:

`conda config --show {{config_option}}`

- Set a configuration value:

`conda config --set {{key}} {{value}}`

- Remove a configuration value:

`conda config --remove {{key}} {{value}}`

- Append a value to an existing configuration key list:

`conda config --append {{key}} {{value}}`

- Prepend a value to an existing configuration key list:

`conda config --prepend {{key}} {{value}}`

- Describe given configuration option:

`conda config --describe {{config_option}}`
