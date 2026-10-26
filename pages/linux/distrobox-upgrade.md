# distrobox upgrade

> Upgrade one or more Distrobox containers using each container's package manager.
> See also: `distrobox`.
> More information: <https://distrobox.it/usage/distrobox-upgrade/>.

- Upgrade a container:

`distrobox upgrade {{container_name}}`

- Upgrade every container:

`distrobox upgrade {{[-a|--all]}}`

- Upgrade only containers that are already running:

`distrobox upgrade {{[-a|--all]}} --running`

- Upgrade specific containers:

`distrobox upgrade {{container1 container2 ...}}`
