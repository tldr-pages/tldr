# kreadconfig5

> Citiți intrările KConfig pentru Plasma KDE.
> Mai multe informaţii: <https://userbase.kde.org/KDE_System_Administration/Configuration_Files>

- Citiți o cheie din configurația globală:

`kreadconfig5 --group {{group_name}} --key {{key_name}}`

- Citiți o cheie dintr-un fișier de configurare specific:

`kwriteconfig5 --file {{path/to/file}} --group {{group_name}} --key {{key_name}}`

- Verificați dacă systemd este utilizat pentru a începe sesiunea Plasma:

`kreadconfig5 --file {{startkderc}} --group {{General}} --key {{systemdBoot}}`
