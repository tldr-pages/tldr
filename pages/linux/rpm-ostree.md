# rpm-ostree

> A hybrid image/package system.
> Manage ostree deployments, package layers, filesystem overlays, and boot configuration.
> More information: <https://coreos.github.io/rpm-ostree/administrator-handbook/>.

- Show rpm-ostree deployments in the order they will appear in the bootloader:

`rpm-ostree status`

- Show packages which are outdated and can be updated:

`rpm-ostree upgrade --preview`

- Prepare a new ostree deployment with upgraded packages and reboot into it:

`rpm-ostree upgrade --reboot`

- Reboot into the previous ostree deployment:

`rpm-ostree rollback --reboot`

- Install a package into a new ostree deployment and reboot into it:

`rpm-ostree install {{package}} --reboot`
