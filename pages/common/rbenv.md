# rbenv

> A tool to easily install Ruby versions and manage application environments.
> See also: `asdf`.
> More information: <https://github.com/rbenv/rbenv>.

- Install a Ruby version:

`rbenv install {{version}}`

- Display a list of the latest stable versions for each Ruby:

`rbenv install --list`

- Display a list of installed Ruby versions:

`rbenv versions`

- Use a specific Ruby version across the whole system:

`rbenv global {{version}}`

- Use a specific Ruby version for an application/project directory:

`rbenv local {{version}}`

- Display the currently selected Ruby version:

`rbenv version`

- Uninstall a Ruby version:

`rbenv uninstall {{version}}`

- Display all Ruby versions that contain the specified executable:

`rbenv whence {{executable}}`
