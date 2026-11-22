# git ignore

> `.gitignore` dosyalarını göster/güncelle.
> `git-extras` paketinin bir parçasıdır.
> Ayrıca bakınız: `git ignore-io`.
> Daha fazla bilgi için: <https://github.com/tj/git-extras/blob/main/Commands.md#git-ignore>.

- Tüm global ve yerel `.gitignore` dosyalarının içeriğini göster:

`git ignore`

- Dosya(lar)ı özel olarak yoksay, `.git/info/exclude` dosyasını güncelle:

`git ignore {{dosya_deseni}} {{[-p|--private]}}`

- Dosya(lar)ı yerel olarak yoksay, yerel `.gitignore` dosyasını güncelle:

`git ignore {{dosya_deseni}}`

- Dosya(lar)ı global olarak yoksay, global `.gitignore` dosyasını güncelle:

`git ignore {{dosya_deseni}} {{[-g|--global]}}`
