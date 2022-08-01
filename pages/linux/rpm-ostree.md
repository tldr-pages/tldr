# rpm-ostree

> A hybrid image/package system.
> Manage ostree deployments, package layers, filesystem overlays, and boot configuration.
> More information: <https://coreos.github.io/rpm-ostree/administrator-handbook/>.

- Show rpm-ostree deployments in the order they'll appear in the bootloader:

`rpm-ostree status`

- Show package updates that will be performed on the next rpm-ostree upgrade:

`rpm-ostree upgrade --preview`

- Prepare a new ostree deployment with upgraded packages and reboot into the new deployment:

`rpm-ostree upgrade --reboot`

- Roll back and reboot into the previous ostree deployment:

`rpm-ostree rollback --reboot`

- Install a package into a new ostree deployment and apply that deployment to the live deployment:

`rpm-ostree install <htop> --apply-live`

- Install a package into a new ostree deployment and reboot into the new deployment:

`rpm-ostree install <htop> --reboot`
