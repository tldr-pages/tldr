# aria2c

> Gyors letöltési segédprogram. Támogatja a HTTP(S), FTP, SFTP, SFTP, BitTorrent és Metalink szabványokat. További információ: <https://aria2.github.io>.

- Egy adott URI letöltése egy fájlba:

`aria2c "{{url}}"`

- Letölthet egy fájlt egy adott kimeneti névvel rendelkező URI-ról:

`aria2c --out={{path/to/file}} "{{url}}"`

- Több különböző fájl párhuzamos letöltése:

`aria2c --force-sequential {{false}} "{{url1 url2 ...}}"`

- Letöltés több forrásból úgy, hogy mindegyik URI ugyanarra a fájlra mutat:

`aria2c "{{url1 url2 ...}}"`

- A fájlban felsorolt URI-k letöltése meghatározott számú párhuzamos letöltéssel:

`aria2c --input-file={{path/to/file}} --max-concurrent-downloads={{number_of_downloads}}`

- Letöltés több kapcsolattal:

`aria2c --split={{number_of_connections}} "{{url}}"`

- FTP letöltés felhasználónévvel és jelszóval:

`aria2c --ftp-user={{username}} --ftp-passwd={{password}} "{{url}}"`

- Letöltési sebesség korlátozása bájt/s-ban:

`aria2c --max-download-limit={{speed}} "{{url}}"`
