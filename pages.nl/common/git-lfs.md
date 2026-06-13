# git lfs

> Werk met grote bestanden in Git repositories.
> Meer informatie: <https://github.com/git-lfs/git-lfs/tree/main/docs>.

- Initialiseer Git LFS:

`git lfs install`

- Houd bestanden bij die overeenkomen met een glob:

`git lfs track '{{*.bin}}'`

- Verander de Git LFS-eindpunt URL (handig als de LFS-server gescheiden is van de Git-server):

`git config {{[-f|--file]}} .lfsconfig lfs.url {{lfs_eindpunt_url}}`

- Toon patronen die worden bijgehouden:

`git lfs track`

- Toon bestanden die worden bijgehouden en gecommit zijn:

`git lfs ls-files`

- Push alle Git LFS-objecten naar de externe server (handig als er fouten optreden):

`git lfs push --all {{externe_naam}} {{branch_naam}}`

- Haal alle Git LFS-objecten op:

`git lfs fetch`

- Vervang pointerbestanden met werkelijke Git LFS-objecten:

`git lfs checkout`
