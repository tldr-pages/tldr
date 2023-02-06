# watch

> Egy program időszakos végrehajtása, a kimenet teljes képernyőn történő megjelenítése. További információ: <https://manned.org/watch>.

- Egy parancs ismételt futtatása és az eredmény megjelenítése:

`watch {{command}}`

- Egy parancs 60 másodpercenként történő ismételt futtatása:

`watch -n {{60}} {{command}}`

- Figyelje egy könyvtár tartalmát, kiemelve a megjelenő különbségeket:

`watch -d {{ls -l}}`

- Egy csővezeték ismételt futtatása és az eredmény megjelenítése:

`watch '{{command_1}} | {{command_2}} | {{command_3}}'`
