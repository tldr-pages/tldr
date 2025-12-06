# vagrant init

> Initialize the current directory to be a Vagrant environment by creating a `Vagrantfile`.
> See also: `vagrant`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/init>.

- Create a `Vagrantfile`:

`vagrant init`

- Create a `Vagrantfile` without instructional comments:

`vagrant init {{[-m|--minimal]}}`

- Specify the box name and URL:

`vagrant init {{box_name}} {{box_url}}`

- Create a `Vagrantfile` with a specific box version:

`vagrant init --box-version {{version}} {{box_name}}`

- Send the `Vagrantfile` to `stdout`:

`vagrant init {{[-o|--output]}} -`

- Overwrite any existing `Vagrantfile`:

`vagrant init {{[-f|--force]}}`

- Provide a custom ERB template for generating the `Vagrantfile`:

`vagrant init --template {{path/to/file.erb}}`
