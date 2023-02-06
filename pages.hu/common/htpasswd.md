# htpasswd

> A htpasswd fájlok létrehozása és kezelése a webkiszolgáló könyvtárak védelmére alapvető hitelesítéssel. További információ: <https://httpd.apache.org/docs/current/programs/htpasswd.html>.

- A htpasswd fájl létrehozása/felülírása:

`htpasswd -c {{path/to/file}} {{username}}`

- Felhasználó hozzáadása a htpasswd fájlhoz vagy a meglévő felhasználó frissítése:

`htpasswd {{path/to/file}} {{username}}`

- Felhasználó hozzáadása a htpasswd fájlhoz kötegelt módban, interaktív jelszókérés nélkül (szkript használatához):

`htpasswd -b {{path/to/file}} {{username}} {{password}}`

- Felhasználó törlése a htpasswd fájlból:

`htpasswd -D {{path/to/file}} {{username}}`

- Felhasználó jelszavának ellenőrzése:

`htpasswd -v {{path/to/file}} {{username}}`

- A felhasználónév (egyszerű szöveg) és a jelszó (md5) karakterláncának megjelenítése:

`htpasswd -nbm {{username}} {{password}}`
