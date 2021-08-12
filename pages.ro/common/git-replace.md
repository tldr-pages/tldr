# git replace

> Creați, listați și ștergeți refs pentru a înlocui obiecte.
> Mai multe informaţii: <https://git-scm.com/docs/git-replace>

- Înlocuiți orice comitere cu unul diferit, lăsând alte comite neschimbate:

`git replace {{object}} {{replacement}}`

- Ștergeți refs înlocuiți existente pentru obiectele date:

`git replace --delete {{object}}`

- Editează interactiv conținutul unui obiect:

`git replace --edit {{object}}`
