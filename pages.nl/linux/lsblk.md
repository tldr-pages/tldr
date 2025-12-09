# lsblk

> Toon informatie over apparaten.
> Meer informatie: <https://manned.org/lsblk>.

- Toon alle opslagapparaten in een boomstructuur:

`lsblk`

- Toon ook lege apparaten:

`lsblk {{[-a|--all]}}`

- Toon de SIZE-kolom in bytes in plaats van in een leesbaar formaat:

`lsblk {{[-b|--bytes]}}`

- Toon informatie over bestandssystemen:

`lsblk {{[-f|--fs]}}`

- Gebruik ASCII-tekens voor de boomstructuur:

`lsblk {{[-i|--ascii]}}`

- Toon informatie over de topologie van blokapparaten:

`lsblk {{[-t|--topology]}}`

- Sluit de apparaten uit die zijn opgegeven met een door komma's gescheiden lijst met hoofdapparaatnummers:

`lsblk {{[-e|--exclude]}} {{1,7,...}}`

- Toon een aangepaste samenvatting gebruikmakend van een door komma's gescheiden lijst met kolommen:

`lsblk {{[-o|--output]}} {{NAME,SERIAL,MODEL,TRAN,TYPE,SIZE,FSTYPE,MOUNTPOINT,...}}`
