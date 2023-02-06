# xonsh

> Python-alapú, platformokon átívelő, Unix-gázoló shell. sh/Python kód írása és keverése a Xonsh-ban (ejtsd: conch). További információ: <https://xon.sh>.

- Interaktív shell munkamenet indítása:

`xonsh`

- Egyetlen parancs végrehajtása, majd kilépés:

`xonsh -c "{{command}}"`

- Parancsok futtatása egy szkriptfájlból, majd kilépés:

`xonsh {{path/to/script_file.xonsh}}`

- Környezeti változók definiálása a shell-folyamat számára:

`xonsh -D{{name1}}={{value1}} -D{{name2}}={{value2}}`

- A megadott `.xonsh` vagy `.json` konfigurációs fájlok betöltése:

`xonsh --rc {{path/to/file1.xonsh}} {{path/to/file2.json}}`

- A `.xonshrc` konfigurációs fájl betöltésének kihagyása:

`xonsh --no-rc`
