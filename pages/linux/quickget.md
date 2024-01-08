# quickget

> Download and prepare materials for building a Quickemu virtual machine.
> NOTE: the parameter "edition" is always optional.
> See also: `quickemu`.
> More information: <https://github.com/quickemu-project/quickemu>.

- Display the list of all supported guest OSes, versions and variants:

`quickget list`

- Download and create the virtual machine configuration for building a Quickemu virtual machine for an OS:

`quickget {{os}} {{release}} {{edition}}`

- Download configuration for a Windows 11 VM with VirtIO drivers for Windows:

`quickget windows 11`

- Download a macOS recovery image and creates a virtual machine configuration:

`quickget macos {{high-sierra|mojave|catalina|big-sur|monterey|ventura}}`

- Show an ISO URL for an OS (does not work for Windows):

`quickget --show-iso-url fedora {{release}} {{edition}}`

- Test if an OS ISO is available for an OS:

`quickget --test-iso-url nixos {{edition}} {{plasma5}}`

- Open an OS distribution's homepage in a browser (does not work for Windows):

`quickget --open-distro-homepage {{os}}`
