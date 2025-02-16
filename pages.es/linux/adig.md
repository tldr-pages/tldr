# adig

> Muestra la información recibida de los servidores del Sistema de Nombres de Dominio (DNS).
> Más información: <https://manned.org/adig>.

- Muestra el registro A (predeterminado) desde DNS para el(los) nombre(s) de host:

`adig {{ejemplo.com}}`

- Muestra salida adicional de [d]epuración:

`adig -d {{ejemplo.com}}`

- Conecta a un [s]ervidor DNS especificado:

`adig -s {{1.2.3.4}} {{ejemplo.com}}`

- Usa un puerto TCP específico para conectarte a un servidor DNS:

`adig -T {{puerto}} {{ejemplo.com}}`

- Usa un puerto UDP específico para conectarte a un servidor DNS:

`adig -U {{puerto}} {{ejemplo.com}}`
