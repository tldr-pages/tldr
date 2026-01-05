# certutil

> Gestisce chiavi e certificati sia nei database NSS che in altri token NSS.
> Maggiori informazioni: <https://manned.org/certutil>.

- Crea un [N]uovo database di certificati nella [d]irectory corrente:

`certutil -N -d .`

- [L]ista tutti i certificati presenti in un database:

`certutil -L -d .`

- Elenca tutte le [K]ey private in un database specificando il [f]ile della password:

`certutil -K -d . -f {{percorso/del/file_password.txt}}`

- [A]ggiunge il certificato firmato al database del richiedente specificando un [n]ickname, gli attributi di [t]rust e un [i]nput file CRT:

`certutil -A -n "{{certificato_server}}" -t ",," -i {{percorso/del/file.crt}} -d .`

- Aggiunge nomi alternativi del soggetto a un dato [c]ertificate con una specifica dimensione della chiave ([g]):

`certutil -S -f {{percorso/del/file_password.txt}} -d . -t ",," -c "{{certificato_server}}" -n "{{nome_server}}" -g {{2048}} -s "CN={{common_name}},O={{organization}}"`
