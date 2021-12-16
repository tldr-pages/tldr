# volta

> A JavaScript Tool Manager that installs Node.js runtimes, npm and Yarn package managers, or any binaries from npm.
> More information: <https://volta.sh>.

- List all installed tools:

`volta list`

- Install the latest version of a tool:

`volta install {{node|npm|yarn|package_name}}`

- Install a specific version of a tool:

`volta install {{node|npm|yarn}}@version`

- Choose a tool version for a project (will store it in `package.json`):

`volta pin {{node|npm|yarn}}@version`

- Display help:

`volta help`

- Display help for a subcommand:

`volta help {{fetch|install|uninstall|pin|list|completions|which|setup|run|help}}`
