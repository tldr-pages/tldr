# gem

> A package manager for the Ruby programming language.
> More information: <https://guides.rubygems.org/command-reference/>.

- Search for remote gem(s) and show all available versions:

`gem search {{regex}} {{[-a|--all]}}`

- Install the latest version of a gem:

`gem install {{gem_name}}`

- Install a specific version of a gem:

`gem install {{gem_name}} {{[-v|--version]}} {{1.0.0}}`

- Install the latest matching (SemVer) version of a gem:

`gem install {{gem_name}} {{[-v|--version]}} '~> {{1.0}}'`

- Update a gem:

`gem update {{gem_name}}`

- List all local gems:

`gem list`

- Uninstall a gem:

`gem uninstall {{gem_name}}`

- Uninstall a specific version of a gem:

`gem uninstall {{gem_name}} {{[-v|--version]}} {{1.0.0}}`
