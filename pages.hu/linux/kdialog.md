# kdialog

> KDE párbeszédpanelek megjelenítése shell szkriptekből. További információ: <https://develop.kde.org/deploy/kdialog/>.

- Egy adott üzenetet megjelenítő párbeszédpanel megnyitása:

`kdialog --msgbox "{{message}}" "{{optional_detailed_message}}"`

- Kérdés párbeszédpanel megnyitása a `yes` és a `no` gombbal, a `0` és a `1` visszaadásával:

`kdialog --yesno "{{message}}"`

- Figyelmeztető párbeszédpanel megnyitása a `yes`, `no` és `cancel` gombokkal, amelyek a `0`, `1`, illetve a `2` gombokat adják vissza:

`kdialog --warningyesnocancel "{{message}}"`

- Nyisson meg egy beviteli párbeszédpanelt, és a `OK` gomb megnyomásakor nyomtassa ki a bevitelt a `stdout` címre:

`kdialog --inputbox "{{message}}" "{{optional_default_text}}"`

- Megnyit egy párbeszédpanelt, amely egy adott jelszó megadására szólít fel, és azt a `stdout` címre nyomtatja ki:

`kdialog --password "{{message}}"`

- Megnyit egy párbeszédpanelt, amely egy adott legördülő menüt tartalmaz, és a kiválasztott elemet a `stdout` címre nyomtatja:

`kdialog --combobx "{{message}}" "{{item1}}" "{{item2}}" "{{...}}"`

- Fájlválasztó párbeszédpanel megnyitása és a kiválasztott fájl elérési útvonalának kinyomtatása a `stdout` címre:

`kdialog --getopenfilename`

- Egy előrehaladási párbeszédpanel megnyitása és a DBUS-hivatkozás kinyomtatása a kommunikációhoz a `stdout` címre:

`kdialog --progressbar "{{message}}"`
