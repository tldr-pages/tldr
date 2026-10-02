# iw

> Toon en manipuleer draadloze apparaten.
> Zie ook: `iw dev`, `nmcli`, `iwctl`.
> Meer informatie: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Scan naar beschikbare draadloze netwerken:

`iw dev {{wlanX}} scan`

- Sluit je aan bij een open draadloos netwerk:

`iw dev {{wlanX}} connect {{ssid}}`

- Sluit de huidige verbinding:

`iw dev {{wlanX}} disconnect`

- Toon informatie over de huidige verbinding:

`iw dev {{wlanX}} link`

- Toon alle fysieke en logische draadloze netwerkinterfaces:

`iw dev`

- Toon alle draadloze mogelijkheden van alle fysieke hardware-interfaces:

`iw phy`

- Toon het huidige draadloze regelgevingsdomein van de kernel:

`iw reg get`

- Toon de help:

`iw help`
