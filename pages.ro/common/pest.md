# pest

> Un cadru de testare PHP cu accent pe simplitate.
> Mai multe informaţii: <https://pestphp.com>

- Inițializarea unei configurații standard a Pest în directorul curent:

`pest --init`

- Rulați teste în directorul curent:

`pest`

- Executați teste adnotate cu grupul dat:

`pest --group {{name}}`

- Rulați teste și imprimați raportul de acoperire la stdout:

`pest --coverage`

- Rulați teste cu acoperire și nu reușesc dacă acoperirea este mai mică decât procentul minim:

`pest --coverage --min={{80}}`
