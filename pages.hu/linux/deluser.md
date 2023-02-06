# deluser

> Felhasználó törlése a rendszerből. További információ: <https://manpages.debian.org/latest/adduser/deluser.html>.

- Felhasználó eltávolítása:

`sudo deluser {{username}}`

- Egy felhasználó és a home könyvtárának eltávolítása:

`sudo deluser --remove-home {{username}}`

- Eltávolít egy felhasználót és az otthoni könyvtárát, de a fájljairól biztonsági másolatot készít egy `.tar.gz` fájlba a megadott könyvtárban:

`sudo deluser --backup-to {{path/to/backup_directory}} --remove-home {{username}}`

- Felhasználó és a tulajdonában lévő összes fájl eltávolítása:

`sudo deluser --remove-all-files {{username}}`
