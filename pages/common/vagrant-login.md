# vagrant login

> Authenticate with HashiCorp's Vagrant Cloud service.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/login>.

- Log in interactively using a username and password:
`vagrant login`

- Check whether you are already logged in:
`vagrant login --check`

- Authenticate using an existing Vagrant Cloud access token:
`vagrant login --token {{token}}`

- Log out of Vagrant Cloud:
`vagrant login --logout`
