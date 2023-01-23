# rdpsign

> A Remote Desktop Protocol (RDP) fájlok aláírására szolgáló eszköz. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/rdpsign>.

- RDP-fájl aláírása:

`rdpsign {{path/to/file.rdp}}`

- RDP-fájl aláírása egy adott sha256 hash használatával:

`rdpsign {{path/to/file.rdp}} /sha265 {{hash}}`

- Csendes kimenet engedélyezése:

`rdpsign {{path/to/file.rdp}} /q`

- Szöveges figyelmeztetések, üzenetek és állapotok megjelenítése:

`rdpsign {{path/to/file.rdp}} /v`

- Az aláírás tesztelése a kimenet megjelenítésével a `stdout` címen a fájl frissítése nélkül:

`rdpsign {{path/to/file.rdp}} /l`
