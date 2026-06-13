# bunx

> Voer een binair pakket uit (lokaal geïnstalleerd of op afstand opgehaald).
> Opmerking: `bun x` kan als alias voor `bunx` gebruikt worden.
> Meer informatie: <https://bun.com/docs/pm/bunx>.

- Download een pakket uit het register en voer het uit:

`bunx {{pakket_naam}} "{{commando_argument}}"`

- Controleer de versie van een lokaal geïnstalleerd pakket (indien gevonden):

`bunx {{pakket_naam}} --version`

- Forceer een uitvoerbaar bestand om te draaien met de Bun runtime (in plaats van Node):

`bunx --bun {{pakket_naam}}`

- Voer een binair bestand uit dat een andere naam heeft dan zijn pakket:

`bunx {{[-p|--package]}} {{pakket_naam}} {{commando}}`

- Download een specifieke versie van een pakket en voer het uit:

`bunx {{pakket_naam@versie}} "{{commando_argument}}"`
