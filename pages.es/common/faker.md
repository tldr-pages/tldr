# faker

> Una biblioteca Python y una herramienta para generar datos falsos.
> Más información: <https://faker.readthedocs.io/en/master/>.

- Muestra todos los proveedores de datos falsos junto con ejemplos:

`faker`

- Genera datos falsos de un tipo específico:

`faker {{name|address|passport_full|credit_card_full|phone_number|email|company|date_time|user_name|password|job|...}}`

- Genera un número de direcciones falsas de un país específico (usa `localectl list-locales | cut -d. -f1` para obtener la lista de locales):

`faker --repeat {{número}} --lang {{de_DE|de_CH|...}} address`

- Genera un número de ciudades en un país específico y las muestra en un archivo (usa `localectl list-locales | cut -d. -f1` para obtener la lista de locales):

`faker --repeat {{número}} --lang {{en_AU|en_US|...}} city -o {{ruta/a/archivo.txt}}`

- Genera una serie de agentes de usuario HTTP aleatorios mostrando una salida detallada:

`faker --repeat {{número}} --verbose user_agent`

- Genera un número de nombres de dominio y separa cada uno utilizando un separador específico:

`faker --repeat {{número}} --sep '{{,}}' domain_name`
