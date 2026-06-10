# xml unescape

> Unescape հատուկ XML նիշերից, օրինակ. `&lt;a1&gt;` → `<a1>`:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139540960>:.

- Անջատեք հատուկ XML նիշերը տողից.:

`xml {{[unesc|unescape]}} "{{&lt;a1&gt;}}"`

- Հեռացնել հատուկ XML նիշերը `stdin`-ից:

`echo "{{&lt;a1&gt;}}" | xml {{[unesc|unescape]}}`

- Ցուցադրել օգնությունը.:

`xml {{[unesc|unescape]}} --help`
