# git ls-tree

> Bir ağaç nesnesinin içeriklerini sırala.
> Daha fazla bilgi: <https://git-scm.com/docs/git-ls-tree>.

- Bir daldaki ağacın içeriklerini sırala:

`git ls-tree {{dal_name}}`

- Bir commit üstündeki ağacın içeriklerini alt ağaçlara ayırarak sırala:

`git ls-tree -r {{commit_değeri}}`

- Bir commit üstündeki ağacın yalnızca dosya isimlerini göster:

`git ls-tree --name-only {{commit_değeri}}`
