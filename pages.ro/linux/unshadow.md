# unshadow

> Utilitate furnizată de proiectul John Spintecătorul pentru a obține fișierul tradițional de parolă Unix dacă sistemul utilizează parole din umbră.
> Mai multe informaţii: <https://www.openwall.com/john/>

- Combinați `/etc/shadow` și `/etc/passwd` sistemului curent:

`sudo unshadow /etc/passwd /etc/shadow`

- Combinați două fișiere de umbră și parolă arbitrare:

`sudo unshadow {{path/to/passwd}} {{path/to/shadow}}`
