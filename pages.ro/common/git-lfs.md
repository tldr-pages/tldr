# git lfs

> Lucrul cu fișiere mari în depozitele Git.
> Mai multe informaţii: <https://git-lfs.github.com>

- Inițializează Git LFS:

`git lfs install`

- Urmăriți fișierele care se potrivesc cu un glob:

`git lfs track '{{*.bin}}'`

- Modificați URL-ul punctului final Git LFS (util dacă serverul LFS este separat de serverul Git):

`git config -f .lfsconfig lfs.url {{lfs_endpoint_url}}`

- Lista modelelor urmărite:

`git lfs track`

- Lista fișierelor urmărite care au fost comise:

`git lfs ls-files`

- Împingeți toate obiectele Git LFS la serverul de la distanță (util dacă se întâlnesc erori):

`git lfs push --all {{remote_name}} {{branch_name}}`

- Adu toate obiectele Git LFS:

`git lfs fetch`

- Checkout toate obiectele Git LFS:

`git lfs checkout`
