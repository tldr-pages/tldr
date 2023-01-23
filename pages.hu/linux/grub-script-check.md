# grub-script-check

> A `grub-script-check` program egy GRUB szkriptfájlt vesz át, és ellenőrzi, hogy nincs-e benne szintaktikai hiba. Nem opciós argumentumként megadhatja az elérési utat. Ha nincs megadva, akkor a standard bemenetről fog olvasni. További információ: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dscript_002dcheck.html>.

- Egy adott szkriptfájl ellenőrzése szintaxis hibák szempontjából:

`grub-script-check {{path/to/grub_config_file}}`

- A bemenet minden sorának megjelenítése a beolvasás után:

`grub-script-check --verbose`

- Verzió megjelenítése:

`grub-script-check --version`

- Súgó megjelenítése:

`grub-script-check --help`
