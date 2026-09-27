# mkdir

> Vytváří adresáře a nastavuje jejich oprávnění.
> Více informací: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Vytvořit konkrétní adresáře:

`mkdir {{cesta/k/adresari1 cesta/k/adresari2 ...}}`

- Vytvořit konkrétní adresáře a jejich nadřazené adresáře pokud je potřeba:

`mkdir {{[-p|--parents]}} {{cesta/k/adresari1 cesta/k/adresari2 ...}}`

- Vytvořit adresáře s konkrétním oprávněním:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{cesta/k/adresari1 cesta/k/adresari2 ...}}`

- Vytvořit několik vnořených adresářu rekurzivně:

`mkdir {{[-p|--parents]}} {{cesta/k/{a,b}/{x,y,z}/{h,i,j}}}`
