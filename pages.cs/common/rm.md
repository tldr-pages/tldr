# rm

> Maže soubory nebo adresáře.
> Viz také: `rmdir`.
> Více informací: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Smazat konkrétní soubory:

`rm {{cesta/k/souboru1 cesta/k/souboru2 ...}}`

- Smazat konkrétní soubory ignorující neexistující:

`rm {{[-f|--force]}} {{cesta/k/souboru1 cesta/k/souboru2 ...}}`

- Smazat konkrétní soubory dotazující se interaktivně před každým smazáním:

`rm {{[-i|--interactive]}} {{cesta/k/souboru1 cesta/k/souboru2 ...}}`

- Smazat konkrétní soubory vypisující informace o každém smazáním:

`rm {{[-v|--verbose]}} {{cesta/k/souboru1 cesta/k/souboru2 ...}}`

- Smazat konkrétní soubory a adresáře rekurzivně:

`rm {{[-r|--recursive]}} {{cesta/k/souboru_nebo_adresari1 cesta/k/souboru_nebo_adresari2 ...}}`

- Smazat prázdné adresáře (tohle je považováno za bezpečnou metodu):

`rm {{[-d|--dir]}} {{cesta/k/adresari}}`
