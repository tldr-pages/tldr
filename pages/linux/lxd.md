# lxd

> The LXD daemon, a manager for containers and virtual machines.
> Usually started by the init system and used through `lxc`.
> See also: `lxc`.
> More information: <https://canonical.com/lxd/docs/latest/howto/initialize/>.

- Initialize LXD interactively:

`sudo lxd init`

- Initialize LXD with a default configuration:

`sudo lxd init --minimal`

- Initialize LXD non-interactively from a preseed file:

`sudo lxd init --preseed < {{path/to/preseed.yaml}}`

- Start the daemon and allow members of a specific group to talk to it:

`sudo lxd --group {{group}}`

- Wait until the daemon is ready to handle requests:

`sudo lxd waitready`

- Stop all instances and shut down the daemon:

`sudo lxd shutdown`

- Display help:

`lxd {{[-h|--help]}}`

- Display version:

`lxd --version`
