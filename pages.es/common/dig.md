# dig

> Utilidad de consulta para DNS.
> Más información: <https://manned.org/dig>.

- Consulta la(s) IP(s) asociadas a un nombre de equipo (registros A):

`dig +short {{example.com}}`

- Obtén una respuesta detallada para un dominio determinado (registros A):

`dig +noall +answer {{example.com}}`

- Consulta un tipo de registro DNS específico asociado a un dominio determinado:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- Especifica un servidor DNS alterno a consultar:

`dig @{{8.8.8.8}} {{example.com}}`

- Realiza una búsqueda DNS inversa para una dirección IP (registro PTR):

`dig -x {{8.8.8.8}}`

- Encuentra servidores de nombre autoritativos para la zona y muestra registros SOA:

`dig +nssearch {{example.com}}`

- Realiza consultas iterativas y muestra el trazado de ruta completo para resolver un dominio:

`dig +trace {{example.com}}`
