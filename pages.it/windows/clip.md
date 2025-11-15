# clip

> Copia il contenuto di input negli Appunti di Windows.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- Manda l'output della riga di comando negli Appunti di Windows:

`{{dir}} | clip`

- Copia i contenuti di un file negli appunti di Windows:

`clip < {{percorso\per\file.ext}}`

- Copia il testo con una nuova riga finale negli appunti di Windows:

`echo {{testo_generico}} | clip`

- Copia il testo senza una nuova riga finale negli appunti di Windows:

`echo | set /p="testo_generico" | clip`
