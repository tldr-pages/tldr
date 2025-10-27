# toolbox enter

> Enter a `toolbox` container for interactive use.
> See also: `toolbox run`.
> More information: <https://manned.org/toolbox-enter.1>.

- Enter a `toolbox` container using the default image of a specific distribution:

`toolbox enter {{[-d|--distro]}} {{distribution}}`

- Enter a `toolbox` container using the default image of a specific release of the current distribution:

`toolbox enter {{[-r|--release]}} {{release}}`

- Enter a toolbox container using the default image for Fedora 42:

`toolbox enter {{[-d|--distro]}} {{fedora}} {{[-r|--release]}} {{f42}}`
