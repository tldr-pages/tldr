# pio project

> PlatformIO projektek kezelésére szolgáló eszköz. További információ: <https://docs.platformio.org/en/latest/core/userguide/project/>.

- Új PlatformIO projekt inicializálása:

`pio project init`

- Új PlatformIO projekt inicializálása egy adott könyvtárban:

`pio project init --project-dir {{path/to/project_directory}}`

- Új PlatformIO-projekt inicializálása egy lapazonosító megadásával:

`pio project init --board {{ATmega328P|uno|...}}`

- Új PlatformIO alapú projekt inicializálása egy vagy több projektopció megadásával:

`pio project init --project-option="{{option}}={{value}}" --project-option="{{option}}={{value}}"`

- Egy projekt konfigurációjának kinyomtatása:

`pio project config`
