# git lfs

> Lavora con file di grandi dimensioni in repository Git.
> Maggiori informazioni: <https://git-lfs.com>.

- Inizializza Git LFS:

`git lfs install`

- Tieni traccia dei file che soddisfano un criterio glob:

`git lfs track '{{*.bin}}'`

- Cambia l'URL endpoint di Git LFS (utile quando server LFS e server Git sono separati):

`git config -f .lfsconfig lfs.url {{lfs_url_endpoint}}`

- Elenca i criteri tracciati:

`git lfs track`

- Elenca i file tracciati che sono già stati salvati in un commit:

`git lfs ls-files`

- Invia tutti gli oggetti Git LFS al server remoto (utile in caso di errori):

`git lfs push --all {{nome_repository_remoto}} {{nome_ramo}}`

- Scarica tutti gli oggetti Git LFS:

`git lfs fetch`

- Ripristina gli oggetti Git LFS:

`git lfs checkout`
