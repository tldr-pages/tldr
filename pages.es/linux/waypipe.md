# waypipe

> Ejecuta aplicaciones gráficas de forma remota bajo un compositor Wayland.
> Más información: <https://manned.org/waypipe>.

- Ejecuta un programa gráfico de forma remota y lo muestra de forma local:

`waypipe ssh {{usuario}}@{{servidor}} {{programa}}`

- Abre un túnel SSH para ejecutar cualquier programa de forma remota y lo muestra de forma local:

`waypipe ssh{{usuario}}@{{servidor}}`

- Omite la prueba de compatibilidad con Vulkan:

`waypipe --test-skip-vulkan ssh {{usuario}}@{{servidor}} {{programa}}`

- Muestra la ayuda:

`waypipe {{[-h|--help]}}`
