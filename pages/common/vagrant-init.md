# vagrant init

> Initialize the current directory with a Vagrantfile.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/init>.

- Create a default Vagrantfile in the current directory:

`vagrant init`

- Initialize a Vagrantfile that uses a specific box:

`vagrant init {{hashicorp/bionic64}}`

- Generate a minimal Vagrantfile without inline comments:

`vagrant init --minimal {{hashicorp/bionic64}}`

- Overwrite an existing Vagrantfile:

`vagrant init --force {{hashicorp/bionic64}}`

- Output the generated Vagrantfile to a specific path:

`vagrant init --output {{path/to/Vagrantfile.local}} {{hashicorp/bionic64}}`

- Specify a box version constraint while initializing:

`vagrant init --box-version "{{>= 1.2.3}}" {{hashicorp/bionic64}}`
