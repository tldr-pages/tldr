# mv

> Přesouvá nebo přejmenuje soubory a adresáře.
> Více informací: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- Přejmenovat soubor nebo adresář pokud cíl není už existující adresář:

`mv {{cesta/ke/zdroji}} {{cesta/k/cili}}`

- Přesunout soubor nebo adresář do existujicího adresáře:

`mv {{cesta/ke/zdroji}} {{cesta/k/existujicimu_adresari}}`

- Přesunout více souborů do existujícího adresáře, zachová název souborů:

`mv {{cesta/ke/zdroji1 cesta/ke/zdroji2 ...}} {{cests/k/existujicimu_adresari}}`

- Netázat se pro potrvzení před přepsáním existujících souborů:

`mv {{[-f|--force]}} {{cesta/ke/zdroji}} {{cesta/k/cili}}`

- Zeptat se pro potvrzení interaktivně před přepsáním existujícíh souborů, bez ohledu na oprávnění souborů:

`mv {{[-i|--interactive]}} {{cesta/k/zdroji}} {{cests/k/cili}}`

- Nepřepisovat existující soubory v cíli:

`mv {{[-n|--no-clobber]}} {{cesta/ke/zdroji}} {{cests/k/cili}}`

- Přesunout soubory ve verbózním režimu, zobrazující soubory potom co jsou přesunuty:

`mv {{[-v|--verbose]}} {{cests/ke/zdroji}} {{cesta/k/cili}}`

- Určit cílový adresář abyste mohli puoužít externí nástroje pro sebrání pohyblivých souborů:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv {{[-t|--target-directory]}} {{cesta/k/cilovemu_adresari}}`
