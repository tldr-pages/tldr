# lxc-create

> Create linux containers.
> More information: <https://linuxcontainers.org/>.

- Create a container interactively in `/var/lib/lxc/`:

`lxc-create --name {{container}} --template download`

- Create a container in a target directory:

`lxc-create --lxcpath {{/path/to/directory/}} --name {{container}} --template download`

- Create a container passing options to a template:

`lxc-create --name {{name}} --template download -- --dist {{distro-name}} --release {{release-version}} --arch {{arch}}`
