# cupsd

> Kiszolgáló démon a CUPS nyomtatókiszolgálóhoz. További információ: <https://www.cups.org/doc/man-cupsd.html>.

- Indítsa el a `cupsd` oldalt a háttérben, más néven démonként:

`cupsd`

- A `cupsd` indítása a \[f\]orgroundon:

`cupsd -f`

- \[l\]aunch `cupsd` on-demand (általában a `launchd` vagy a `systemd`):

`cupsd -l`

- A `cupsd` indítása a megadott \[`c`\]`upsd.conf` konfigurációs fájl segítségével:

`cupsd -c {{path/to/cupsd.conf}}`

- A `cupsd` indítása a megadott `cups-file`\[`s`\]`.conf` konfigurációs fájl használatával:

`cupsd -s {{path/to/cups-files.conf}}`

- \[t\]est the \[`c`\]`upsd.conf` configuration file for errors:

`cupsd -t -c {{path/to/cupsd.conf}}`

- \[t\]est the `cups-file`\[`s`\]`.conf` configuration file for errors:

`cupsd -t -s {{path/to/cups-files.conf}}`

- Az összes rendelkezésre álló opció megjelenítése:

`cupsd -h`
