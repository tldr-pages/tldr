# pip config

> Manage local and global configuration for pip.
> More information: <https://pip.pypa.io/en/stable/cli/pip_config/>.

- List all configuration values:

`pip config list`

- Show configuration files and their values:

`pip config debug`

- Set the value for a command option:

`pip config set {{command.option}} {{value}} {{--global|--user|--site}}`

- Get the value for a command option:

`pip config get {{command.option}} {{--global|--user|--site}}`

- Unset the value for a command option:

`pip config unset {{command.option}} {{--global|--user|--site}}`

- Edit the configuration file with the default editor:

`pip config edit {{--global|--user|--site}}`

- Edit the configuration file with a specific editor:

`pip config edit {{--global|--user|--site}} --editor {{path/to/editor_binary}}`
