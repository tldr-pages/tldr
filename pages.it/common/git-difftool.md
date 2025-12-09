# git difftool

> Mostra le modifiche ai file tracciati usando uno strumento Diff esterno. Accetta le stesse opzioni e argomenti di Git diff.
> Maggiori informazioni: <https://git-scm.com/docs/git-difftool>.

- Elenca gli strumenti Diff disponibili:

`git difftool --tool-help`

- Imposta meld come strumento Diff predefinito:

`git config --global diff.tool "{{meld}}"`

- Usa lo strumento Diff predefinito per mostrare le modifiche nell'area di stage:

`git difftool --staged`

- Uso uno specifico strumento Diff (opendiff) per mostrare le modifiche a partire da un dato commit:

`git difftool --tool={{opendiff}} {{commit}}`
