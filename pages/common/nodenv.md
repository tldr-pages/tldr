# nodenv

> A tool to manage NodeJS versions.
> More information: <https://github.com/nodenv/nodenv>.

- Install a version of NodeJS:

`nodenv install {{version}}`

- Display a list of available versions:

`nodenv install --list`

- Use a specific version of NodeJS across the whole system:

`nodenv global {{version}}`

- Use a specific version of NodeJS with a directory:

`nodenv local {{version}}`

- Show the NodeJS version for the current directory:

`nodenv version`

- Show the location of a NodeJS-installed command, e.g. `npm`:

`nodenv which {{command}}`
