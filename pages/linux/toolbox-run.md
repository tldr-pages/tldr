# toolbox run

> Run a command in an existing `toolbox` container.
> See also: `toolbox enter`.
> More information: <https://manned.org/toolbox-run>.

- Run a command inside a specific `toolbox` container:

`toolbox run {{[-c|--container]}} {{container_name}} {{command}}`

- Run a command inside a `toolbox` container for a specific release of a distribution:

`toolbox run {{[-d|--distro]}} {{distribution}} {{[-r|--release]}} {{release}} {{command}}`

- Run `emacs` inside a `toolbox` container using the default image for a specific Fedora release:

`toolbox run {{[-d|--distro]}} {{fedora}} {{[-r|--release]}} f{{version}} {{emacs}}`
