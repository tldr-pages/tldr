# bun install

> Installeer JavaScript afhankelijkheden voor een project vanuit `package.json`.
> Meer informatie: <https://bun.com/docs/pm/cli/install>.

- Installeer alle afhankelijkheden vermeld in `package.json`:

`bun {{[i|install]}}`

- Installeer een enkel pakket (dit is een alias voor `bun add`):

`bun {{[i|install]}} {{pakket_naam}}@{{versie}}`

- Installeer een pakket globaal:

`bun {{[i|install]}} {{[-g|--global]}} {{pakket_naam}}`

- Installeer alleen productieafhankelijkheden (slaat `devDependencies` over):

`bun {{[i|install]}} --production`

- Installeer afhankelijkheden precies vanuit het `bun.lockb` lockbestand (bevroren lockbestand):

`bun {{[i|install]}} --frozen-lockfile`

- Forceer het opnieuw downloaden van alle pakketten uit het register, waarbij de cache wordt genegeerd:

`bun {{[i|install]}} {{[-f|--force]}}`
