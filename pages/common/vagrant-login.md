# vagrant login

> Authenticate with HashiCorp's Vagrant Cloud server.
> Logging in is only necessary if you are accessing protected boxes or using Vagrant Share.
> See also: `vagrant`, `vagrant cloud`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/login>.

- Log in to Vagrant Cloud interactively with a username and password:

`vagrant login`

- Check if you are currently logged in:

`vagrant login --check`

- Log in using a Vagrant Cloud access token:

`vagrant login --token {{your_access_token}}`

- Log out of Vagrant Cloud:

`vagrant login --logout`
