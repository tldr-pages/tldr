# watch

> Voer een programma periodiek uit en bekijk de uitvoer in volledig schermmodus.
> Meer informatie: <https://manned.org/watch>.

- Voer een commando herhaaldelijk uit en toon het resultaat:

`watch {{commando}}`

- Voer een commando elke 60 seconden opnieuw uit:

`watch {{[-n|--interval]}} 60 {{commando}}`

- Controleer de schijfruimte en markeer deze verschillen zodra ze zich voordoen:

`watch {{[-d|--differences]}} df`

- Voer een pipeline herhaaldelijk uit en toon het resultaat:

`watch "{{commando1}} | {{commando2}} | {{commando3}}"`

- Sluit `watch` af als de zichtbare uitvoer verandert:

`watch {{[-g|--chgexit]}} {{lsblk}}`

- Interpreteer terminal besturingstekens:

`watch {{[-c|--color]}} {{ls --color=always}}`
