# qm suspend

Suspends a virtual machine (VM) in the Proxmox Virtual Environment (PVE) cluster using the "qm" command-line tool.

> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

## Options

- `-id <vmid>` or `--vmid <vmid>`: Specifies the ID of the virtual machine to suspend.

- `-skiplock`: Skips the lock check when suspending the VM. Use with caution, as it may lead to data corruption in certain situations.

- `-skiplockstorage`: Skips the lock check for storage when suspending the VM. Use with caution, as it may lead to data corruption in certain situations.

## Usage

Suspend a virtual machine with the ID 101:

```bash
qm suspend -id 101
