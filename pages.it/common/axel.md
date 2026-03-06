# axel

> Acceleratore di download.
> Supporta HTTP, HTTPS, FTP e FTPS.
> Vedi anche: `aria2c`.
> Maggiori informazioni: <https://manned.org/axel>.

- Scarica un URL in un file:

`axel {{url}}`

- Scarica e specifica un file di output:

`axel {{url}} {{[-o|--output]}} {{path/to/file}}`

- Scarica con un numero specifico di connessioni:

`axel {{[-n|--num-connections]}} {{number}} {{url}}`

- Usa un numero specifico di mirror per la ricerca e il download:

`axel {{[-S|--search=]}}{{number}} {{url}}`

- Limita la velocità di download (byte al secondo):

`axel {{[-s|--max-speed]}} {{speed}} {{url}}`

- Usa solo il protocollo IPv4 quando si connette all'host:

`axel {{[-4|--ipv4]}} {{url}}`

- Limita l'output a `stdout` e usa un user-agent personalizzato durante il download:

`axel {{[-q|--quiet]}} {{[-U|--user-agent]}} {{"Mozilla/5.0"}} {{url}}`
