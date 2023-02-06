# pio test

> Helyi tesztek futtatása egy PlatformIO projektben. További információ: <https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>.

- Az összes teszt futtatása az aktuális PlatformIO projekt összes környezetében:

`pio test`

- Csak bizonyos környezetek tesztelése:

`pio test --environment {{environment1}} --environment {{environment2}}`

- Csak olyan tesztek futtatása, amelyek neve megfelel egy adott glob-mintának:

`pio test --filter "{{pattern}}"`

- Azon tesztek figyelmen kívül hagyása, amelyek neve egyezik egy adott glob-mintával:

`pio test --ignore "{{pattern}}"`

- Port megadása a firmware feltöltéséhez:

`pio test --upload-port {{upload_port}}`

- Egyéni konfigurációs fájl megadása a tesztek futtatásához:

`pio test --project-conf {{path/to/platformio.ini}}`
