# smbclient

> Programma client simile ad FTP per server SMB/CIFS.
> Maggiori informazioni: <https://manned.org/man.it/smbclient.1>.

- Connettiti ad una share (all'utente verrà richiesta la password; `exit` per uscire dalla sessione):

`smbclient {{//server/share}}`

- Connettiti con un altro nome utente:

`smbclient {{//server/share}} --user {{username}}`

- Connettiti con un altro gruppo di lavoro:

`smbclient {{//server/share}} --workgroup {{dominio}} --user {{username}}`

- Connettiti con un nome utente ed una password:

`smbclient {{//server/share}} --user {{username%password}}`

- Scarica un file dal server:

`smbclient {{//server/share}} --directory {{percorso/della/directory}} --command "get {{file.txt}}"`

- Carica un file sul server:

`smbclient {{//server/share}} --directory {{percorso/della/directory}} --command "put {{file.txt}}"`

- Elenca le share di un server in modo anonimo:

`smbclient --list={{server}} --no-pass`
