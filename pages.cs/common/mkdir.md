# mkdir

> Vytváří adresáře a nastavuje jejich oprávnění.
> Více informací: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Vytvořit konkrétní adresáře:

`mkdir {{cesta/k/adresari1 cesta/k/adresari2 ...}}`

- Vytvořit konkrétní adresáře a jejich nadřazené adresáře pokud je potřeba:

`mkdir {{[-p|--parents]}} {{cesta/k/adresari1 cesta/k/adresari2 ...}}`

- Vytvořit adresáře s konkrétním oprávněním:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{cests/k/adresari1 cesta/k/adresari2 ...}}`
