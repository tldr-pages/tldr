# watch

> Egy parancs ismételt végrehajtása, és a kimenet teljes képernyős módban történő figyelése. További információ: <https://manned.org/watch>.

- Az aktuális könyvtárban lévő fájlok figyelése:

`watch {{ls}}`

- A lemezterület figyelése és a változások kiemelése:

`watch -d {{df}}`

- Figyelje a "csomóponti" folyamatokat, 3 másodpercenkénti frissítéssel:

`watch -n {{3}} "{{ps aux | grep node}}"`
