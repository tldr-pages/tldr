# starship

> A minimális, villámgyors és végtelenül testreszabható prompt bármelyik shellhez. Néhány alparancsnak, mint például a `starship init`, saját használati dokumentációja van. További információ: <https://starship.rs>.

- Kiírja a csillaghajó integrációs kódját a megadott héjhoz:

`starship init {{bash|elvish|fish|ion|powershell|tcsh|zsh}}`

- Az aktuális prompt minden egyes részének magyarázata és a megjelenítésükhöz szükséges idő megjelenítése:

`starship explain`

- A kiszámított csillaghajó-konfiguráció kinyomtatása (a `--default` használatával az alapértelmezett konfigurációt nyomtathatja ki helyette):

`starship print-config`

- A támogatott modulok listája:

`starship module --list`

- A csillaghajó konfigurációjának szerkesztése az alapértelmezett szerkesztőprogramban:

`starship configure`

- Hibajelentés létrehozása GitHub issue előre kitöltve a rendszerre és a csillaghajó konfigurációjára vonatkozó információkkal:

`starship bug-report`

- A megadott héjhoz tartozó befejező szkript kinyomtatása:

`starship completions {{bash|elvish|fish|powershell|zsh}}`

- Súgó megjelenítése egy alparancshoz:

`starship {{subcommand}} --help`
