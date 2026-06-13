# git am

> Yama dosyalarını uygula. E-posta ile commit alırken faydalıdır.
> Ayrıca bakınız: `git format-patch`.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-am>.

- Bir yama dosyasını uygula:

`git am {{örnek/yama.patch}}`

- Yama dosyası uygulama işlemini durdur:

`git am --abort`

- Mümkün olacak kadar yama dosyasını uygula ve bu dosyaların uygulanamayan parçalarını bahsi geçen dosyaları reddetmek için kaydet:

`git am --reject {{örnek/yama.patch}}`
