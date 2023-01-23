# clip

> A bemeneti tartalom másolása a Windows vágólapjára. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- A parancssori kimenet átvezetése a Windows vágólapjára:

`{{dir}} | clip`

- Egy fájl tartalmának másolása a Windows vágólapjára:

`clip < {{path/to/file.ext}}`

- Szöveg másolása a Windows vágólapra egy újsorral a végén:

`echo {{some text}} | clip`

- Szöveg másolása a Windows vágólapra újsor nélkül:

`echo | set /p="some text" | clip`
