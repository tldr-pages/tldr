# vagrant init

> Initializes the current directory to be a Vagrant environment by creating a `Vagrantfile`.
> See also: `vagrant`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/init>.

- Create a `Vagrantfile`:

`vagrant init`

- Create a `Vagrantfile` without instructional comments:

`vagrant init --minimal`

- Specify the box name and url:

`vagrant init {{box_name}} {{box_url}}`

- Specify the box version:

`vagrant init --box-version {{version_num}}`

- Send the `Vagrantfile` to stdout:

`vagrant init --output -`

- Overwrite any existing `Vagrantfile`:

`vagrant init --force`

- Provide a custom ERB template for generating the `Vagrantfile`:

`vagrant init --template {{path/to/file.erb}}`
