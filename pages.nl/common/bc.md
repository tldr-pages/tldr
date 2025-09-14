# bc

> Een rekenmachinetaal met willekeurige precisie.
> Zie ook: `dc`, `qalc`.
> Meer informatie: <https://manned.org/bc>.

- Start een interactieve sessie:

`bc`

- Start een interactieve sessie met de standaard wiskundige bibliotheek ingeschakeld:

`bc {{[-i|--interactive]}} {{[-l|--mathlib]}}`

- Bereken een uitdrukking:

`echo '{{5 / 3}}' | bc`

- Voer een script uit:

`bc {{pad/naar/script.bc}}`

- Bereken een uitdrukking met de gespecificeerde schaal:

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- Bereken een sinus/cosinus/arctangens/natuurlijke logaritme/exponentiële functie met behulp van `mathlib`:

`echo '{{s|c|a|l|e}}({{1}})' | bc {{[-l|--mathlib]}}`

- Voer een inline faculteitsscript uit:

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial({{10}})" | bc`
