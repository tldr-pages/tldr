# vagrant box

> Manage Vagrant boxes (virtual machine images).
> See also: `vagrant`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/box>.

- List all installed boxes:

`vagrant box list`

- Add a new box:

`vagrant box add {{hashicorp/bionic64}}`

- Add a box from a custom URL:

`vagrant box add {{my-box}} {{https://example.com/my-box.box}}`

- Remove an installed box:

`vagrant box remove {{hashicorp/bionic64}}`

- Update all boxes that are in use in the current Vagrant environment:

`vagrant box update`

- Update a specific box:

`vagrant box update --box {{bento/debian-12}}`

- Check if there is a new version available for the box that you are using:

`vagrant box outdated`

- Clean up old versions of installed boxes:

`vagrant box prune`
