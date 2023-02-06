# dex

> A DesktopEntry Execution egy olyan program, amely az Application típusú DesktopEntry fájlokat generálja és hajtja végre. További információ: <https://github.com/jceb/dex>.

- Az automatikus indítás mappákban található összes program végrehajtása:

`dex --autostart`

- A megadott mappákban lévő összes program végrehajtása:

`dex --autostart --search-paths {{path/to/directory1}}:{{path/to/directory2}}:{{path/to/directory3}}:`

- A programok előnézete a GNOME-specifikus automatikus indításban kerülnének végrehajtásra:

`dex --autostart --environment {{GNOME}}`

- A programok előnézete a szokásos automatikus indításban kerülne végrehajtásra:

`dex --autostart --dry-run`

- A DesktopEntry tulajdonság értékének előnézete `Name`:

`dex --property {{Name}} {{path/to/file.desktop}}`

- DesktopEntry létrehozása az aktuális könyvtárban lévő programhoz:

`dex --create {{path/to/file.desktop}}`

- Egyetlen program végrehajtása (a `Terminal=true` asztali fájlban lévő címmel) az adott terminálon:

`dex --term {{terminal}} {{path/to/file.desktop}}`
