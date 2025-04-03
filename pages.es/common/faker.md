# faker

> Una biblioteca Python y una herramienta para generar datos falsos.
> Más información: <https://faker.readthedocs.io/en/master/>.

- Muestra todos los proveedores de datos falsos junto con ejemplos:

`faker`

- Genera datos falsos de un tipo específico:

`faker {{nombre|dirección|pasaporte_completo|tarjeta_de_crédito_completa|número_teléfono|email|empresa|fecha_hora|nombre_usuario|contraseña|trabajo|...}}`

- Genera un número de direcciones falsas de un país específico (usa `localectl list-locales | cut -d. -f1` para obtener la lista de locales):

`faker --repeat {{número}} --lang {{de_DE|de_CH|...}} address`

- Genera un número de ciudades en un país específico y las muestra en un archivo (usa `localectl list-locales | cut -d. -f1` para obtener la lista de locales):

`faker --repeat {{número}} --lang {{en_AU|en_US|...}} city -o {{ruta/a/archivo.txt}}`

- Genera una serie de agentes de usuario HTTP aleatorios mostrando una salida detallada:

`faker --repeat {{número}} --verbose usuario_agente`

- Genera un número de nombres de dominio y separa cada uno utilizando un separador específico:

`faker --repeat {{número}}} --sep '{{,}}' nombre_dominio`
