# toolbox create

> Create a new Toolbx container.
> More information: <https://manned.org/toolbox-create>.

- Create a Toolbx container for a specific distribution:

`toolbox create {{[-d|--distro]}} {{distribution}}`

- Create a Toolbx container for a specific release of the current distribution:

`toolbox create {{[-r|--release]}} {{release}}`

- Create a Toolbx container with a custom image:

`toolbox create {{[-i|--image]}} {{name}}`

- Create a Toolbx container from a custom Fedora image:

`toolbox create {{[-i|--image]}} {{quay.io/fedora/fedora:tag}}`

- Create a Toolbx container using the default image for a specific Fedora release:

`toolbox create {{[-d|--distro]}} {{fedora}} {{[-r|--release]}} f{{version}}`
