# axel

> Downloader accelerato.
> Supporta HTTP, HTTPS e FTP.
> Maggiori informazioni: <https://github.com/axel-download-accelerator/axel>.

- Scarica un file da un URL:

`axel {{url}}`

- Scarica specificando il nome del file da creare:

`axel {{url}} -o {{filename}}`

- Scarica sfruttando connessioni multiple:

`axel -n {{numero_connessioni}} {{url}}`

- Cerca dei mirror:

`axel -S {{numero_mirror}} {{url}}`

- Limita la velocità di download (in bytes al secondo):

`axel -s {{limite_velocità}} {{url}}`
