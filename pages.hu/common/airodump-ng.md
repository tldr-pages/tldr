# airodump-ng

> Csomagok rögzítése és a vezeték nélküli hálózatokról szóló információk megjelenítése. A `aircrack-ng` weboldal része. További információ: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Csomagok rögzítése és információk megjelenítése vezeték nélküli hálózatról:

`sudo airodump-ng {{interface}}`

- Csomagok rögzítése és információk megjelenítése egy vezeték nélküli hálózatról a MAC-cím és a csatorna megadásával, valamint a kimenet mentése egy fájlba:

`sudo airodump-ng --channel {{channel}} --write {{path/to/file}} --bssid {{mac}} {{interface}}`
