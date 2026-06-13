# pcapfix

> Repara archivos PCAP y PcapNG dañados o corruptos.
> Más información: <https://f00l.de/pcapfix/>.

- Repara un archivo PCAP/PcapNG (Nota: para los archivos PCAP, sólo se escanean los primeros 262144 bytes de cada paquete):

`pcapfix {{ruta/al/archivo.pcapng}}`

- Repara un archivo PCAP completo:

`pcapfix --deep-scan {{ruta/al/archivo.pcap}}`

- Repara un archivo PCAP/PcapNG y escribe el archivo reparado en la ubicación especificada:

`pcapfix --outfile {{ruta/al/archivo_reparado.pcap}} {{ruta/al/archivo.pcap}}`

- Repara un archivo PcapNG y lo trata como un archivo PcapNG, ignorando el reconocimiento automático:

`pcapfix --pcapng {{ruta/al/archivo.pcapng}}`

- Repara un archivo y muestra el proceso en detalle:

`pcapfix --verbose {{ruta/al/archivo.pcap}}`
