# sfdk config

> Configures sfdk.

- Show configuration in all scopes:

`sfdk config --show`

- Set a configuration value:

`sfdk config {{name}}={{value}}`

- Mask an option as empty:

`sfdk config {{name}}=`

- Mask an option as empty without pushing it at the inner scope:

`sfdk config {{name}}`

- Clear option value:

`sfdk --drop {{name}}`

- Run subcommand in specified scope (`global`, `session` or `command`):

`sfdk config --{{scope}} {{subcommand}}`
