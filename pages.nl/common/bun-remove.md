# bun remove

> Verwijder een afhankelijkheid uit `package.json`.
> Opmerking: `rm` kan gebruikt worden als alias voor `remove`.
> Meer informatie: <https://bun.com/docs/pm/cli/remove>.

- Verwijder een afhankelijkheid:

`bun remove {{pakket_naam}}`

- Verwijder meerdere afhankelijkheden:

`bun remove {{pakket_naam1 pakket_naam2 ...}}`

- Verwijder een globaal geïnstalleerd pakket:

`bun remove {{[-g|--global]}} {{pakket_naam}}`

- Verwijder een afhankelijkheid zonder het `package.json` bestand bij te werken:

`bun remove --no-save {{pakket_naam}}`

- Voer de opdracht uit zonder daadwerkelijk pakketten te verwijderen (simuleer de verwijdering):

`bun remove --dry-run {{pakket_naam}}`
