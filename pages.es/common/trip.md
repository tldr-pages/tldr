# trip

> Una herramienta de diagnóstico de red.
> Combina la funcionalidad de `traceroute` y `ping`.
> Diseñada para ayudar en el análisis de problemas de red.
> Más información: <https://trippy.rs/reference/cli/>.

- Uso básico con parámetros por defecto:

`sudo trip {{example.com}}`

- Rastrea sin requerir privilegios elevados (solo plataformas soportadas):

`trip {{example.com}} --unprivileged`

- Rastrea solo con `IPv6`:

`sudo trip {{example.com}} --ipv6`

- Rastrea usando el protocolo `udp`:

`sudo trip {{example.com}} --protocol {{udp}}`

- Utiliza el puerto de destino personalizado `443` para el rastreo `tcp`:

`sudo trip {{example.com}} --protocol {{tcp}} --target-port {{443}}`

- Utiliza el puerto de origen personalizado `5000` para el seguimiento `udp`:

`sudo trip {{example.com}} --protocol {{udp}} --source-port {{5000}}`
