# bc

> Een rekenmachinetaal met willekeurige precisie.
> Zie ook: `dc`.
> Meer informatie: <https://keith.github.io/xcode-man-pages/bc.1.html>.

- Start een interactieve sessie:

`bc`

- Start een interactieve sessie met de standaard wiskundige bibliotheek ingeschakeld:

`bc --mathlib`

- Bereken een uitdrukking:

`bc --expression '{{5 / 3}}'`

- Voer een script uit:

`bc {{pad/naar/script.bc}}`

- Bereken een uitdrukking met de gespecificeerde schaal:

`bc --expression '{{scale = 10; 5 / 3}}'`

- Bereken een sinus/cosinus/arctangens/natuurlijke logaritme/exponentiële functie met behulp van `mathlib`:

`bc --mathlib --expression '{{s|c|a|l|e}}({{1}})'`
