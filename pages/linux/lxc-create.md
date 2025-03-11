# lxc-create

> Create linux containers.
> More information: <https://linuxcontainers.org/lxc/getting-started>.

- Create a container interactively in `/var/lib/lxc/`:

`sudo lxc-create --name {{container_name}} --template download`

- Create a container in a target directory:

`sudo lxc-create --lxcpath {{/path/to/directory/}} --name {{container_name}} --template download`

- Create a container passing options to a template:

`sudo lxc-create --name {{container_name}} --template download -- --dist {{distro-name}} --release {{release-version}} --arch {{arch}}`
