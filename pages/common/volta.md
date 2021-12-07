# volta

> A JavaScript Tool Manager that installs Node.js runtimes, Npm and Yarn package managers, or any binaries from Npm.
> More information: <https://volta.sh>.

- List all installed tools:

`volta list`

- Install the latest version of a tool:

`volta install {{node|npm|yarn}}`

- Install a specific version of a tool:

`volta install {{node|npm|yarn}}@version`

- Choose a tool version for a project (will store it in `package.json`):

`volta pin {{node|npm|yarn}}@version`

- Print help listings all sub-commands and all flags:

`volta help`

- Print detailed help for a single sub-command:

`volta help {{fetch|install|uninstall|pin|list|completions|which|setup|run|help}}`
