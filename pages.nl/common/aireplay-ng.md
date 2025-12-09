# aireplay-ng

> Injecteer pakketten in een draadloos netwerk.
> Deel van `aircrack-ng`.
> Meer informatie: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Stuur een specifiek aantal losgekoppelde pakketten op basis van het MAC-adres van een toegangspunt, het MAC-adres van een cliënt en een interface:

`sudo aireplay-ng --deauth {{nummer}} --bssid {{ap_mac}} --dmac {{cliënt_mac}} {{interface}}`
