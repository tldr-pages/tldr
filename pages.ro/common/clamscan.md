# clamscan

> Un scaner de viruși de linie de comandă.
> Mai multe informaţii: <https://www.clamav.net>

- Scanarea unui fișier pentru vulnerabilități:

`clamscan {{path/to/file}}`

- Scanați toate fișierele recursiv într-un anumit director:

`clamscan -r {{path/to/directory}}`

- Scanarea datelor din stdin:

`{{command}} | clamscan -`

- Specificați un fișier de bază de date virus sau un director de fișiere:

`clamscan --database {{path/to/database_file_or_directory}}`

- Scanați directorul curent și ieșiți numai fișierele infectate:

`clamscan --infected`

- Ieșiți raportul de scanare într-un fișier jurnal:

`clamscan --log {{path/to/log_file}}`

- Mutați fișierele infectate într-un anumit director:

`clamscan --move {{path/to/quarantine_directory}}`

- Elimină fișierele infectate:

`clamscan --remove yes`
