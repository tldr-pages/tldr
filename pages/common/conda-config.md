# conda config

> Modify configuration values in .condarc.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/config.html>.

- Show current configuration values. Shows all configuration values if no arguments given.:

`conda config {{--show}} {{<setting_name>}}`

- Set or remove a configuration value:

`conda config {{[--set|--remove]}} {{<key>}} {{<value>}}`

- Append or prepend a value to an existing configuration key:

`conda config {{[--append|--prepend]}} {{<key>}} {{<value>}}`

- Describe given configuration parameters. If no arguments given, show information for all configuration parameters.:

`conda config {{--describe}} {{<option>}}`

