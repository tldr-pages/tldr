# warp-diag

> Diagnosztikai és visszajelző eszköz a Cloudflare WARP szolgáltatásához. Lásd még: `warp-cli`. További információ: <https://developers.cloudflare.com/warp-client/>.

- Generáljon egy zip-fájlt a rendszer konfigurációjára és a WARP-kapcsolatra vonatkozó információkkal:

`warp-diag`

- Zip-fájl generálása hibakeresési információkkal, beleértve a kimeneti fájlnév időbélyegzőjét:

`warp-diag --add-ts`

- A kimeneti fájl mentése egy adott könyvtárba:

`warp-diag --output {{path/to/directory}}`

- Új visszajelzés elküldése a Cloudflare WARP-nek interaktívan:

`warp-diag feedback`
