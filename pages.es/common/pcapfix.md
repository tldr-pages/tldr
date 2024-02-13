# pcapfix

> Repara archivos `pcap` y `pcapng` dañados o corruptos.
> Más información: <https://f00l.de/pcapfix/>.

- Repara un archivo `pcap`/`pcapng` (Nota: para los archivos `pcap`, sólo se escanean los primeros 262144 bytes de cada paquete):

`pcapfix {{ruta/al/archivo.pcapng}}`

- Repara un archivo `pcap` completo:

`pcapfix --deep-scan {{ruta/al/archivo.pcap}}`

- Repara un archivo `pcap`/`pcapng` y escribe el archivo reparado en la ubicación especificada:

`pcapfix --outfile {{ruta/al/archivo_reparado.pcap}} {{ruta/al/archivo.pcap}}`

- Repara un archivo `pcapng` y lo trata como un archivo `pcapng`, ignorando el reconocimiento automático:

`pcapfix --pcapng {{ruta/al/archivo.pcapng}}`

- Repara un archivo y muestra el proceso en detalle:

`pcapfix --verbose {{ruta/al/archivo.pcap}}`
