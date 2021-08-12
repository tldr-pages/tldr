# dex

> DesktopEntry Execution este un program pentru a genera și executa fișiere DesktopEntry de tip Application.
> Mai multe informaţii: <https://github.com/jceb/dex>

- Executați toate programele din folderele autostart:

`dex --autostart`

- Executați toate programele din dosarele specificate:

`dex --autostart --search-paths {{path/to/directory1}}:{{path/to/directory2}}:{{path/to/directory3}}:`

- Previzualizarea programelor va fi executată într-un autostart specific GNOME:

`dex --autostart --environment {{GNOME}}`

- Previzualizarea programelor ar fi executate într-un autostart regulat:

`dex --autostart --dry-run`

- Previzualizaţi valoarea proprietăţii DesktopEntry `Name`:

`dex --property {{Name}} {{path/to/file.desktop}}`

- Creați un DesktopEntry pentru un program în directorul curent:

`dex --create {{path/to/file.desktop}}`

- Executați un singur program (cu `terminal=true` în fișierul desktop) în terminalul dat:

`dex --term {{terminal}} {{path/to/file.desktop}}`
