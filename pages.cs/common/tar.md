# tar

> Archivovací nástroj.
> Často kombinován s komprimovací metodou, například `gzip` nebo `bzip2`.
> Více informací: <https://www.gnu.org/software/tar/manual/tar.html>.

- Vytvořit archiv a zapsat jej do souboru:

`tar cf {{cesta/k/cili.tar}} {{cesta/k/souboru1 cesta/k/souboru2 ...}}`

- Vytvořit gzip archiv a zapsat jej do souboru:

`tar czf {{cesta/k/cili.tar.gz}} {{cesta/k/souboru1 cesta/k/souboru2 ...}}`

- Vytvořit gzip (komprimovaný) archiv z adresáře pomocí relativních cest:

`tar czf {{cesta/k/cili.tar.gz}} {{[-C|--directory]}} {{cesta/k/adresari}} .`

- E[x]trahovat (komprimovaný) archiv do aktuálního adresáře [v]erbózně:

`tar xvf {{cesta/ke/zdroji.tar[.gz|.bz2|.xz]}}`

- E[x]trahovat (komprimovaný) archiv do cílového adresáře:

`tar xf {{cesta/ke/zdroji.tar[.gz|.bz2|.xz]}} {{[-C|--directory]}} {{cesta/k/adresari}}`

- Vytvořit komprimovaý archiv, zapsat jej do souboru a [a]utomaticky určit program pro kompresi pomocí přípony souboru:

`tar caf {{cesta/k/cili.tar.xz}} {{cesta/k/souboru1 cesta/k/souboru2 ...}}`

- Vypsa[t] obsah souboru tar [v]erbózně:

`tar tvf {{cesta/ke/zdroji.tar}}`

- E[x]trahovat soubory, které se shodují se vzorem z archivu:

`tar xf {{cesta/k/source.tar}} --wildcards "{{*.html}}"`
