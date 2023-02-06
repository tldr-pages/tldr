# btrbk

> Eszköz pillanatképek és távoli biztonsági mentések készítésére a btrfs alvolumenekről. További információ: <https://digint.ch/btrbk/doc/readme.html>.

- Statisztikák nyomtatása a konfigurált alkötegekről és pillanatképekről:

`sudo btrbk stats`

- A konfigurált alkötegek és pillanatfelvételek listázása:

`sudo btrbk list`

- Kiírja, hogy mi történne egy futtatás során a megjelenített változtatások nélkül:

`sudo btrbk --verbose dryrun`

- Biztonsági mentési rutinok verbális futtatása, előrehaladási sáv megjelenítése:

`sudo btrbk --progress --verbose run`

- Csak a konfigurált alkötegek pillanatfelvételeinek létrehozása:

`sudo btrbk snapshot`
