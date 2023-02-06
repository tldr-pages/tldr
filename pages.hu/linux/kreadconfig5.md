# kreadconfig5

> KConfig bejegyzések olvasása a KDE Plasma számára. További információ: <https://userbase.kde.org/KDE_System_Administration/Configuration_Files>.

- Kulcs beolvasása a globális konfigurációból:

`kreadconfig5 --group {{group_name}} --key {{key_name}}`

- Kulcs beolvasása egy adott konfigurációs fájlból:

`kwriteconfig5 --file {{path/to/file}} --group {{group_name}} --key {{key_name}}`

- Annak ellenőrzése, hogy a systemd-t használják-e a Plasma munkamenet indításához:

`kreadconfig5 --file {{startkderc}} --group {{General}} --key {{systemdBoot}}`
