# kwriteconfig5

> KConfig bejegyzések írása a KDE Plazma számára. További információ: <https://userbase.kde.org/KDE_System_Administration/Configuration_Files>.

- Súgó megjelenítése:

`kwriteconfig5 --help`

- Globális konfigurációs kulcs beállítása:

`kwriteconfig5 --group {{group_name}} --key {{key}} {{value}}`

- Kulcs beállítása egy adott konfigurációs fájlban:

`kwriteconfig5 --file {{path/to/file}} --group {{group_name}} --key {{key}} {{value}}`

- Kulcs törlése:

`kwriteconfig5 --group {{group_name}} --key {{key}} --delete`

- A systemd használata a Plasma munkamenet indításához, ha elérhető:

`kwriteconfig5 --file {{startkderc}} --group {{General}} --key {{systemdBoot}} {{true}}`

- A címsor elrejtése, ha egy ablakot maximalizálnak (mint az Ubuntu):

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{Windows}} --key {{BorderlessMaximizedWindows}} {{true}}`

- A KRunner konfigurálása a Meta (Command/Windows) globális gyorsbillentyűvel történő megnyitáshoz:

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{ModifierOnlyShortcuts}} --key {{Meta}} {{"org.kde.kglobalaccel,/component/krunner_desktop,org.kde.kglobalaccel.Component,invokeShortcut,_launch"}}`
