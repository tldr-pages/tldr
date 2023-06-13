# smbclient

> Programma client simile ad FTP per server SMB/CIFS.
> Maggiori informazioni: <https://manned.org/man.it/smbclient.1>.

- Connettiti ad una share (all'utente verrà richiesta la password; `exit` per uscire dalla sessione):

`smbclient {{//server/share}}`

- Connettiti con un altro nome utente:

`smbclient {{//server/share}} --user {{username}}`

- Connettersi con un altro gruppo di lavoro:

`smbclient {{//server/condivisione}} --workgroup {{dominio}} --user {{username}}`

- Connettersi con un nome utente ed una password:

`smbclient {{//server/condivisione}} --user {{username%password}}`

- Scaricare un file dal server:

`smbclient {{//server/condivisione}} --directory {{percorso/della/directory}} --command "get {{file.txt}}"`

- Carica un file sul server:

`smbclient {{//server/condivisione}} --directory {{percorso/della/directory}} --command "put {{file.txt}}"`

- Elencare le azioni di un server in modo anonimo:

`smbclient --list={{server}} --no-pass`
