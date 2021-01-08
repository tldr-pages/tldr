# git format-patch

> Prepara file .patch. Utile per l'invio di commit via email.
> Vedi anche `git am`, che permette di applicare file .patch.
> Maggiori informazioni: <https://git-scm.com/docs/git-format-patch>.

- Crea un file `.patch` (il nome è assegnato automaticamente) con i commit non ancora inviati al repository remoto:

`git format-patch {{origin}}`

- Scrivi su `stdout` un file `.patch` per l'intervallo di commit definito dai due commit dati:

`git format-patch --stdout {{commit_1}}..{{commit_2}}`

- Scrivi un file `.patch` per gli ultimi 3 commit:

`git format-patch -{{3}}`
