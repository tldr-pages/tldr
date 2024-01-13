# quickget

> Download and prepare materials for building a Quickemu virtual machine.
> NOTE: the parameter "edition" is always optional.
> See also: `quickemu`.
> More information: <https://github.com/quickemu-project/quickemu>.

- Display the list of all supported guest operating systems, versions and variants:

`quickget list`

- Download and create the virtual machine configuration for building a Quickemu virtual machine for an OS:

`quickget {{os}} {{release}} {{edition}}`

- Download configuration for a Windows 11 VM with VirtIO drivers for Windows:

`quickget windows 11`

- Download a macOS recovery image and creates a virtual machine configuration:

`quickget macos {{high-sierra|mojave|catalina|big-sur|monterey|ventura}}`

- Show an ISO URL for an operating system (Note: it does not work for Windows):

`quickget --show-iso-url fedora {{release}} {{edition}}`

- Test if an ISO file is available for an operating system:

`quickget --test-iso-url nixos {{edition}} {{plasma5}}`

- Open an operating system distribution's homepage in a browser (Note: it does not work for Windows):

`quickget --open-distro-homepage {{os}}`
