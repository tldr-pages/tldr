# bwrap

> Run programs in a lightweight sandbox.
> More information: <https://manned.org/bwrap>.

- Run a program in a read-only environment:

`bwrap --ro-bind / / {{/bin/bash}}`

- Give the environment access to devices, process information and create a `tmpfs` for it:

`bwrap --dev-bind /dev /dev --proc /proc --ro-bind / / --tmpfs /tmp {{/bin/bash}}`
