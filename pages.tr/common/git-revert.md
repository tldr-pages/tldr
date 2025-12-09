# git revert

> Öncekilerin etkilerini geri alan yeni bir commit oluştur.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-revert>.

- En son commit'leri geri al:

`git revert {{@}}`

- En son 5. commit'i geri al:

`git revert HEAD~{{4}}`

- Birden fazla commit'i geri al:

`git revert {{dal_ismi~5..dal_ismi~2}}`

- Yeni commit'ler oluşturma, yalnızca çalışan ağacı değiştir:

`git revert -n {{0c01a9..9a1743}}`
