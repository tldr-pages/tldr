# xml փախուստ

> Խուսափել հատուկ XML նիշերից, օրինակ. `<a1>` → `&lt;a1&gt;`:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139540960>:.

- Խուսափեք հատուկ XML նիշերից տողի մեջ.:

`xml {{[esc|escape]}} "{{<a1>}}"`

- Խուսափեք հատուկ XML նիշերից `stdin`-ից:

`echo "{{<a1>}}" | xml {{[esc|escape]}}`

- Ցուցադրել օգնությունը.:

`xml {{[esc|escape]}} --help`
