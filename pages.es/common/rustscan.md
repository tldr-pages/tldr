# rustscan

> Escáner de puertos rápido, escrito en Rust integrado con `nmap`.
> Más información: <https://github.com/RustScan/RustScan>.

- Escanea todos los puertos de una o más direcciones delimitadas por comas usando los valores predeterminados:

`rustscan --addresses {{ip_o_nombrehost}}`

- Escanea los [t]op 1000 puertos con detección de servicio y versión:

`rustscan --top --addresses {{dirección_o_direcciones}}`

- Escanea una lista específica de [p]uertos:

`rustscan --ports {{puerto1,puerto2,...,puertoN}} --addresses {{dirección_o_direcciones}}`

- Escanea un rango específico de puertos:

`rustscan --range {{inicio-fin}} --addresses {{dirección_o_direcciones}}`

- Añade argumentos de script a `nmap`:

`rustscan --addresses {{dirección_o_direcciones}} -- -A -sC`

- Escanea con un tamaño de lote ([b]atch) (por defecto: 4500) y [t]iempo de espera personalizado (por defecto: 1500ms):

`rustscan --batch-size {{tamaño_lote}} --timeout {{timeout}} --addresses {{dirección_o_direcciones}}`

- Escanea puertos en un orden específico:

`rustscan --scan-order {{serial|random}} --addresses {{dirección_o_direcciones}}`

- Escanea en modo "greppable" (solo imprime los puertos y no usa `nmap`):

`rustscan --greppable --addresses {{dirección_o_direcciones}}`
