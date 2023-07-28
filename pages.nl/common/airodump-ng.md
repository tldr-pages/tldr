# airodump-ng

> Leg pakketten vast en geef informatie over draadloze netwerken weer.
> Deel van `aircrack-ng`.
> Meer informatie: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Leg pakketten vast en geef informatie weer over een draadloos netwerk:

`sudo airodump-ng {{interface}}`

- Leg pakketten vast en geef informatie weer over een draadloos netwerk met het MAC-adres en kanaal, en sla de uitvoer op in een bestand:

`sudo airodump-ng --channel {{kanaal}} --write {{pad/naar/bestand}} --bssid {{mac}} {{interface}}`
