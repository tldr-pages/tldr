# uniq

> Geef de unieke regels uit een invoer of bestand weer.
> Omdat het geen herhaalde regels detecteert tenzij ze naast elkaar staan, moeten we ze eerst sorteren.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>.

- Toon elke regel één keer:

`sort {{pad/naar/bestand}} | uniq`

- Toon alleen unieke regels:

`sort {{pad/naar/bestand}} | uniq {{[-u|--unique]}}`

- Toon alleen dubbele regels:

`sort {{pad/naar/bestand}} | uniq {{[-d|--repeated]}}`

- Toon het aantal voorkomens van elke regel samen met die regel:

`sort {{pad/naar/bestand}} | uniq {{[-c|--count]}}`

- Toon het aantal voorkomens van elke regel, gesorteerd op meest frequent:

`sort {{pad/naar/bestand}} | uniq {{[-c|--count]}} | sort {{[-nr|--numeric-sort --reverse]}}`
