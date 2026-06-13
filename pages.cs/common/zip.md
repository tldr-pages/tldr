# zip

> Zabaluje a komprimuje (archivuje) soubory do Zip archivu.
> Viz také: `unzip`.
> Více informací: <https://manned.org/zip>.

- Přidat soubory/adresáře do konkrétního archivu:

`zip {{[-r|--recurse-paths]}} {{cesta/ke/komprimovanemu.zip}} {{cesta/k/souboru_nebo_adresari1 cesta/k/souboru_nebo_adresari2 ...}}`

- Vymazat soubory/adresáře z konkrétního archivu:

`zip {{[-d|--delete]}} {{cesta/ke/komprimovanemu.zip}} {{cesta/k/souboru_nebo_adresari1 cesta/k/souboru_nebo_adresari2 ...}}`

- Archivovat soubory/adresáře kromě uvedených:

`zip {{[-r|--recurse-paths]}} {{cesta/ke/komprimovanemu.zip}} {{cesta/k/souboru_nebo_adresari1 cesta/k/souboru_nebo_adresari2 ...}} {{[-x|--exclude]}} {{cesta/k/vyrazenych_souboru_nebo_adresaru}}`

- Archivovat soubory/adresáře s určitou úrovní komprimace (`0` - nejnižší, `9` - nejvyšší):

`zip {{[-r|--recurse-paths]}} -{{0..9}} {{cesta/ke/komprimovanemu.zip}} {{cesta/k/souboru_nebo_adresari1 cesta/k/souboru_nebo_adresari2...}}`

- Vytvořit zašifrovaný archiv pod uvedeným heslem:

`zip {{[-re|--recurse-paths --encrypt]}} {{cesta/ke/komprimovanemu.zip}} {{cesta/k/souboru_nebo_adresari1 cesta/k/souboru_nebo_adresari2 ...}}`

- Archivovat soubory/složky do vícedílného rozděleného Zip archivu (např. 3GB díly):

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{cesta/ke/komprimovanemu.zip}} {{cesta/k/souboru_nebo_adresari1 cesta/k/souboru_nebo_adresari2 ...}}`

- Vypsat obsah konkrétního archivu:

`zip {{[-sf|--split-size --freshen]}} {{cesta/ke/komprimovanemu.zip}}`
