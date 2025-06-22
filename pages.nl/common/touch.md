# touch

> Maak bestanden aan en stel toegang-/wijzigingstijden in.
> Meer informatie: <https://manned.org/touch>.

- Maak specifieke bestanden aan:

`touch {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Stel de toeg[a]ng- of wijzigingstijden ([m]) van een bestand in op de huidige tijd en maak ([c]) geen bestand aan als deze niet bestaat:

`touch {{[-c|--no-create]}} -{{a|m}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Stel de [t]ijd van een bestand in op een specifieke waarde en maak ([c]) geen bestand aan als deze niet bestaat:

`touch {{[-c|--no-create]}} -t {{YYYYMMDDHHMM.SS}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Stel de timestamp van de bestanden in op die van het [r]eferentiebestand en maak ([c]) geen bestand aan als deze niet bestaat:

`touch {{[-c|--no-create]}} {{[-r|--reference]}} {{pad/naar/referentiebestand}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Stel de timestamp in door een string te parsen:

`touch {{[-d|--date]}} "{{last year|5 hours|next thursday|nov 14|...}}" {{pad/naar/bestand}}`
