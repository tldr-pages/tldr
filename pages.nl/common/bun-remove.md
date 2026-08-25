# bun remove

> Verwijder een afhankelijkheid uit `package.json`.
> Meer informatie: <https://bun.com/docs/pm/cli/remove>.

- Verwijder een afhankelijkheid:

`bun {{[rm|remove]}} {{pakket_naam}}`

- Verwijder meerdere afhankelijkheden:

`bun {{[rm|remove]}} {{pakket_naam1 pakket_naam2 ...}}`

- Verwijder een globaal geïnstalleerd pakket:

`bun {{[rm|remove]}} {{[-g|--global]}} {{pakket_naam}}`

- Verwijder een afhankelijkheid zonder het `package.json` bestand bij te werken:

`bun {{[rm|remove]}} --no-save {{pakket_naam}}`

- Voer de opdracht uit zonder daadwerkelijk pakketten te verwijderen (simuleer de verwijdering):

`bun {{[rm|remove]}} --dry-run {{pakket_naam}}`
