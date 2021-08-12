# smbclient

> FTP ca client pentru a accesa resursele SMB/CIFS pe servere.

- Conectează-te la o partajare (utilizatorului i se va solicita parola; `exit` pentru a iesi din sesiune):

`smbclient {{//server/share}}`

- Conectați-vă cu un nume de utilizator diferit:

`smbclient {{//server/share}} --user {{username}}`

- Conectați-vă cu un grup de lucru diferit:

`smbclient {{//server/share}} --workgroup {{domain}} --user {{username}}`

- Conectați-vă cu un nume de utilizator și o parolă:

`smbclient {{//server/share}} --user {{username%password}}`

- Descărcați un fișier de pe server:

`smbclient {{//server/share}} --directory {{path/to/directory}} --command "get {{file.txt}}"`

- Încărcați un fișier pe server:

`smbclient {{//server/share}} --directory {{path/to/directory}} --command "put {{file.txt}}"`
