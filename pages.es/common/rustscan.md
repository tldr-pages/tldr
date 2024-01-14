# rustscan

> Escáner rápido de puertos escrito en Rust con `nmap` incorporado.
> Más información: <https://github.com/RustScan/RustScan>.

- Escanea todos los puertos de una o más direcciones delimitadas por comas usando los valores por defecto:

`rustscan --addresses {{ip_o_nombreHost}}`

- Escanea los [t]op 1000 puertos con detección de servicio y versión:

`rustscan --top --addresses {{dirección_o_direcciones}}`

- Escanea una lista específica de [p]uertos:

`rustscan --ports {{puerto1,puerto2,...,puertoN}} --addresses {{dirección_o_direcciones}}`

- Escanea un rango específico de puertos:

`rustscan --range {{inicio-fin}} --addresses {{dirección_o_direcciones}}`

- Añade argumentos de script a `nmap`:

`rustscan --addresses {{dirección_o_direcciones}} -- -A -sC`

- Escanea con tamaño de [b]atch personalizado (por defecto: 4500) y [t]imeout (por defecto: 1500ms):

`rustscan --batch-size {{tamaño_lote}} --timeout {{timeout}} --addresses {{dirección_o_direcciones}}`

- Escanea con un orden de puertos específico:

`rustscan --scan-order {{serial|aleatorio}} --addresses {{dirección_o_direcciones}}`

- Escanea en modo greppable (modalidad solo salida de los puertos, sin `nmap`):

`rustscan --greppable --addresses {{dirección_o_direcciones}}`
