# ack

> A grep-hez hasonló, fejlesztők számára optimalizált keresőeszköz. Lásd még: `rg` További információ: <https://beyondgrep.com/documentation>.

- Az aktuális könyvtárban rekurzívan keres egy karakterláncot vagy reguláris kifejezést tartalmazó fájlokat:

`ack "{{search_pattern}}"`

- Nagy- és kisbetűket nem érzékelő minta keresése:

`ack --ignore-case "{{search_pattern}}"`

- A mintának megfelelő sorok keresése, csak az illeszkedő szöveget írja ki, a sor többi részét nem:

`ack -o "{{search_pattern}}"`

- A keresés korlátozása egy adott típusú fájlokra:

`ack --type={{ruby}} "{{search_pattern}}"`

- Ne keressen egy adott típusú fájlokban:

`ack --type=no{{ruby}} "{{search_pattern}}"`

- A talált találatok teljes számának számolása:

`ack --count --no-filename "{{search_pattern}}"`

- Csak a fájlneveket és az egyes fájlok találatainak számát nyomtatja ki:

`ack --count --files-with-matches "{{search_pattern}}"`

- Az összes olyan érték felsorolása, amely a `--type` címmel használható:

`ack --help-types`
