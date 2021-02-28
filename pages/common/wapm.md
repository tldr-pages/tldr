# wapm

> The WebAssembly package manager.
> More information: <https://wapm.io/help/reference>.

- Interactively create a new `wapm.toml` file:

`wapm init`

- Download all the packages listed as dependencies in `wapm.toml`:

`wapm install`

- Download a specific version of a package and add it to the list of dependencies in wapm.toml:

`wapm install {{package_name}}@{{version}}`

- Download a package and install it globally:

`wapm install --global {{package_name}}`

- Uninstall a package and remove it from the list of dependencies in `wapm.toml`:

`wapm uninstall {{package_name}}`

- Print a tree of locally-installed dependencies:

`wapm list`

- List top-level globally installed packages:

`wapm list --global`

- Execute a package command using the Wasmer runtime:

`wapm run {{command_name}} {{arguments}}`
