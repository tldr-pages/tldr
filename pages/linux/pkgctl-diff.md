# pkgctl diff

> Compare package files using different modes.
> See also: `pkgctl`.
> More information: <https://manned.org/pkgctl-diff>.

- Compare package files in tar content list different mode (default):

`pkgctl diff {{[-l|--list]}} {{path/to/file|pkgname}}`

- Compare package files in diffoscope different mode:

`pkgctl diff {{[-d|--diffoscope]}} {{path/to/file|pkgname}}`

- Compare package files in `.PKGINFO` different mode:

`pkgctl diff {{[-p|--pkginfo]}} {{path/to/file|pkgname}}`

- Compare package files in `.BUILDINFO` different mode:

`pkgctl diff {{[-b|--buildinfo]}} {{path/to/file|pkgname}}`
