# uniq

> Geef de unieke regels uit een invoer of bestand weer.
> Omdat het geen herhaalde regels detecteert tenzij ze naast elkaar staan, moeten we ze eerst sorteren.
> Zie ook: `sort`.
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

- Vergelijk alleen de eerste 10 tekens van elke regel op uniekheid:

`sort {{pad/naar/bestand}} | uniq {{[-w|--check-chars]}} 10`

- Vergelijk tekst na de eerste 5 tekens van elke regel op uniekheid:

`sort {{pad/naar/bestand}} | uniq {{[-s|--skip-chars]}} 5`
