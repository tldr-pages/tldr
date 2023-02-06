# smbpasswd

> Samba-felhasználó hozzáadása/eltávolítása vagy jelszavának módosítása. A Samba-felhasználóknak rendelkezniük kell egy meglévő helyi Unix-fiókkal. További információ: <https://manned.org/smbpasswd.8>.

- Az aktuális felhasználó SMB-jelszavának módosítása:

`smbpasswd`

- Egy megadott felhasználó hozzáadása a Samba-hoz és jelszó beállítása (a felhasználónak már léteznie kell a rendszerben):

`sudo smbpasswd -a {{username}}`

- Egy meglévő Samba-felhasználó jelszavának módosítása:

`sudo smbpasswd {{username}}`

- Samba-felhasználó törlése (a `pdbedit` címet használja helyette, ha a Unix-fiókot törölték):

`sudo smbpasswd -x {{username}}`
