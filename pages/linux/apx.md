# apx

> A wrapper around multiple package managers for Vanilla OS.
> Some subcommands such as `init` have their own usage documentation.
> More information: <https://github.com/Vanilla-OS/apx>.

- Initialize the unmanaged container:

`apx init`

- Install a package inside the container:

`apx install {{package_name}}`

- Search for a package inside the container:

`apx search {{package_name}}`

- Remove a package from the container:

`apx remove {{package_name}}`

- Update the list of available packages in the container:

`apx update`

- Upgrade all installed packages in the container:

`apx upgrade`

- Execute a command inside the container:

`apx run {{command}}`
