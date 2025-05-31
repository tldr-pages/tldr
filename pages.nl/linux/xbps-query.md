# xbps-query

> XBPS hulpprogramma om te zoeken naar een pakket en repository informatie.
> Bekijk ook: `xbps`.
> Meer informatie: <https://manned.org/xbps-query.1>.

- Zoek naar een pakket in externe repositories met behulp van een reguliere expressie of een trefwoord (als `--regex` wordt weggelaten):

`xbps-query {{[-s|--search]}} {{reguliere_expressie|trefwoord}} --repository --regex`

- Toon informatie over een geïnstalleerd pakket:

`xbps-query {{[-S|--show]}} {{pakket}}`

- Toon informatie over een pakket in externe repositories:

`xbps-query {{[-S|--show]}} {{pakket}} --repository`

- Toon alle geregistreerde pakketen in de pakket database:

`xbps-query {{[-l|--list-pkgs]}}`

- Toon expliciet geïnstalleerde pakketen (bijv. niet automatisch geïnstalleerd als afhankelijkheden):

`xbps-query {{[-m|--list-manual-pkgs]}}`
