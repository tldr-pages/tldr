# git replace

> Nesnelerin yerini değiştirmek için referans oluştur, sırala ve sil.
> Daha fazla bilgi: <https://git-scm.com/docs/git-replace>.

- Öbür commit'lere dokunmadan bir commit'in başka bir commit ile yerini değiştir:

`git replace {{nesne}} {{yer_değiştirme}}`

- Belirtilen nesnede varolan yer değiştirme referanslarını sil:

`git replace --delete {{nesne}}`

- Bir nesnenin içeriğini etkileşimli olarak düzenle:

`git replace --edit {{nesne}}`
