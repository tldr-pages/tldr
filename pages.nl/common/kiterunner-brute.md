# kiterunner brute

> Een contextuele webscanner voor het bruteforcen van API-paden en web-endpoints met behulp van woordenlijsten.
> Het `brute` subcommando richt zich op een of meerdere hosts.
> Meer informatie: <https://github.com/assetnote/kiterunner#usage>.

- Bruteforce een doel met een Assetnote woordenlijst (bijvoorbeeld de eerste 20.000 API routes):

`kiterunner brute {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210328:20000}}`

- Bruteforce een doelwit met een aangepaste woordenlijst:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{pad/naar/woordenlijst.txt}}`

- Bruteforce met een dirsearch-woordlijst met extensie-substitutie:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{pad/naar/dirsearch.txt}} {{[-D|--dirsearch-compat]}} {{[-e|--extensions]}} {{json,txt}}`

- Bruteforce met specifieke bestandsextensies toegevoegd en uitvoer in JSON-formaat:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{pad/naar/woordenlijst.txt}} {{[-e|--extensions]}} {{aspx,ashx}} {{[-o|--output]}} {{json}}`

- Bruteforce een lijst met doelen uit een bestand met aangepaste concurrency-instellingen voor prestaties:

`kiterunner brute {{pad/naar/targets.txt}} {{[-w|--wordlist]}} {{pad/naar/woordenlijst.txt}} {{[-x|--max-connection-per-host]}} {{5}} {{[-j|--max-parallel-hosts]}} {{100}}`

- Bruteforce en negeer specifieke inhoudslengte antwoorden:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{pad/naar/woordenlijst.txt}} --ignore-length {{100-105}}`

- Bruteforce met aangepaste HTTP-headers:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{pad/naar/woordenlijst.txt}} {{[-H|--header]}} "{{Authorization: Bearer token}}"`

- Bruteforce een lijst van doelen uit een bestand met fail status code filtering:

`kiterunner brute {{pad/naar/doelen.txt}} {{[-w|--wordlist]}} {{pad/naar/woordenlijst.txt}} --fail-status-codes {{400,401,404}}`
