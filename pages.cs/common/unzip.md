# unzip

> Extrahuje soubory/adresáře ze Zipových archivů.
> Viz také: `zip`.
> Více informací: <https://manned.org/unzip>.

- Extrahovat všechny soubory/adresáře ze specifického archivu do aktuálního adresáře:

`unzip {{cesta/k/archivu1.zip cesta/k/archivu2.zip ...}}`

- Extrahovat soubory/adresáře z archivu do konkrétní cesty:

`unzip {{cesta/k/archivu1.zip cesta/k/archivu2.zip ...}} -d {{cesta/k/vystupu}}`

- Extrahovat soubory/adresáře z archivů do `stdout` spolu s názvy souborů:

`unzip -c {{cesta/k/archivu1.zip cesta/k/archivu2.zip ...}}`

- Extrahovat archiv vytvořený na Windows, obsahujicí soubory s názvy souborů mimo ASCII (např. Čínské nebo Japonské znaky):

`unzip -O {{gbk}} {{cesta/k/archivu1.zip cesta/k/archivu2.zip ...}}`

- Vypsat obsah konkrétního archivu bez extrahování:

`unzip -l {{cesta/k/archivu.zip}}`

- Extrahovat konkrétní soubor z archivu:

`unzip -j {{cesta/k/archivu.zip}} {{cesta/k/souboru1_v_archivu cesta/k/souboru2_v_archivu ...}}`
