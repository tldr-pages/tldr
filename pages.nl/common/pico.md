# pico

> Teksteditor gestyled naar de Alpine Composer.
> Meer informatie: <https://manned.org/pico>.

- Start de editor:

`pico {{pad/naar/bestand}}`

- Start de editor met de cursor n regels in het bestand:

`pico +{{n}} {{pad/naar/bestand}}`

- Start de editor met de cursor getoond vóór de huidige selectie:

`pico -g {{pad/naar/bestand}}`

- Definieer de aanhalingsstring voor bestanden zoals e-mail:

`pico -Q "{{aanhalingsstring}}" {{pad/naar/bestand}}`

- Schakel muisfunctionaliteit in wanneer uitgevoerd binnen een `xterm`-venster:

`pico -m {{pad/naar/bestand}}`

- Stel de werkmap in voor `pico`:

`pico -o {{pad/naar/map}}`

- Schakel de modus "alleen bekijken" in, waarmee bewerkingen niet zijn toegestaan:

`pico -v {{pad/naar/bestand}}`

- Toon alle bestanden, inclusief die beginnend met een punt:

`pico -a`
