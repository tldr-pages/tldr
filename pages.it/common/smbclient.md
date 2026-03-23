# smbclient

> Programma client simile ad FTP per server SMB/CIFS.
> Maggiori informazioni: <https://manned.org/smbclient>.

- Connettiti ad una share (all'utente verrà richiesta la password; `exit` per uscire dalla sessione):

`smbclient {{//server/share}}`

- Connettiti con un altro nome utente:

`smbclient {{//server/share}} {{[-U|--user]}} {{username}}`

- Connettiti con un altro gruppo di lavoro:

`smbclient {{//server/share}} {{[-W|--workgroup]}} {{dominio}} {{[-U|--user]}} {{username}}`

- Connettiti con un nome utente ed una password:

`smbclient {{//server/share}} {{[-U|--user]}} {{username%password}}`

- Scarica un file dal server:

`smbclient {{//server/share}} {{[-D|--directory]}} {{percorso/della/directory}} {{[-c|--command]}} "get {{file.txt}}"`

- Carica un file sul server:

`smbclient {{//server/share}} {{[-D|--directory]}} {{percorso/della/directory}} {{[-c|--command]}} "put {{file.txt}}"`

- Elenca le share di un server in modo anonimo:

`smbclient {{[-L|--list]}} {{server}} --no-pass`
