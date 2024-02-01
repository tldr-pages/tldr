# rvm

> A tool for easily installing, managing, and working with multiple ruby environments.
> More information: <https://rvm.io>.

- Install one or more versions of Ruby:

`rvm install {{version1 version2 ...}}`

- Display a list of installed versions:

`rvm list`

- Use a specific version of Ruby:

`rvm use {{version}}`

- Set the default Ruby version:

`rvm --default use {{version}}`

- Upgrade a version of Ruby to a new version:

`rvm upgrade {{current_version}} {{new_version}}`

- Uninstall a version of Ruby and keep its sources:

`rvm uninstall {{version}}`

- Remove a version of Ruby and its sources:

`rvm remove {{version}}`

- Show specific dependencies for your OS:

`rvm requirements`
