# mixxx

> Ingyenes és nyílt forráskódú cross-platform DJ szoftver. További információ: <https://mixxx.org/manual/latest/chapters/appendix.html#command-line-options>.

- Indítsa el a Mixxx GUI-t teljes képernyőn:

`mixxx --fullScreen`

- Indítsa el biztonságos fejlesztői módban az összeomlás hibakereséséhez:

`mixxx --developer --safeMode`

- Hibás működés hibájának elhárítása:

`mixxx --debugAssertBreak --developer --loglevel trace`

- A Mixxx elindítása a megadott beállításfájl használatával:

`mixxx --resourcePath {{mixxx/res/controllers}} --settingsPath {{path/to/settings-file}}`

- Egyéni vezérlő hozzárendelés hibakeresése:

`mixxx --controllerDebug --resourcePath {{path/to/mapping-directory}}`

- Parancssori súgó megjelenítése:

`mixxx --help`
