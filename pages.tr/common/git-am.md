# git am

> Yama dosyalarını uygula. E-posta ile commit alırken faydalıdır.
> Ayrıca yama dosyalarının üretilmesine yarayan `git format-patch` sayfasına bakılması önerilir.
> Daha fazla bilgi: <https://git-scm.com/docs/git-am>.

- Bir yama dosyasını uygula:

`git am {{örnek/yama.patch}}`

- Yama dosyası uygulama işlemini durdur:

`git am --abort`

- Mümkün olacak kadar yama dosyasını uygula ve bu dosyaların uygulanamayan parçalarını bahsi geçen dosyaları reddetmek için kaydet:

`git am --reject {{örnek/yama.patch}}`
