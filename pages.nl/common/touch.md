# touch

> Maak bestanden aan en stel toegang-/wijzigingstijden in.
> Meer informatie: <https://manned.org/man/freebsd-13.1/touch>.

- Maak specifieke bestanden aan:

`touch {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Stel de toeg[a]ng- of wijzigingstijden ([m]) van een bestand in op de huidige tijd en maak ([c]) geen bestand aan als deze niet bestaat:

`touch -c -{{a|m}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Stel de [t]ijd van een bestand in op een specifieke waarde en maak ([c]) geen bestand aan als deze niet bestaat:

`touch -c -t {{YYYYMMDDHHMM.SS}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Stel de timestamp van de bestanden in op die van het [r]eferentiebestand en maak ([c]) geen bestand aan als deze niet bestaat:

`touch -c -r {{pad/naar/referentiebestand}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`
