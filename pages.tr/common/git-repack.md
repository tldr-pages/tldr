# git repack

> Bir Git deposundaki paketlenmemiş nesneleri paketle.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-repack>.

- Mevcut dizindeki paketlenmemiş nesneleri paketle:

`git repack`

- Paketlemeden sonra gereksiz nesneleri sil:

`git repack -d`

- Tüm nesneleri tek bir pakette yeniden paketle:

`git repack -a`

- Yeniden paketlemeyi yalnızca yerel nesnelerle sınırla:

`git repack -l`
