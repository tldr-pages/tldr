# quickget

> Download and prepare materials for building a Quickemu virtual machine.
> Note: The parameter "edition" is always optional.
> See also: `quickemu`.
> More information: <https://github.com/quickemu-project/quickemu>.

- Display the list of all supported guest operating systems, versions and variants:

`quickget list`

- Download and create the virtual machine configuration for building a Quickemu virtual machine for an OS:

`quickget {{os}} {{release}} {{edition}}`

- Download configuration for a Windows 11 VM with VirtIO drivers for Windows:

`quickget windows 11`

- Download a macOS recovery image and creates a virtual machine configuration:

`quickget macos {{mojave|catalina|big-sur|monterey|ventura|sonoma}}`

- Show an ISO URL for an operating system:

`quickget --url fedora {{release}} {{edition}}`

- Test if an ISO file is available for an operating system:

`quickget --check nixos {{release}} {{edition}}`

- Download an image without building any VM configuration:

`quickget --download {{os}} {{release}} {{edition}}`

- Create a VM configuration for an OS image:

`quickget --create-config {{os}} {{path/to/iso}}`
