# dkms

> A framework that allows for dynamic building of kernel modules.
> More information: <https://manned.org/dkms>.

- List currently installed modules:

`dkms status`

- Rebuild all modules for the currently running kernel:

`sudo dkms autoinstall`

- Install version 1.2.1 of the acpi_call module for the currently running kernel:

`sudo dkms install -m {{acpi_call}} -v {{1.2.1}}`

- Remove version 1.2.1 of the acpi_call module from all kernels:

`sudo dkms remove -m {{acpi_call}} -v {{1.2.1}} --all`
