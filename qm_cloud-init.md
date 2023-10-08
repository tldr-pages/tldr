# qm cloud-init

> used to configure cloud-init settings for virtual machines managed by Proxmox Virtual Environment (Proxmox VE) on a Linux OS.
> More information: [Cloud-Init Support](https://pve.proxmox.com/wiki/Cloud-Init_Support)

## Syntax
`qm cloud-init <vmid> <options>`

## Parameters
`vmid`: The ID of the virtual machine for which you want to configure cloud-init settings.

## Options
-name <name>: Set the name of the cloud-init configuration. This is an optional human-readable identifier for the configuration.

-user <user>: Specify the cloud-init user that this configuration applies to. This is usually the username for SSH access.

-password <password>: Set the password for the specified user. You can use this option if you want to set an initial password for the user account.

-sshkey <sshkey>: Provide an SSH public key to be added to the authorized_keys file of the specified user. This allows SSH access without a password.

-hostname <hostname>: Set the hostname for the virtual machine.

-ipconfig <ipconfig>: Configure network interfaces with IP addresses, gateway, and DNS servers. Use CIDR notation for specifying IP addresses.

-pre <script>: Execute a shell script before cloud-init is run on the virtual machine. This can be useful for performing additional configuration tasks.