# gem

> Interact with the package manager for the Ruby programming language.
> More information: <https://rubygems.org>.

- Display remote gems:

`gem search {{regexp}}`

- Display remote gem(s) and show all available versions:

`gem search {{regexp}} --all`

- Install latest version of a gem:

`gem install {{gemname}}`

- Install specific version of a gem:

`gem install {{gemname}} --version {{1.0.0}}`

- Update a gem:

`gem update {{gemname}}`

- List all local gems:

`gem list`

- Uninstall a gem:

`gem uninstall {{gemname}}`

- Uninstall specific version of a gem:

`gem uninstall {{gemname}} --version {{1.0.0}}`
