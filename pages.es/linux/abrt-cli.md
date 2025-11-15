# abrt-cli

> Herramienta automática de reporte de errores para sistemas basados en Fedora.
> Se utiliza para detectar, analizar y notificar fallos de aplicaciones.
> Más información: <https://abrt.readthedocs.io/en/latest/usage.html>.

- Lista los problemas detectados:

`abrt-cli list`

- Muestra los detalles de un problema específico:

`abrt-cli info {{problema_id}}`

- Elimina un informe de fallo:

`abrt-cli remove {{problema_id}}`

- Informa de un problema al gestor de errores configurado (por ejemplo, Bugzilla):

`abrt-cli report {{problema_id}}`

- Monitorea un archivo de registro y activa un programa cuando se encuentra una coincidencia:

`abrt-watch-log -F {{cadena_error}} {{/var/log/myapp.log}} {{notify-send "Fallo detectado"}}`

- Genera un informe para depurar manualmente:

`abrt-cli report {{[-a|--analyze]}} {{problema_id}}`
