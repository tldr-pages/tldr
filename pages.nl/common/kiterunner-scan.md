# kiterunner scan

> Een contextuele web scanner om gelijktijdig API paden en web eindpunten te scannen met behulp van kitebuilder woordenlijsten.
> Het `scan` subcommando richt zich op een of meerdere hosts met gestructureerde API verzoeken.
> Meer informatie: <https://github.com/assetnote/kiterunner#usage>.

- Scan een doel met een Assetnote woordenlijst (bijvoorbeeld de eerste 5000 API-routes):

`kiterunner scan {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210228:5000}}`

- Scan een doel met een kitebuilder woordenlijst:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{pad/naar/woordenlijst.kite}}`

- Meerdere hosts scannen vanuit een bestand met een kitebuilder wordlist:

`kiterunner scan {{pad/naar/hosts.txt}} {{[-w|--kitebuilder-list]}} {{pad/naar/woordenlijst.kite}}`

- Scannen met een Assetnote woordenlijst en JSON uitvoer:

`kiterunner scan {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210228:5000}} -o {{json}}`

- Scan met aangepaste concurrency-instellingen voor prestaties:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{pad/naar/woordenlijst.kite}} {{[-x|--max-connection-per-host]}} {{5}} {{[-j|--max-parallel-hosts]}} {{100}}`

- Scannen met een woordenlijst als een normale woordenlijst, waarbij het scannen op diepte wordt uitgeschakeld:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{pad/naar/rafter.txt}} {{[-d|--preflight-depth]}} {{0}}`

- Scan met aangepaste headers en negeer antwoorden met specifieke inhoudslengte:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{pad/naar/woordenlijst.kite}} {{[-H|--header]}} "{{Authorization: Bearer token}}" --ignore-length {{100-105}}`

- Voer een volledige kitebuilder scan uit zonder fase scanning:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{pad/naar/woordenlijst.kite}} --kitebuilder-full-scan`
