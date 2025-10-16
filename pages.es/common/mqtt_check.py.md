# mqtt_check.py

> Una simple utilidad para probar y validar las credenciales de inicio de sesión MQTT.
> Parte de la suite Impacket.
> Más información: <https://github.com/fortra/impacket>.

- Comprueba las credenciales de inicio de sesión MQTT para un objetivo (nombre del host del broker MQTT):

`mqtt_check.py {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{nombre_del_destino}}`

- Especifique un ID de cliente personalizado para la autenticación:

`mqtt_check.py -client-id {{id_cliente}} {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{nombre_del_destino}}`

- Habilita SSL para la conexión:

`mqtt_check.py -ssl {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{nombre_del_destino}}`

- Se conecta a un puerto específico (por defecto es 1883):

`mqtt_check.py -port {{puerto}} {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{nombre_del_destino}}`

- Habilita salida de depuración:

`mqtt_check.py -debug {{dominio}}/{{nombre_de_usuario}}:{{contraseña}}@{{nombre_del_destino}}`

- Muestra la ayuda:

`mqtt_check.py --help`
