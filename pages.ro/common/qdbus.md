# qdbus

> Mecanismul de comunicare inter-proces (IPC) și Remote Procedură Calling (RPC) dezvoltat inițial pentru Linux.
> Mai multe informaţii: <https://doc.qt.io/qt-5/qtdbus-index.html>

- Lista denumirilor de servicii disponibile:

`qdbus`

- Lista căilor de obiecte pentru un anumit serviciu:

`qdbus {{service_name}}`

- Lista metodelor, semnalelor și proprietăților disponibile pe un anumit obiect:

`qdbus {{service_name}} {{/path/to/object}}`

- Executați o metodă specifică care trece argumente și afișați valoarea returnată:

`qdbus {{service_name}} {{/path/to/object}} {{method_name}} {{argument1}} {{argument2}}`

- Afișează valoarea curentă a luminozității într-o sesiune KDE Plasma:

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness}}`

- Setați o anumită luminozitate la o sesiune KDE Plasmă:

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness}} {{5000}}`

- Invocați scurtătura de mărire a volumului într-o sesiune KDE Plasma:

`qdbus {{org.kde.kglobalaccel}} {{/component/kmix}} {{invokeShortcut}} "{{increase_volume}}"`

- Ajutor pentru afișare:

`qdbus --help`
