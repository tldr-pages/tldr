# kiterunner wordlist

> Een contextuele webscanner voor het beheren van wordlists die gebruikt worden in API en web endpoint discovery.
> Het `wordlist` subcommando zorgt voor het opsommen en opslaan van wordlists in `~/.cache/kiterunner`.
> Meer informatie: <https://github.com/assetnote/kiterunner#usage>.

- Maak een lijst van alle in de cache opgeslagen en beschikbare Assetnote woordenlijsten:

`kiterunner wordlist list`

- Geef woordlijsten met JSON uitvoer weer:

`kiterunner wordlist list {{[-o|--output]}} {{json}}`

- Geef woordlijsten met uitgebreide debug-uitvoer weer:

`kiterunner wordlist list {{[-v|--verbose]}} {{debug}}`

- Sla een specifieke Assetnote woordenlijst op met een alias:

`kiterunner wordlist save {{apiroutes-210328}}`

- Sla een specifieke Assetnote woordenlijst op met de volledige bestandsnaam:

`kiterunner wordlist save {{pad/naar/httparchive_apiroutes_2024_05_28.txt}}`

- Sla meerdere woordenlijsten op met een alias:

`kiterunner wordlist save {{apiroutes-210328,aspx-210328}}`

- Sla een woordenlijst op met stille modus om uitvoer te onderdrukken:

`kiterunner wordlist save {{apiroutes-210328}} {{[-q|--quiet]}}`
