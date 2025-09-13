# rm

> Verwijder bestanden of mappen.
> Zie ook: `rmdir`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Verwijder specifieke bestanden:

`rm {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Verwijder specifieke bestanden, maar negeer niet-bestaande bestanden:

`rm {{[-f|--force]}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Verwijder specifieke bestanden [i]nteractief door vóór elke verwijdering bevestiging te vragen:

`rm {{[-i|--interactive]}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Verwijder specifieke bestanden en toon informatie over iedere verwijdering:

`rm {{[-v|--verbose]}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Verwijder specifieke bestanden en mappen [r]ecursief:

`rm {{[-r|--recursive]}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Verwijder lege mappen (dit word beschouwd als de veilige methode):

`rm {{[-d|--dir]}} {{pad/naar/map}}`
