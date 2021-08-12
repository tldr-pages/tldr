# mimetype

> Determinați automat tipul MIME al unui fișier.

- Tipăriți tipul MIME al unui fișier dat:

`mimetype {{path/to/file}}`

- Afișează numai tipul MIME, și nu numele fișierului:

`mimetype --brief {{path/to/file}}`

- Afișează o descriere a tipului MIME:

`mimetype --describe {{path/to/file}}`

- Determinați tipul MIME de stdin (nu verifică un nume de fișier):

`{{some_command}} | mimetype --stdin`

- Afișează informații de depanare despre modul în care a fost determinat tipul MIME:

`mimetype --debug {{path/to/file}}`

- Afișează toate tipurile posibile MIME ale unui fișier dat în ordine de încredere:

`mimetype --all {{path/to/file}}`

- Specificați în mod explicit codul de limbă de 2 litere al ieșirii:

`mimetype --language {{path/to/file}}`
