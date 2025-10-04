# pip config

> Manage local and global configuration for pip.
> More information: <https://pip.pypa.io/en/stable/cli/pip_config/>.

- List all configuration values:

`pip config list`

- Show configuration files and their values:

`pip config debug`

- Set the value for a command option:

`pip {{--global|--user|--site}} config set {{command.option}} {{value}}`

- Get the value for a command option:

`pip {{--global|--user|--site}} config get {{command.option}}`

- Unset the value for a command option:

`pip {{--global|--user|--site}} config unset {{command.option}}`

- Edit the configuration file with the default editor:

`pip {{--global|--user|--site}} config edit`

- Edit the configuration file with a specific editor:

`pip {{--global|--user|--site}} --editor {{path/to/editor/binary}} config edit`
