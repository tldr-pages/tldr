# qdbus

> Folyamatok közötti kommunikáció (IPC) és távoli eljáráshívás (RPC) mechanizmus, amelyet eredetileg a Linuxhoz fejlesztettek ki. További információ: <https://doc.qt.io/qt-5/qtdbus-index.html>.

- Az elérhető szolgáltatások neveinek listája:

`qdbus`

- Egy adott szolgáltatás objektum elérési útvonalainak listázása:

`qdbus {{service_name}}`

- Egy adott objektumon elérhető metódusok, jelek és tulajdonságok listázása:

`qdbus {{service_name}} {{/path/to/object}}`

- Egy adott metódus végrehajtása argumentumok átadásával és a visszaadott érték megjelenítése:

`qdbus {{service_name}} {{/path/to/object}} {{method_name}} {{argument1}} {{argument2}}`

- Az aktuális fényerő értékének megjelenítése egy KDE Plasma munkamenetben:

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness}}`

- Egy adott fényerő beállítása egy KDE Plasma munkamenetben:

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness}} {{5000}}`

- Hangerő fel parancsikon meghívása egy KDE Plazma munkamenetben:

`qdbus {{org.kde.kglobalaccel}} {{/component/kmix}} {{invokeShortcut}} "{{increase_volume}}"`

- Súgó megjelenítése:

`qdbus --help`
