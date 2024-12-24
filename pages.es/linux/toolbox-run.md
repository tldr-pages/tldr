# toolbox run

> Ejecuta un comando en un contenedor existente de `toolbox`.
> Vea también: `toolbox enter`.
> Más información: <https://manned.org/toolbox-run>.

- Ejecuta un comando dentro de un contenedor específico `toolbox`:

`toolbox run --container {{nombre_del_contenedor}} {{comando}}`

- Ejecuta un comando dentro de un contenedor `toolbox` para una liberación específica de una distribución:

`toolbox run --distro {{distribution}} --release {{release}} {{comando}}`

- Ejecuta `emacs` dentro de un contenedor `toolbox` utilizando la imagen predeterminada de Fedora 39:

`toolbox run --distro {{fedora}} --release {{f39}} {{emacs}}`
