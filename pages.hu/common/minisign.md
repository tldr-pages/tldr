# minisign

> Egyszerű eszköz fájlok aláírására és az aláírások ellenőrzésére. További információ: <https://jedisct1.github.io/minisign/>.

- Új kulcspár generálása az alapértelmezett helyen:

`minisign -G`

- Fájl aláírása:

`minisign -Sm {{path/to/file}}`

- Egy fájl aláírása, egy megbízható (aláírt) és egy nem megbízható (nem aláírt) megjegyzés hozzáadásával az aláíráshoz:

`minisign -Sm {{path/to/file}} -c "{{Untrusted comment}}" -t "{{Trusted comment}}"`

- Egy fájl és az aláírásában szereplő megbízható megjegyzések ellenőrzése a megadott nyilvános kulcsfájl használatával:

`minisign -Vm {{path/to/file}} -p {{path/to/publickey.pub}}`

- Egy fájl és az aláírásában szereplő megbízható megjegyzések hitelesítése, a nyilvános kulcs megadása Base64 kódolt literálként:

`minisign -Vm {{path/to/file}} -P "{{public_key_base64}}"`
