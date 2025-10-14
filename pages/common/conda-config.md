# conda config

> Modify configuration values in .condarc.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/config.html>.

- Show current configuration values. Shows all configuration values if no arguments given:

`conda config --show {{setting_name}}`

- Set a configuration value:

`conda config --set {{key}} {{value}}`

- Remove a configuration value:

`conda config --remove {{key}} {{value}}`

- Append a value to an existing configuration key list:

`conda config --append {{key}} {{value}}`

- Prepend a value to an existing configuration key list:

`conda config --prepend {{key}} {{value}}`

- Describe given configuration parameters. If no arguments given, show information for all configuration parameters:

`conda config {{--describe}} {{configuration_option}}`
