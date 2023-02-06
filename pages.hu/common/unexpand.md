# unexpand

> A szóközök tabulátorokká alakítása. További információ: <https://www.gnu.org/software/coreutils/unexpand>.

- Az egyes fájlokban lévő üres részek átalakítása tabulátorokká, a szabványos kimenetre írva:

`unexpand {{path/to/file}}`

- Üresek átalakítása tabulátorokká, olvasás a standard kimenetről:

`unexpand`

- Az összes üres betűket konvertálja, ahelyett, hogy csak a kezdeti üres betűket konvertálná:

`unexpand -a {{path/to/file}}`

- Csak a vezető üres sorozatok átalakítása (felülírja a -a parancsot):

`unexpand --first-only {{path/to/file}}`

- A tabulátorok egymástól bizonyos számú karakterre legyenek, nem 8-ra (engedélyezi a -a-t):

`unexpand -t {{number}} {{path/to/file}}`
