# kcat

> Apache Kafka termelő és fogyasztó eszköz. További információ: <https://github.com/edenhill/kcat>.

- A legfrissebb eltolással kezdődő üzenetek fogyasztása:

`kcat -C -t {{topic}} -b {{brokers}}`

- A legrégebbi eltolással kezdődő üzenetek fogyasztása és kilépés az utolsó üzenet beérkezése után:

`kcat -C -t {{topic}} -b {{brokers}} -o beginning -e`

- Az üzenetek fogyasztása Kafka fogyasztói csoportként:

`kcat -G {{group_id}} {{topic}} -b {{brokers}}`

- Üzenet közzététele a `stdin` oldalról történő beolvasással:

`echo {{message}} | kcat -P -t {{topic}} -b {{brokers}}`

- Üzenetek közzététele fájlból való olvasással:

`kcat -P -t {{topic}} -b {{brokers}} {{path/to/file}}`

- Az összes téma és bróker metaadatainak listázása:

`kcat -L -b {{brokers}}`

- Egy adott téma metaadatainak listázása:

`kcat -L -t {{topic}} -b {{brokers}}`

- Egy téma/partíció eltolásának lekérdezése egy adott időpontban:

`kcat -Q -t {{topic}}:{{partition}}:{{unix_timestamp}} -b {{brokers}}`
