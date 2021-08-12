# tmpmail

> Un e-mail temporar direct de la terminalul scris în POSIX sh.
> Mai multe informaţii: <https://github.com/sdushantha/tmpmail>

- Creați un inbox temporar:

`tmpmail --generate`

- Lista mesajelor și ID-ul lor numeric:

`tmpmail`

- Afișează cel mai recent e-mail primit:

`tmpmail --recent`

- Deschide un mesaj specific:

`tmpmail {{email_id}}`

- Vizualizați e-mailul ca text brut fără tag-uri HTML:

`tmpmail --text`

- Deschideți e-mailul cu un anumit browser (implicit este w3m):

`tmpmail --browser {{browser}}`
