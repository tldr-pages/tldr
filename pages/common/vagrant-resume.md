# vagrant resume

> Resume a Vagrant managed machine that was previously suspended.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/resume>.

- Resume machine specified by name or id:

`vagrant resume {{name|id}}`

- Resume and run all configured provisioners:

`vagrant resume {{name|id}} --provision`

- Resume and specify which provisioners to re-run:

`vagrant resume {{name|id}} --provision-with {{provisioner}}`
