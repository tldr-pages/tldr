# aria2c

> Utilidad de descarga rápida.
> Soporta HTTP(S), FTP, SFTP, BitTorrent y Metalink.
> Más información: <https://aria2.github.io>.

- Descarga un URI específico a un archivo:

`aria2c "{{url}}"`

- Descarga un archivo de una URI con un nombre de salida específico:

`aria2c --out {{ruta/al/archivo}} "{{url}}"`

- Descarga varios archivos diferentes en paralelo:

`aria2c --force-sequential {{false}} "{{url1 url2 ...}}"`

- Descarga el mismo archivo desde diferentes espejos y verifica la suma de comprobación del archivo descargado:

`aria2c --checksum {{sha-256}}={{suma_de_comprobación}} "{{url1}}" "{{url2}}" "{{urlN}}"`

- Descarga las URI enumeradas en un archivo con un número determinado de descargas paralelas:

`aria2c --input-file {{ruta/al/archivo}} --max-concurrent-downloads {{número_de_descargas}}`

- Descarga con varias conexiones:

`aria2c --split {{número_de_conexiones}} "{{url}}"`

- Descarga a través de FTP con un nombre de usuario y contraseña:

`aria2c --ftp-user {{usuario}} --ftp-passwd {{contraseña}} "{{url}}"`

- Limita la velocidad de descarga en bytes por segundo:

`aria2c --max-download-limit {{velocidad}} "{{url}}"`
