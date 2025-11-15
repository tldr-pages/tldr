# adig

> Muestra la información recibida de los servidores del Sistema de Nombres de Dominio (DNS).
> Más información: <https://manned.org/adig>.

- Muestra el registro A (predeterminado) desde DNS para el(los) nombre(s) de host:

`adig {{example.com}}`

- Muestra salida adicional de [d]epuración:

`adig -d {{example.com}}`

- Conecta a un [s]ervidor DNS especificado:

`adig -s {{1.2.3.4}} {{example.com}}`

- Usa un puerto TCP específico para conectarse a un servidor DNS:

`adig -T {{puerto}} {{example.com}}`

- Usa un puerto UDP específico para conectarse a un servidor DNS:

`adig -U {{puerto}} {{example.com}}`
