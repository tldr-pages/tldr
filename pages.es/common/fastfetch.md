# fastfetch

> Muestra información sobre el sistema operativo, el software y el hardware.
> Más información: <https://manned.org/fastfetch>.

- Muestra la información del sistema:

`fastfetch`

- Muestra toda la información del sistema con todos los módulos activados:

`fastfetch {{[-c|--config]}} all`

- Carga un archivo de configuración personalizado:

`fastfetch {{[-c|--config]}} {{ruta/al/archivo_de_configuración}}`

- Obtiene una estructura específica:

`fastfetch {{[-s|--structure]}} {{os:kernel:de:cpu:gpu}}`

- Usa un logo específico:

`fastfetch {{[-l|--logo]}} {{logo}}`

- Muestra la información del sistema sin logo:

`fastfetch {{[-l|--logo]}} none`

- Usa un color específico para las etiquetas y el título:

`fastfetch --color {{blue}}`
