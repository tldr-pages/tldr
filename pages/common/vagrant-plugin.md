# vagrant plugin

> Manage Vagrant plugins.
> See also: `vagrant`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/plugin>.

- List all the plugins currently installed:

`vagrant plugin list`

- Install a plugin from remote repositories, usually RubyGems:

`vagrant plugin install {{vagrant_vbguest}}`

- Install a plugin from a local file source:

`vagrant plugin install {{path/to/my_plugin.gem}}`

- Update all installed plugins to their latest version:

`vagrant plugin update`

- Update a plugin to the latest version:

`vagrant plugin update {{vagrant_vbguest}}`

- Uninstall a specific plugin:

`vagrant plugin uninstall {{vagrant_vbguest}}`
