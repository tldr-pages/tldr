# cp

> Kopíruje soubory a adresáře.
> Více informací: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- Zkopírovat soubor do jiné lokace:

`cp {{cesta/ke/zdrojovemu_souboru.ext}} {{cesta/k/cilovemu_souboru.ext}}`

- Zkopírovat soubor do jiného adresáře, zachová název souboru:

`cp {{cesta/ke/zdrojovemu_adresari.ext}} {{cesta/k/nadrazenemu_adresari}}`

- Rekurzivně zkopírovat obsah adresáře do jiné lokace (pokud cíl existuje, adresář se zkopíruje do něj):

`cp {{[-r|--recursive]}} {{cesta/ke/zdrojovemu_adresari}} {{cesta/k/cilovemu_adresare}}`

- Zkopírovat adresář rekurzivně, ve verbózním režimu (zobrazí soubory jak jsou zkopírovány):

`cp {{[-vr|--verbose --recursive]}} {{cesta/ke/zdrojovemu_adresari}} {{cesta/k/cilovemu_adresari}}`

- Zkopírovat více souborů do adresáře naráz:

`cp {{[-t|--target-directory]}} {{cesta/k/cilovemu_adresari}} {{cesta/k/souboru1 cesta/k/souboru2 ...}}`

- Zkopírovat všechny soubory se specifickou koncovkou do jiné lokace, v interaktívním režimu (zeptá se uživatele před přepsáním):

`cp {{[-i|--interactive]}} {{*.ext}} {{cesta/k/cilovemu_adresari}}`

- Následovat symbolické linky před zkopírováním:

`cp {{[-L|--dereference]}} {{link}} {{cesta/k/cilovemu_adresari}}`

- Používat plnou cestu zdrojových souborů, automaticky vytvoří jakékoliv chybějící meziadresáře při kopírováním:

`cp --parents {{zdrojova/cesta/k/souboru}} {{cesta/k/cilovemu_souboru}}`
