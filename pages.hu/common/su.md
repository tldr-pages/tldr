# su

> Shell váltás egy másik felhasználóra. További információ: <https://manned.org/su>.

- Váltás superuserre (root jelszó szükséges):

`su`

- Egy adott felhasználóra váltás (a felhasználó jelszava szükséges):

`su {{username}}`

- Egy adott felhasználóra váltás és egy teljes bejelentkezési héj szimulálása:

`su - {{username}}`

- Parancs végrehajtása egy másik felhasználóként:

`su - {{username}} -c "{{command}}"`
