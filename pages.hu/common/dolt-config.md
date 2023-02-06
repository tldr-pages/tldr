# dolt config

> Helyi (tárolónként) és globális (felhasználónként) Dolt konfigurációs változók olvasása és írása. További információ: <https://docs.dolthub.com/interfaces/cli#dolt-config>.

- Az összes helyi és globális konfigurációs beállítási lehetőség és azok értékeinek felsorolása:

`dolt config --list`

- Egy helyi vagy globális konfigurációs változó értékének megjelenítése:

`dolt config --get {{name}}`

- Módosíthatja egy helyi konfigurációs változó értékét, létrehozhatja, ha nem létezik:

`dolt config --add {{name}} {{value}}`

- Globális konfigurációs változó értékének módosítása, létrehozva azt, ha nem létezik:

`dolt config --global --add {{name}} {{value}}`

- Helyi konfigurációs változó törlése:

`dolt config --unset {{name}}`

- Globális konfigurációs változó törlése:

`dolt config --global --unset {{name}}`
