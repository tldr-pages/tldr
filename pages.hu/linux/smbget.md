# smbget

> `wget`-szerű segédprogram fájlok letöltéséhez SMB-kiszolgálókról. További információ: <https://www.samba.org/samba/docs/current/man-html/smbget.1.html>.

- Fájl letöltése egy kiszolgálóról:

`smbget {{smb://server/share/file}}`

- Megosztás vagy könyvtár rekurzív letöltése:

`smbget --recursive {{smb://server/share}}`

- Csatlakozás felhasználónévvel és jelszóval:

`smbget {{smb://server/share/file}} --user {{username%password}}`

- Titkosított átvitelt igényel:

`smbget {{smb://server/share/file}} --encrypt`
