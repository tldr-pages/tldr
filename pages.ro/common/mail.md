# mail

> Comanda funcționează pe cutia poștală a utilizatorului dacă nu este dat niciun argument.
> Pentru a trimite un e-mail, corpul mesajului este construit din intrarea standard.

- Trimite un mesaj e-mail de la tastatura. Linia de comandă de mai jos continuă după apăsarea tastei Enter. Textul mesajului se poate întinde pe mai multe linii. Apăsați tasta Ctrl-D pentru a finaliza textul mesajului:

`mail --subject="{{subject line}}" {{to_user@example.com}}`

- Trimiteți un e-mail care conține conținut de fișier:

`mail --subject="{{$HOSTNAME filename.txt}}" {{to_user@example.com}} < {{path/to/filename.txt}}`

- Trimiteți un fișier `tar.gz” ca atașament:

`tar cvzf - {{path/to/directory1 path/to/directory2}} | uuencode {{data.tar.gz}} | mail --subject="{{subject_line}}" {{to_user@example.com}}`
