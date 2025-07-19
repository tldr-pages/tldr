# eventcreate

> Crear entradas personalizadas en el registro de eventos.
> Los ID de evento pueden ser cualquier número entre 1 y 1000.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/eventcreate>.

- Crear un nuevo evento con un ID dado (1-1000) en el registro:

`eventcreate /t {{success|error|warning|information}} /id {{id}} /d "{{mensaje}}"`

- Crear un evento en un registro de eventos específico:

`eventcreate /l {{nombre_del_registro}} /t {{tipo}} /id {{id}} /d "{{mensaje}}"`

- Crear un evento con una fuente específica:

`eventcreate /so {{nombre_de_la_fuente}} /t {{tipo}} /id {{id}} /d "{{mensaje}}"`

- Crear un evento en el registro de eventos de una máquina remota:

`eventcreate /s {{nombre_del_host}} /u {{nombre_de_usuario}} /p {{contraseña}} /t {{tipo}} /id {{id}} /d "{{mensaje}}"`
