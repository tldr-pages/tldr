# glib-compile-resources

> Az erőforrás-fájlokat (pl. képeket) bináris erőforrás-csomaggá fordítja. Ezeket a GResource API segítségével GTK-alkalmazásokba lehet linkelni. További információ: <https://manned.org/glib-compile-resources>.

- A `file.gresource.xml` oldalon hivatkozott erőforrásokat .gresource bináris állományba fordítja:

`glib-compile-resources {{file.gresource.xml}}`

- A `file.gresource.xml` oldalon hivatkozott erőforrások fordítása C forrásfájlba:

`glib-compile-resources --generate-source {{file.gresource.xml}}`

- A `file.gresource.xml` alatt található erőforrások lefordítása egy kiválasztott célfájlba, a `.c`, `.h` vagy `.gresource` kiterjesztéssel:

`glib-compile-resources --generate --target={{file.ext}} {{file.gresource.xml}}`

- A `file.gresource.xml` alatt hivatkozott erőforrásfájlok listájának kinyomtatása:

`glib-compile-resources --generate-dependencies {{file.gresource.xml}}`
