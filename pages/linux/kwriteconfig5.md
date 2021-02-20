# kwriteconfig5

> Write KConfig entries for KDE Plasma.
> More information: <https://userbase.kde.org/KDE_System_Administration/Configuration_Files>.

- Set a global configuration key:

`kwriteconfig5 --group {{group_name}} --key {{key_name}} {{value}}`

- Set a key in a specific configuration file:

`kwriteconfig5 --file {{path/to/file}} --group {{group_name}} --key {{key_name}} {{value}}`

- Delete a key:

`kwriteconfig5 --group {{group_name}} --key {{key_name}} --delete`

- Use systemd to start the Plasma session when available:

`kwriteconfig5 --file {{startkderc}} --group {{General}} --key {{systemdBoot}} {{true}}`

- Hide the title bar when a window is maximized (like Ubuntu):

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{Windows}} --key {{BorderlessMaximizedWindows}} {{true}}`

- Open KRunner with the Meta (Command/Windows) key:

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{ModifierOnlyShortcuts}} --key {{Meta}} {{"org.kde.kglobalaccel,/component/krunner_desktop,org.kde.kglobalaccel.Component,invokeShortcut,_launch"}}`
