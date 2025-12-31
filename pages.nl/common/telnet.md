# telnet

> Maak verbinding met een opgegeven poort van een host met behulp van het telnet-protocol.
> Meer informatie: <https://manned.org/telnet>.

- Telnet naar de standaardpoort van een host:

`telnet {{host}}`

- Telnet naar een specifieke poort van een host:

`telnet {{ip_adres}} {{poort}}`

- Beëindig een telnet-sessie:

`quit`

- Verstuur de standaard escape-tekencombinatie om de sessie te beëindigen:

`<Ctrl ]>`

- Start `telnet` met "x" als het sessie beëindigingsteken:

`telnet {{[-e|--escape]}} {{x}} {{ip_adres}} {{poort}}`

- Telnet naar de Star Wars-animatie:

`telnet {{towel.blinkenlights.nl}}`
