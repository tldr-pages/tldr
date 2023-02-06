# xidel

> Letöltés és kivonatolás HTML/XML oldalakból, valamint JSON API-kból. További információ: <https://www.videlibri.de/xidel.html>.

- A Google-keresés által talált összes URL kinyomtatása:

`xidel {{https://www.google.com/search?q=test}} --extract "//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']"`

- A Google-keresés által talált összes oldal címének kinyomtatása és letöltése:

`xidel {{https://www.google.com/search?q=test}} --follow "{{//a/extract(@href, 'url[?]q=([^&]+)&', 1)[. != '']}}" --extract {{//title}} --download {{'{$host}/'}}`

- Kövesse az összes linket egy oldalon és nyomtassa ki a címeket, XPath segítségével:

`xidel {{https://example.org}} --follow {{//a}} --extract {{//title}}`

- Kövesse az összes linket egy oldalon és nyomtassa ki a címeket CSS-szelektorokkal:

`xidel {{https://example.org}} --follow "{{css('a')}}" --css {{title}}`

- Kövesse az összes linket egy oldalon, és nyomtassa ki a címeket, mintaillesztéssel:

`xidel {{https://example.org}} --follow "{{<a>{.}</a>*}}" --extract "{{<title>{.}</title>}}"`

- A minta beolvasása a example.xml-ből (amely azt is ellenőrzi, hogy a "ood" elemet tartalmazó elem ott van-e, ellenkező esetben nem):

`xidel {{path/to/example.xml}} --extract "{{<x><foo>ood</foo><bar>{.}</bar></x>}}"`

- A Stack Overflow összes legújabb kérdésének kiírása címmel és URL-címmel, mintakövetéssel az RSS-csatornán:

`xidel {{http://stackoverflow.com/feeds}} --extract "{{<entry><title>{title:=.}</title><link>{uri:=@href}</link></entry>+}}"`

- Olvasatlan Reddit-levelek ellenőrzése, Webscraping, CSS, XPath, JSONiq és automatikus űrlapkiértékelés kombinálása:

`xidel {{https://reddit.com}} --follow "{{form(css('form.login-form')[1], {'user': '$your_username', 'passwd': '$your_password'})}}" --extract "{{css('#mail')/@title}}"`
