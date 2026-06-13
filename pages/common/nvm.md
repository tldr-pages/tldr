# nvm

> Install, uninstall, or switch between Node.js versions.
> Supports version numbers like "12.8" or "v16.13.1", and labels like "node", "system", etc.
> See also: `asdf`.
> More information: <https://github.com/nvm-sh/nvm#usage>.

- Install/uninstall a specific version of Node.js:

`nvm {{install|uninstall}} {{node_version}}`

- Use a specific version of Node.js in the current shell:

`nvm use {{node_version}}`

- Set the default Node.js version:

`nvm alias default {{node_version}}`

- List remote versions available for install, only show LTS (long-term support) versions:

`nvm ls-remote --lts`

- List installed versions:

`nvm {{[ls|list]}}`

- Launch the REPL of a specific version of Node.js:

`nvm run {{node_version}}`

- Execute a script in a specific version of Node.js:

`nvm exec {{node_version}} node {{path/to/script.js}}`

- Upgrade to the latest working npm version on the current Node.js version:

`nvm install-latest-npm`
