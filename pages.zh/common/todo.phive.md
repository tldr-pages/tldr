# phive

> The Phar Installation and Verification Environment for secure PHP application deployment.
> More information: <https://phar.io>.

- Display a list of available aliased Phars:

`phive list`

- Install a specified Phar to the local directory:

`phive install {{alias|url}}`

- Install a specified Phar globally:

`phive install {{alias|url}} --global`

- Install a specified Phar to a target directory:

`phive install {{alias|url}} --target {{path/to/directory}}`

- Update all Phar files to the latest version:

`phive update`

- Remove a specified Phar file:

`phive remove {{alias|url}}`

- Remove unused Phar files:

`phive purge`

- List all available commands:

`phive help`
