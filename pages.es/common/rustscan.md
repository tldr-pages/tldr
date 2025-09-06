# rustscan

> Escáner de puertos rápido, escrito en Rust integrado con `nmap`.
> Más información: <https://github.com/bee-san/RustScan/wiki>.

- Escanea todos los puertos de una o más direcciones delimitadas por comas usando los valores predeterminados:

`rustscan {{[-a|--addresses]}} {{ip_o_nombrehost}}`

- Escanea los top 1000 puertos con detección de servicio y versión:

`rustscan --top {{[-a|--addresses]}} {{dirección_o_direcciones}}`

- Escanea una lista específica de puertos:

`rustscan {{[-p|--ports]}} {{puerto1,puerto2,...,puertoN}} {{[-a|--addresses]}} {{dirección_o_direcciones}}`

- Escanea un rango específico de puertos:

`rustscan {{[-r|--range]}} {{inicio}}-{{fin}} {{[-a|--addresses]}} {{dirección_o_direcciones}}`

- Añade argumentos de script a `nmap`:

`rustscan {{[-a|--addresses]}} {{dirección_o_direcciones}} -- -O {{[-sC|--script=default]}}`

- Escanea con un tamaño de lote (por defecto: 4500) y tiempo de espera personalizado (por defecto: 1500ms):

`rustscan {{[-b|--batch-size]}} {{tamaño_lote}} {{[-t|--timeout]}} {{timeout}} {{[-a|--addresses]}} {{dirección_o_direcciones}}`

- Escanea puertos en un orden específico:

`rustscan --scan-order {{serial|random}} {{[-a|--addresses]}} {{dirección_o_direcciones}}`

- Escanea en modo "greppable" (solo imprime los puertos y no usa `nmap`):

`rustscan {{[-g|--greppable]}} {{[-a|--addresses]}} {{dirección_o_direcciones}}`
