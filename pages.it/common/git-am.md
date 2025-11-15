# git am

> Applica file di patch. Utile quando si ricevono commit via email.
> Vedi anche `git format-patch` per generare file di patch.
> Maggiori informazioni: <https://git-scm.com/docs/git-am>.

- Applica un file di patch:

`git am {{percorso/del/file.patch}}`

- Interrompi l'applicazione di un file di patch:

`git am --abort`

- Applica quanto possibile di un file di patch, salvando le parti non applicabili in file `.rej`:

`git am --reject {{percorso/del/file.patch}}`
