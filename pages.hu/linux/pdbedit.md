# pdbedit

> A Samba felhasználói adatbázis szerkesztése. Egyszerű felhasználó hozzáadásához/eltávolításához/jelszóhoz használhatja a `smbpasswd` címet is. További információ: <https://manned.org/pdbedit>.

- Listázza ki az összes Samba felhasználót (a verbose flag használatával megjelenítheti a beállításokat):

`sudo pdbedit --list --verbose`

- Egy meglévő Unix-felhasználó hozzáadása a Samba-hoz (jelszót kér):

`sudo pdbedit --user {{username}} --create`

- Samba-felhasználó eltávolítása:

`sudo pdbedit --user {{username}} --delete`

- A Samba-felhasználó sikertelen jelszószámlálójának visszaállítása:

`sudo pdbedit --user {{username}} --bad-password-count-reset`
