# localectl

> Kontroluj ustawienia regionalne i układ klawiatury systemu.
> Więcej informacji: <https://www.freedesktop.org/software/systemd/man/localectl.html>.

- Wyświetl aktualne ustawienia regionalne systemu i układu klawiatury:

`localectl`

- Wyświetl dostępne ustawienia regionalne:

`localectl list-locales`

- Ustaw zmienną ustawień regionalnych:

`localectl set-locale {{LANG}}={{pl_PL.UTF-8}}`

- Wyświetl dostępne układy klawiatury:

`localectl list-keymaps`

- Ustaw systemowy układ klawiatury dla konsoli i X11:

`localectl set-keymap {{pl}}`
