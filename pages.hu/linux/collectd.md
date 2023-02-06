# collectd

> Rendszerstatisztika-gyűjtő démon. További információ: <https://collectd.org/>.

- Használati súgó megjelenítése, beleértve a program verzióját is:

`collectd -h`

- A konfigurációs fájl tesztelése, majd kilépés:

`collectd -t`

- A plugin adatgyűjtési funkciójának tesztelése, majd kilépés:

`collectd -T`

- A collectd indítása:

`collectd`

- Egyéni konfigurációs fájl helyének megadása:

`collectd -C {{path/to/file}}`

- Egyéni PID-fájl helyének megadása:

`collectd -P {{path/to/file}}`

- Ne lépjen a háttérbe:

`collectd -f`
