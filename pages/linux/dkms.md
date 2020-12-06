# dkms

> A framework that allows for dynamic building of kernel modules.
> More information: <https://github.com/dell/dkms>.

- List currently installed modules:

`dkms status`

- Rebuild all modules for the currently running kernel:

`dkms autoinstall`

- Install version 1.2.1 of the acpi_call module for the currently running kernel:

`dkms install -m {{acpi_call}} -v {{1.2.1}}`

- Remove version 1.2.1 of the acpi_call module from all kernels:

`dkms remove -m {{acpi_call}} -v {{1.2.1}} --all`
