# lighthouse

> Elemzi a webalkalmazásokat és weboldalakat, modern teljesítménymutatókat és a fejlesztők legjobb gyakorlataira vonatkozó információkat gyűjt. További információ: <https://github.com/GoogleChrome/lighthouse>.

- HTML-jelentést generál egy adott weboldalhoz, és elmenti az aktuális könyvtárban lévő fájlba:

`lighthouse {{https://example.com}}`

- JSON-jelentés generálása és kinyomtatása:

`lighthouse --output {{json}} {{https://example.com}}`

- JSON-jelentés generálása és mentése egy adott fájlba:

`lighthouse --output {{json}} --output-path {{path/to/file.json}} {{https://example.com}}`

- Jelentés generálása a böngésző használatával headless módban, bejelentkezés nélkül a `stdout` oldalon:

`lighthouse --quiet --chrome-flags="{{--headless}}" {{https://example.com}}`

- Jelentés generálása a megadott JSON-fájlban található HTTP-fejléc kulcs/érték párok felhasználásával az összes kérelemre vonatkozóan:

`lighthouse --extra-headers={{path/to/file.json}} {{https://example.com}}`

- Kizárólag bizonyos kategóriákra vonatkozó jelentés készítése:

`lighthouse --only-categories={{performance,accessibility,best-practices,seo,pwa}} {{https://example.com}}`

- Jelentés készítése eszközemulációval és minden fojtás kikapcsolásával:

`lighthouse --screenEmulation.disabled --throttling-method={{provided}} --no-emulatedUserAgent {{https://example.com}}`

- Súgó megjelenítése:

`lighthouse --help`
