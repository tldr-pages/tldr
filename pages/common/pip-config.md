# pip config

> Manage local and global configuration for pip.
> More information: <https://pip.pypa.io/en/stable/cli/pip_config/>.

- List all configuration values:

`pip config list`

- Show configuration files and their values:

`pip config debug`

- Set the value for a command option:

`pip config {{--global|--user|--site}} set {{command.option}} {{value}}`

- Get the value for a command option:

`pip config {{--global|--user|--site}} get {{command.option}}`

- Unset the value for a command option:

`pip config {{--global|--user|--site}} unset {{command.option}}`

- Edit the configuration file with the default editor:

`pip config {{--global|--user|--site}} edit`

- Edit the configuration file with a specific editor:

`pip config {{--global|--user|--site}} --editor {{path/to/editor/binary}} edit`
