# git am

> Yama dosyalarını uygula ve commit oluştur. E-posta ile commit alırken faydalıdır.
> Ayrıca bakınız: `git format-patch`.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-am>.

- Yerel bir yama dosyasındaki değişiklikleri uygula ve commit oluştur:

`git am {{örnek/yama.patch}}`

- Uzak bir yama dosyasındaki değişiklikleri uygula ve commit oluştur:

`curl {{[-L|--location]}} {{https://example.com/yama.patch}} | git am`

- Yama dosyası uygulama işlemini durdur:

`git am --abort`

- Yama dosyasının uygulanabilen kısmını uygula, uygulanamayan parçaları `.rej` dosyalarına kaydet:

`git am --reject {{örnek/yama.patch}}`
