# autorecon

> Herramienta de reconocimiento de red multihilo que realiza una enumeración automatizada de servicios.
> Más información: <https://github.com/Tib3rius/AutoRecon>.

- Realiza reconocimiento sobre el(los) host(s) objetivo(s) (los resultados del escaneo detallado se guardarán en `./results`):

`sudo autorecon {{host_o_ip1,host_o_ip2,...}}`

- Realiza reconocimiento sobre el(los) objetivo(s) desde un archivo:

`sudo autorecon --target-file {{ruta/al/archivo}}`

- Guarda los resultados en un directorio diferente:

`sudo autorecon --output {{ruta/a/resultados}} {{host_o_ip1,host_o_ip2,...}}`

- Limita el escaneo a [p]uertos y protocolos específicos (`T` para TCP, `U` para UDP, `B` para ambos):

`sudo autorecon --ports {{T:21-25,80,443,U:53,B:123}} {{host_o_ip1,host_o_ip2,...}}`
