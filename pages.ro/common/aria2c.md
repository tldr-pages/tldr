# aria2c

> Utilitar de descărcare rapidă.
> Suportă HTTP (S), FTP, SFTP, BitTorrent și Metalink.
> Mai multe informaţii: <https://aria2.github.io>

- Descărcați un URI într-un fișier:

`aria2c {{url}}`

- Descărcați fișierul indicat de URI specificat cu numele de ieșire specificat:

`aria2c --out={{filename}} {{url}}`

- Descărcați mai multe fișiere în paralel:

`aria2c --force-sequential {{url_1}} {{url_2}}`

- Descărcați din mai multe surse fiecare URI care indică spre același fișier:

`aria2c {{url_1}} {{url_2}}`

- Descărcați URI-urile listate într-un fișier cu descărcări paralele limitate:

`aria2c --input-file={{filename}} --max-concurrent-downloads={{number_of_downloads}}`

- Descărcați cu mai multe conexiuni:

`aria2c --split={{number_of_connections}} {{url}}`

- Descărcare FTP cu nume de utilizator și parolă:

`aria2c --ftp-user={{username}} --ftp-passwd={{password}} {{url}}`

- Limitați viteza de descărcare în octeți/s:

`aria2c --max-download-limit={{speed}} {{url}}`
