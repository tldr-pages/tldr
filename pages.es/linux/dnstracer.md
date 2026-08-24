# dnstracer

> El comando dnstracer determina de dónde obtiene la información un servidor DNS.
> Más información: <https://manned.org/dnstracer>.

- Averigua de dónde obtuvo tu servidor DNS local la información sobre www.example.com:

`dnstracer {{www.example.com}}`

- Empieza con un DNS específico que ya conozcas:

`dnstracer -s {{dns.example.org}} {{www.example.com}}`

- Consulta solo servidores IPv[4]:

`dnstracer -4 {{www.example.com}}`

- Vuelve a intentar cada solicitud 5 veces en caso de fallo:

`dnstracer -r {{5}} {{www.example.com}}`

- Muestra todos los pasos durante la ejecución:

`dnstracer -v {{www.example.com}}`

- Muestra un resumen de todas las respuestas recibidas tras la ejecución:

`dnstracer -o {{www.example.com}}`
