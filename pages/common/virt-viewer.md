# virt-viewer

> Minimal graphical interface for a virtual machine (VM).
> Note: `domain` refers to the name, UUID, or ID for the existing VMs.
> See also: `virsh`.
> More information: <https://manned.org/virt-viewer>.

- Launch `virt-viewer` with a prompt to select running virtual machines:

`virt-viewer {{[-c|--connect]}} {{qemu:///system|qemu:///session|...}}`

- Launch `virt-viewer` for a specific virtual machine by ID, UUID, or name:

`virt-viewer {{[-c|--connect]}} {{URI}} {{domain}}`

- Wait for a virtual machine to start and automatically reconnect if it shuts down and restarts:

`virt-viewer {{[-c|--connect]}} {{URI}} {{[-r|--reconnect]}} {{[-w|--wait]}} {{domain}}`

- Connect to a specific remote virtual machine over TLS (requires pre-configured TLS certificates):

`virt-viewer {{[-c|--connect]}} {{qemu+tls://host/system}} {{domain}}`

- Connect to a specific remote virtual machine over SSH (requires SSH access to the host):

`virt-viewer {{[-c|--connect]}} {{xen+ssh://username@host/system}} {{domain}}`
