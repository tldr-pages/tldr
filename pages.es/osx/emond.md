# emond

> Servicio de Monitor de Eventos que acepta eventos de varios servicios, los ejecuta a través de un simple motor de reglas, y toma acciones.
> Las acciones pueden ejecutar comandos, enviar correos electrónicos o mensajes SMS.
> Más información: <https://www.manpagez.com/man/8/emond/>.

- Inicia el daemon:

`emond`

- Especifica las reglas que emond debe procesar indicando una ruta a un archivo o directorio:

`emond -r {{ruta/al/archivo_o_directorio}}`

- Utiliza un archivo de configuración específico:

`emond -c {{ruta/al/archivo_de_configuración}}`
