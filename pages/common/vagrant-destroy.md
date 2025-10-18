# vagrant destroy

> Stop a guest machine and destroy all its resources.
> Any boxes installed are kept intact.
> See also: `vagrant`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/destroy>.

- Destroy the currently running machine:

`vagrant destroy`

- Target a machine by name or id:

`vagrant destroy {{name|id}}`

- Do not ask for confirmation before destroying:

`vagrant destroy {{[-f|--force]}}`

- Shut down the machine gracefully:

`vagrant destroy {{[-g|--graceful]}}`
