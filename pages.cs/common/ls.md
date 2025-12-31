# ls

> Vypisuje obsah adresáře.
> Více informací: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Vypsat soubory samostatně na každý řádek:

`ls -1`

- Vypsat všechny soubory, včetně skrytých souborů:

`ls {{[-a|--all]}}`

- Vypsat všechny soubory s koncovým znakem který značí typ souboru (adresář/, symbolický_link@, spustitelný*, ...):

`ls {{[-F|--classify]}}`

- Vypsat všechny soubory s dlouhým formátem (oprávnění, vlastnictví, velikost, a datum změny):

`ls {{[-la|-l --all]}}`

- Vypsat všechny soubory s dlouhým formátem s velikostí v lidsky-čitelných jednotkách (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Vypsat všechny soubory s dlouhým formátem, seřazené podle velikosti (sestupně) rekurzivně:

`ls {{[-lSR|-lS --recursive]}}`

- Vypsat všechny soubory s dlouhým formátem, seřazené podle času změny v obráceném pořadí (nejstarší první):

`ls {{[-ltr|-lt --reverse]}}`

- Vypsat pouze adresáře:

`ls {{[-d|--directory]}} */`
