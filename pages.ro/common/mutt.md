# mutt

> Client de e-mail în linia de comandă.
> Mai multe informaţii: <http://mutt.org>

- Deschideți cutia poștală specificată:

`mutt -f {{mailbox}}`

- Trimiteți un e-mail și specificați un subiect și un destinatar cc:

`mutt -s {{subject}} -c {{cc@example.com}} {{recipient@example.com}}`

- Trimiteți un e-mail cu fișiere atașate:

`mutt -a {{file1}} {{file2}} -- {{recipient@example.com}}`

- Specificați un fișier pentru a include ca corp de mesaj:

`mutt -i {{file}} {{recipient@example.com}}`

- Specificați un fișier schiță care conține antetul și corpul mesajului, în format RFC 5322:

`mutt -H {{file}} {{recipient@example.com}}`
