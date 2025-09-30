# ftp

> Interactief bestanden overzetten tussen een lokale en een externe FTP-server.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Verbind interactief met een externe FTP-server:

`ftp {{host}}`

- Log in als een anonieme gebruiker:

`ftp -A {{host}}`

- Schakel automatisch inloggen uit bij de eerste verbinding:

`ftp -n {{host}}`

- Voer een bestand uit met een lijst van FTP-opdrachten:

`ftp -s:{{pad\naar\bestand}} {{host}}`

- Download meerdere bestanden (glob-expressie):

`mget {{*.png}}`

- Upload meerdere bestanden (glob-expressie):

`mput {{*.zip}}`

- Verwijder meerdere bestanden op de externe server:

`mdelete {{*.txt}}`

- Toon de help:

`ftp --help`
