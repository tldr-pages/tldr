# gzip

> Komprimuje/dekomprimuje soubory s `gzip` kompresí (LZ77).
> Více informací: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Komprimovat soubor a nahradit jej `gzip` archivem:

`gzip {{cesta/k/souboru}}`

- Dekomprimovat souboru a nahradit jej původní nekomprimovanou verzí:

`gzip {{[-d|--decompress]}} {{cesta/k/souboru.gz}}`

- Komprimovat soubor se zachováním původního souboru:

`gzip {{[-k|--keep]}} {{cesta/k/souboru}}`

- Komprimovat soubor a zadat název výstupního souboru:

`gzip {{[-c|--stdout]}} {{cesta/k/souboru}} > {{souboru/k/komprimovanemu_souboru.gz}}`

- Dekomprimovat `gzip` archiv a zadat název výstupního souboru:

`gzip {{[-c|--stdout]}} {{[-d|--decompress]}} {{cesta/k/souboru.gz}} > {{cesta/k/nekomprimovanemu_souboru}}`

- Upřesnit úroveň komprese. 1 je nejrychlejší (nízká komprese), 9 je nejpomalejší (vysoká komprese), 6 je výchozí:

`gzip -{{1..9}} {{[-c|--stdout]}} {{cesta/k/souboru}} > {{cesta/ke/komprimovanemu_souboru.gz}}`

- Zobrazit název a procento zmenšení pro každý komprimovaný nebo dekomprimovaný soubor:

`gzip {{[-v|--verbose]}} {{[-d|--decompress]}} {{cesta/k/souboru.gz}}`
