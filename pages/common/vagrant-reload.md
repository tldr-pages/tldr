# vagrant reload

> Equivalent of running `halt` followed by `up`.
> A reload is usually required for changes in a Vagrantfile to take effect.
> See also: `vagrant`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/reload>.

- Reload the currently running machine:

`vagrant reload`

- Target a machine by name or id:

`vagrant reload {{name|id}}`

- Force the provisioners to run:

`vagrant reload --provision`
