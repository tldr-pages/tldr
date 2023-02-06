# tlmgr key

> A TeX Live adatbázisok ellenőrzéséhez használt GPG kulcsok kezelése. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- A TeX Live összes kulcsának listázása:

`tlmgr key list`

- Kulcs hozzáadása egy adott fájlból:

`sudo tlmgr key add {{path/to/key.gpg}}`

- Kulcs hozzáadása a `stdin`:

`cat {{path/to/key.gpg}} | sudo tlmgr key add -`

- Egy adott kulcs eltávolítása az azonosítója alapján:

`sudo tlmgr key remove {{key_id}}`
