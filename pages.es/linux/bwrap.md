# bwrap

> Ejecuta programas en un sandbox ligero.
> Más información: <https://manned.org/bwrap>.

- Ejecuta un programa en un entorno de sólo lectura:

`bwrap --ro-bind / / {{/bin/bash}}`

- Da al entorno acceso a dispositivos, información de procesos y crea un `tmpfs` para el mismo:

`bwrap --dev-bind /dev /dev --proc /proc --ro-bind / / --tmpfs /tmp {{/bin/bash}}`
