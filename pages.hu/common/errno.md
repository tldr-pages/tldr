# errno

> Nézze meg az errno neveket és leírásokat. További információ: <https://joeyh.name/code/moreutils/>.

- Errno leírás keresése név vagy kód alapján:

`errno {{name|code}}`

- Az összes errno név, kód és leírás listázása:

`errno --list`

- Keressen olyan kódot, amelynek leírása tartalmazza a megadott szöveg egészét:

`errno --search {{text}}`

- Olyan kód keresése, amelynek leírása tartalmazza a megadott szöveg egészét (minden helyi nyelven):

`errno --search-all-locales {{text}}`
