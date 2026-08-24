# cat

> Afișează și concatenează fișiere.
> Mai multe informații: <https://manned.org/cat.1posix>.

- Afișează conținutul unui fișier la `stdout`:

`cat {{cale/către/fișier}}`

- Concatenează mai multe fișiere într-un fișier de ieșire:

`cat {{cale/către/fișier1 cale/către/fișier2 ...}} > {{cale/către/fișier_de_ieșire}}`

- Adaugă mai multe fișiere la un fișier de ieșire:

`cat {{cale/către/fișier1 cale/către/fișier2 ...}} >> {{cale/către/fișier_de_ieșire}}`

- Copiază conținutul unui fișier într-un fișier de ieșire fără memorie tampon:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Scrie `stdin` într-un fișier:

`cat - > {{cale/către/fișier}}`
