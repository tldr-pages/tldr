# git format-patch

> `.patch` dosyaları oluştur. Commit'leri e-posta olarak gönderirken işe yarar.
> Ayrıca benzer bir komut olan `git am` sayfasına bakılması önerilir.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-format-patch>.

- Gönderilmemiş tüm commit'ler için otomatik olarak adlandırılan bir `.patch` dosyası oluştur:

`git format-patch {{origin}}`

- stdout'daki belirtilen 2 revizyon arasındaki tüm commit'ler için bir `.patch` dosyası oluştur:

`git format-patch {{revizyon_1}}..{{revizyon_2}}`

- Son 3 commit için bit `.patch` dosyası oluştur:

`git format-patch -{{3}}`
