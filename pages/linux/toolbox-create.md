# toolbox create

> Create a new `toolbox` container.
> More information: <https://manned.org/toolbox-create.1>.

- Create a `toolbox` container for a specific distribution:

`toolbox create --distro {{distribution}}`

- Create a `toolbox` container for a specific release of the current distribution:

`toolbox create --release {{release}}`

- Create a `toolbox` container with a custom image:

`toolbox create --image {{name}}`

- Create a `toolbox` container from a custom Fedora image:

`toolbox create --image {{registry.fedoraproject.org/fedora-toolbox:36}}`

- Create a `toolbox` container using the default image for Fedora 36:

`toolbox create --distro {{fedora}} --release {{f36}}`
