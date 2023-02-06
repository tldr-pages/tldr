# adduser

> Felhasználói kiegészítő segédprogram. További információ: <https://manpages.debian.org/latest/adduser/adduser.html>.

- Hozzon létre egy új felhasználót egy alapértelmezett kezdőkönyvtárral, és kérje a felhasználót jelszó megadására:

`adduser {{username}}`

- Új felhasználó létrehozása otthoni könyvtár nélkül:

`adduser --no-create-home {{username}}`

- Új felhasználó létrehozása a megadott elérési útvonalon lévő otthoni könyvtárral:

`adduser --home {{path/to/home}} {{username}}`

- Új felhasználó létrehozása a megadott héjjal, amely a bejelentkezési héjként van beállítva:

`adduser --shell {{path/to/shell}} {{username}}`

- Új felhasználó létrehozása a megadott csoporthoz tartozóként:

`adduser --ingroup {{group}} {{username}}`
