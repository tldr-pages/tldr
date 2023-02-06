# startx

> A startx szkript az xinit egy front endje, amely egy szép felhasználói felületet biztosít az X Window System egyetlen munkamenetének futtatásához. További információ: <https://x.org/releases/X11R7.5/doc/man/man1/startx.1.html>.

- X munkamenet indítása:

`startx`

- X-munkamenet indítása egy előre meghatározott mélységi értékkel:

`startx -- -depth {{value}}`

- X-munkamenet indítása előre meghatározott dpi-értékkel:

`startx -- -dpi {{value}}`

- A `.xinitrc` fájlban lévő beállítások felülírása és új X-munkamenet indítása:

`startx /{{path/to/window_manager_or_desktop_environment}}`
