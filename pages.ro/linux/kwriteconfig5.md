# kwriteconfig5

> Scrieți intrările KConfig pentru Plasma KDE.
> Mai multe informaţii: <https://userbase.kde.org/KDE_System_Administration/Configuration_Files>

- Ajutor pentru afișare:

`kwriteconfig5 --help`

- Setați o cheie de configurare globală:

`kwriteconfig5 --group {{group_name}} --key {{key}} {{value}}`

- Setați o cheie într-un fișier de configurare specific:

`kwriteconfig5 --file {{path/to/file}} --group {{group_name}} --key {{key}} {{value}}`

- Şterge o cheie:

`kwriteconfig5 --group {{group_name}} --key {{key}} --delete`

- Utilizați systemd pentru a începe sesiunea Plasma atunci când este disponibil:

`kwriteconfig5 --file {{startkderc}} --group {{General}} --key {{systemdBoot}} {{true}}`

- Ascunde bara de titlu atunci când o fereastră este maximizată (cum ar fi Ubuntu):

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{Windows}} --key {{BorderlessMaximizedWindows}} {{true}}`

- Configurați KRunner pentru a deschide cu tasta globală Meta (Command/Windows):

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{ModifierOnlyShortcuts}} --key {{Meta}} {{"org.kde.kglobalaccel,/component/krunner_desktop,org.kde.kglobalaccel.Component,invokeShortcut,_launch"}}`
