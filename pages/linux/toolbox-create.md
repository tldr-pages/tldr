# toolbox create

> Create a new `toolbox` container.
> More information: <https://manned.org/toolbox-create>.

- Create a `toolbox` container for a specific distribution:

`toolbox create {{[-d|--distro]}} {{distribution}}`

- Create a `toolbox` container for a specific release of the current distribution:

`toolbox create {{[-r|--release]}} {{release}}`

- Create a `toolbox` container with a custom image:

`toolbox create {{[-i|--image]}} {{name}}`

- Create a `toolbox` container from a custom Fedora image:

`toolbox create {{[-i|--image]}} {{quay.io/fedora/fedora:tag}}`

- Create a `toolbox` container using the default image for a specific Fedora release:

`toolbox create {{[-d|--distro]}} {{fedora}} {{[-r|--release]}} f{{version}}`
