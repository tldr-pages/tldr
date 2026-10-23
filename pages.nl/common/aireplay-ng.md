# aireplay-ng

> Injecteer pakketten in een draadloos netwerk.
> Onderdeel van Aircrack-ng netwerksoftwaresuite.
> Meer informatie: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Stuur een specifiek aantal disassociatiepakketten op basis van het MAC-adres van een toegangspunt, het MAC-adres van een client en een interface:

`sudo aireplay-ng --deauth {{aantal}} --bssid {{ap_mac}} --dmac {{client_mac}} {{interface}}`
