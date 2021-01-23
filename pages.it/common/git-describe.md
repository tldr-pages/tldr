# git describe

> Rendi il nome di un oggetto Git più leggibile usando i riferimenti disponibili.
> Maggiori informazioni: <https://git-scm.com/docs/git-describe>.

- Crea un nome univoco per il commit corrente (il nome contiene i tag più recenti, il numero di commit aggiuntivi, e l'hash breve del commit):

`git describe`

- Crea un nome di 4 cifre per l'hash breve del commit:

`git describe --abbrev={{4}}`

- Genera un nome che includa anche il percorso di riferimento:

`git describe --all`

- Descrivi un tag Git:

`git describe {{v1.0.0}}`

- Crea un nome per l'ultimo commit di un dato ramo:

`git describe {{nome_ramo}}`
