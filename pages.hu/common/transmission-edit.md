# transmission-edit

> A torrentfájlok bejelentési URL-jének módosítása. Lásd még: `transmission`. További információ: <https://manned.org/transmission-edit>.

- URL hozzáadása vagy eltávolítása egy torrent bejelentési listájáról:

`transmission-edit --{{add|delete}} {{http://example.com}} {{path/to/file.torrent}}`

- Egy nyomkövető jelszavának frissítése egy torrentfájlban:

`transmission-edit --replace {{old-passcode}} {{new-passcode}} {{path/to/file.torrent}}`
