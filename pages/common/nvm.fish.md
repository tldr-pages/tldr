# nvm

> Install, uninstall, or switch between Node.js versions under the `fish` shell.
> Supports version numbers like "12.8" or "v16.13.1", and labels like "stable", "system", etc.
> More information: <https://github.com/jorgebucaran/nvm.fish>.

- Install a specific version of Node.js:

`nvm install {{node_version}}`

- Use a specific version of Node.js in the current shell:

`nvm use {{node_version}}`

- Set the default Node.js version:

`set nvm_default_version {{node_version}}`

- List all available Node.js versions and highlight the default one:

`nvm list`

- Uninstall a given Node.js version:

`nvm uninstall {{node_version}}`
