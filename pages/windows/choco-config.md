# choco config

> Manage configuration file settings for Chocolatey.
> More information: <https://docs.chocolatey.org/en-us/choco/commands/config/>.

- Display all configuration settings and their values:

`choco config list`

- Display the value of a specific configuration setting:

`choco config get {{setting_name}}`

- Set a value for a specific configuration setting:

`choco config set {{setting_name}} {{value}}`

- Unset a specific configuration setting:

`choco config unset {{setting_name}}`
