# whatweb

> Escáner web de nueva generación.
> Más información: <https://github.com/urbanadventurer/WhatWeb#usage>.

- Escanea sitios web/objetivos en busca de tecnologías web:

`whatweb {{website1 website2 ...}}`

- Lee objetivos/sitios web desde un archivo:

`whatweb {{[-i|--input-file]}} {{archivo_objetivos}}`

- Analiza un sitio web/objetivo en modo detallado:

`whatweb {{[-v|--verbose]}} {{example.com}}`

- Ejecuta un escaneo agresivo en un sitio web:

`whatweb {{[-a|--aggression]}} 3 {{example.com}}`

- Escanea una red y suprime los errores:

`whatweb --no-errors {{192.168.0.0/24}}`

- Lista de complementos:

`whatweb {{[-l|--list-plugins]}}`

- Lista de complementos:

`whatweb {{[-I|--info-plugins]}} {{nombre_del_complemento}}`
