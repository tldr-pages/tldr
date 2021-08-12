# git cat-file

> Furnizați informații despre conținut sau tip și dimensiune pentru obiectele din depozitul Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-cat-file>

- Obțineți [s] ize a HEAD comite în octeți:

`git cat-file -s HEAD`

- Obțineți [t] ype (blob, copac, comitere, etichetă) unui obiect Git dat:

`git cat-file -t {{8c442dc3}}`

- Pretty- [p] rint conținutul unui anumit obiect Git bazat pe tipul său:

`git cat-file -p {{HEAD~2}}`
