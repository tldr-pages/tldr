# git revert

> Crea nuovi commit che invertano i risultati dei commit precedenti.
> Maggiori informazioni: <https://git-scm.com/docs/git-revert>.

- Inverti il commit più recente:

`git revert {{HEAD}}`

- Inverti il quintùltimo commit:

`git revert HEAD~{{4}}`

- Inverti più commit:

`git revert {{nome_ramo~5..nome_ramo~2}}`

- Inverti senza creare nuovi commit, ma modificando l'albero di lavoro:

`git revert -n {{0c01a9..9a1743}}`
