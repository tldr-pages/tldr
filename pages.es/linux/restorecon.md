# restorecon

> Restaura el contexto de seguridad de SELinux en archivos y directorios según las reglas persistentes.
> Vea también: `semanage-fcontext`.
> Más información: <https://manned.org/restorecon>.

- Muestra el contexto de seguridad actual de un archivo o directorio:

`ls {{[-dlZ|--directory -l --context]}} {{ruta/al/archivo_o_directorio}}`

- Restaura el contexto de seguridad de un archivo o directorio:

`restorecon {{ruta/al/archivo_o_directorio}}`

- Restaura el contexto de seguridad de un directorio de forma recursiva y muestra todas las etiquetas modificadas:

`restorecon -R -v {{ruta/al/directorio}}`

- Restaura el contexto de seguridad de un directorio de forma recursiva, utilizando todos los subprocesos disponibles, y muestra el progreso:

`restorecon -R -T {{0}} -p {{ruta/al/directorio}}`

- Previsualiza los cambios en las etiquetas que se producirían sin aplicarlos:

`restorecon -R -n -v {{ruta/al/directorio}}`
