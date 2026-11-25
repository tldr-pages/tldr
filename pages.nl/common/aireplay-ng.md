# aireplay-ng

> Injecteer pakketten in een draadloos netwerk.
> Onderdeel van Aircrack-ng netwerksoftwaresuite.
> Meer informatie: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Stuur een specifiek aantal disassociatiepakketten op basis van het MAC-adres van een toegangspunt, het MAC-adres van een client en een interface:

`sudo aireplay-ng {{[-0|--deauth]}} {{aantal}} -a {{ap_mac}} -c {{client_mac}} {{interface}}`
