# htpasswd

> Creați și gestionați fișiere htpasswd pentru a proteja directoarele serverului web utilizând autentificarea de bază.
> Mai multe informaţii: <https://httpd.apache.org/docs/current/programs/htpasswd.html>

- Creează/suprascrie fișierul htpasswd:

`htpasswd -c {{path/to/file}} {{username}}`

- Adăugați utilizator la fișierul htpasswd sau actualizați utilizatorul existent:

`htpasswd {{path/to/file}} {{username}}`

- Adăugați utilizator la fișierul htpasswd în modul batch fără o solicitare de parolă interactivă (pentru utilizarea scriptului):

`htpasswd -b {{path/to/file}} {{username}} {{password}}`

- Ștergeți utilizatorul din fișierul htpasswd:

`htpasswd -D {{path/to/file}} {{username}}`

- Verifică parola de utilizator:

`htpasswd -v {{path/to/file}} {{username}}`

- Afișează un șir cu nume de utilizator (text simplu) și parolă (md5):

`htpasswd -nbm {{username}} {{password}}`
