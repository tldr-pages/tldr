# git lfs

> Nagyméretű fájlokkal való munka a Git tárolókban. További információ: <https://git-lfs.github.com>.

- A Git LFS inicializálása:

`git lfs install`

- A globnak megfelelő fájlok követése:

`git lfs track '{{*.bin}}'`

- A Git LFS végpont URL-jének módosítása (hasznos, ha az LFS-kiszolgáló különálló a Git-kiszolgálótól):

`git config -f .lfsconfig lfs.url {{lfs_endpoint_url}}`

- Nyomon követett minták listázása:

`git lfs track`

- Nyomon követett fájlok listázása, amelyeket már átadtak:

`git lfs ls-files`

- Az összes Git LFS objektum átküldése a távoli kiszolgálóra (hasznos, ha hiba lép fel):

`git lfs push --all {{remote_name}} {{branch_name}}`

- Az összes Git LFS objektum lekérése:

`git lfs fetch`

- Az összes Git LFS objektum ellenőrzése:

`git lfs checkout`
