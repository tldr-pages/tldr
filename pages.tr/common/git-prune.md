# git prune

> Nesne veritabanından erişilemeyen tüm nesneleri budamaya yarayan git komutu.
> Bu komut genelde doğrudan kullanılmasa da Git gc tarafından bir iç komut olarak kullanılmaktadır.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-prune>.

- Git prune tarafından silinebilecek nesneleri onları silmeden raporla:

`git prune --dry-run`

- Erişilemeyen nesneleri buda ve stdout'a budanan şeyleri görüntüle:

`git prune --verbose`

- Erişilemeyen nesneleri budarken ilerlemeyi göster:

`git prune --progress`
