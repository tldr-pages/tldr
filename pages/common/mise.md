# mise

> Manage versions of different packages.
> More information: <https://mise.jdx.dev>.

- List all available plugins:

`mise plugins list-all`

- Install a plugin:

`mise plugins add {{name}}`

- List runtime versions available for install:

`mise ls-remote {{name}}`

- Install a specific version of a package:

`mise install {{name}}@{{version}}`

- Set global version for a package:

`mise use --global {{name}}@{{version}}`

- Set local version for a package:

`mise use {{name}}@{{version}}`

- Set environment variable in configuration:

`mise set {{variable}}={{value}}`

- Pass an option

`mise install {{name}}\[{{option}}={{option_value}}\]@{{version}}`
`mise use {{name}}\[{{option}}={{option_value}}\]@{{version}}`

- Multiple options

`mise use {{name}}\[{{option1}}={{option1_value}},{{option2}}={{option2_value}}\]@{{version}}`
