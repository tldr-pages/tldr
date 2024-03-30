# sed

> Pas tekst aan in een op een scriptbare manier.
> Bekijk ook: `awk`, `ed`.
> Meer informatie: <https://manned.org/man/sed.1posix>.

- Vervang alle `apple` (basis regex) met `mango` (basis regex) in alle invoerregels en toon het resultaat in `stdout`:

`{{commando}} | sed 's/apple/mango/g'`

- Voer een specifiek script bestand uit en toon het resultaat in `stdout`:

`{{commando}} | sed -f {{pad/naar/script.sed}}`

- Toon alleen de eerste regel in `stdout`:

`{{commando}} | sed -n '1p'`
