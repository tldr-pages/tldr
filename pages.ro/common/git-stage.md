# git stage

> Adăugați conținutul fișierului în zona de așteptare.
> Sinonim cu `git add`.
> Mai multe informaţii: <https://git-scm.com/docs/git-stage>

- Adăugați un fișier la index:

`git stage {{path/to/file}}`

- Adăugați toate fișierele (urmărite și neurmărite):

`git stage -A`

- Doar adăugați fișiere deja urmărite:

`git stage -u`

- De asemenea, adăugați fișiere ignorate:

`git stage -f`

- Interactiv etape părți ale fișierelor:

`git stage -p`

- Părți etalate interactiv ale unui fișier dat:

`git stage -p {{path/to/file}}`

- Etapa interactiv un fișier:

`git stage -i`
