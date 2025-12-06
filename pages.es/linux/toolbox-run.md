# toolbox run

> Ejecuta un comando en un contenedor existente de Toolbx.
> Vea también: `toolbox enter`.
> Más información: <https://manned.org/toolbox-run>.

- Ejecuta un comando dentro de un contenedor específico Toolbx:

`toolbox run --container {{nombre_del_contenedor}} {{comando}}`

- Ejecuta un comando dentro de un contenedor Toolbx para una liberación específica de una distribución:

`toolbox run --distro {{distribución}} --release {{lanzamiento}} {{comando}}`

- Ejecuta `emacs` dentro de un contenedor Toolbx utilizando la imagen predeterminada de Fedora 39:

`toolbox run --distro {{fedora}} --release {{f39}} {{emacs}}`
