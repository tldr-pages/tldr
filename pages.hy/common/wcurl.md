# wcurl

> Պարզ փաթաթում `curl`-ի շուրջ՝ ֆայլերը հեշտությամբ ներբեռնելու համար:.
> Տես նաև՝ `wget`, `curl`:.
> Լրացուցիչ տեղեկություններ. <https://curl.se/wcurl/manual.html>:.

- Ներբեռնեք URL-ի բովանդակությունը URL-ով նշված ֆայլում (այս դեպքում՝ `index.html`).:

`wcurl {{https://example.com/index.html}}`

- Ներբեռնեք URL-ի բովանդակությունը նշված անունով ֆայլում՝:

`wcurl {{[-o|--output]}} {{path/to/file}} {{https://example.com/index.html}}`

- Ներբեռնեք URL-ի բովանդակությունը՝ միացնելով առաջընթացի գիծը և լռելյայն դնելով HTTP/2:

`wcurl --curl-options "--progress-bar --http2" {{https://example.com/index.html}}`

- Վերսկսել ընդհատված ներբեռնումից.:

`wcurl --curl-options "--clobber --continue-at -" {{https://example.com/index.html}}`
