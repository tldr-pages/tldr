# git am

> Applica file di patch. Utile quando si ricevono commits via email.
> Vedi anche `git format-patch` per generare file di patch.
> Maggiori informazioni: <https://git-scm.com/docs/git-am>.

- Applica un file di patch:

`git am {{percorso/al/file.patch}}`

- Interrompi l'applicazione di un file di patch:

`git am --abort`

- Applica quanto possibile di un file di patch e salva in *.rej file le parti la cui applicazione non è andata a buon fine:

`git am --reject {{percorso/al/file.patch}}`
