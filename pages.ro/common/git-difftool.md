# git difftool

> Afișați modificările fișierelor utilizând instrumente diff externe. Acceptă aceleași opțiuni și argumente ca `git dif`.
> A se vedea, de asemenea,: `git dif`.
> Mai multe informaţii: <https://git-scm.com/docs/git-difftool>

- Lista de instrumente dif disponibile:

`git difftool --tool-help`

- Setați instrumentul diff implicit pentru a contopi:

`git config --global diff.tool "{{meld}}"`

- Utilizați instrumentul diff implicit pentru a afișa modificările pe etape:

`git difftool --staged`

- Utilizați un instrument specific (opendiff) pentru a afișa modificările de la un anumit angajament:

`git difftool --tool={{opendiff}} {{commit}}`
