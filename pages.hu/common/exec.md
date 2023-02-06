# exec

> Az aktuális folyamatot egy másik folyamatra cseréli. További információ: <https://linuxcommand.org/lc3_man_pages/exech.html>.

- Cserélje ki a megadott paranccsal az aktuális környezeti változók felhasználásával:

`exec {{command -with -flags}}`

- A megadott paranccsal való helyettesítése a környezeti változók törlésével:

`exec -c {{command -with -flags}}`

- Cserélje ki a megadott parancsra és jelentkezzen be az alapértelmezett shell használatával:

`exec -l {{command -with -flags}}`

- Cserélje ki a megadott paranccsal és változtassa meg a folyamat nevét:

`exec -a {{process_name}} {{command -with -flags}}`
