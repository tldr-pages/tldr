# updog

> A Python SimpleHTTPServer helyettesítője. Lehetővé teszi a HTTP/S-en keresztüli feltöltést és letöltést, ad hoc SSL tanúsítványokat tud beállítani és HTTP basic auth-t használ. További információ: <https://github.com/sc0tfree/updog>.

- HTTP-kiszolgáló indítása az aktuális könyvtárhoz:

`updog`

- HTTP-kiszolgáló indítása egy megadott könyvtárhoz:

`updog --directory {{/path/to/directory}}`

- HTTP-kiszolgáló indítása egy megadott porton:

`updog --port {{port}}`

- HTTP-kiszolgáló indítása jelszóval (A bejelentkezéshez hagyja üresen a felhasználónevet, és adja meg a jelszót a jelszó mezőbe):

`updog --password {{password}}`

- A szállítás titkosításának engedélyezése SSL-en keresztül:

`updog --ssl`
