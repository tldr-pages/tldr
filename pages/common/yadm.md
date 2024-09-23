# yadm

> A dotfiles manager that works by using git.
> The subcommands are just like git but you use yadm [command].
> You can use yadm (init | clone | push | pull).
> This command is one that allows you to pass flags to configure yadm.
> More information: <https://yadm.io/docs/overview>.

- Override the yadm directory. Yadm stores its configurations relative to this directory:

`yadm --yadm-dir`

- Override the yadm data directory: Yadm stores its data relative to this directory:

`yadm --yadm-data`

- Override the location of the yadm repository:

`yadm --yadm-repo`

- Override the location of the yadm configuration file:

`yadm --yadm-config`

- Override the location of the yadm encryption configuration:

`yadm  --yadm-encrypt`

- Override the location of the yadm encrypted files archive:

`yadm  --yadm-archive`

- Override the location of the yadm bootstrap program:

`yadm --yadm-bootstrap`
