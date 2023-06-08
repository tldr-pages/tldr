# toolbox run

> Run a command in an existing `toolbox` container.
> See also: `toolbox enter`.
> More information: <https://manned.org/toolbox-run>.

- Run a command inside a specific `toolbox` container:

`toolbox run --container {{container_name}} {{command}}`

- Run a command inside a `toolbox` container for a specific release of a distribution:

`toolbox run --distro {{distribution}} --release {{release}} {{command}}`

- Run `emacs` inside a `toolbox` container using the default image for Fedora 38:

`toolbox run --distro {{fedora}} --release {{f38}} {{emacs}}`
