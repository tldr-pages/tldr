# git stage

> Değiştirilmiş dosyaları indekse ekle.
> `git add` takma adı.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-stage>.

- İndekse bir dosya ekle:

`git stage {{örnek/dosya}}`

- Tüm (izlenen veya izlenmeyen) dosyaları ekle:

`git stage -A`

- Yalnızca izlenen dosyaları ekle:

`git stage -u`

- Yoksayılan dosyaları dahi ekle:

`git stage -f`

- Dosyaların parçalarını etkileşimli olarak sahnele:

`git stage -p`

- Belirtilen dosyaların parçalarını etkileşimli olarak sahnele:

`git stage -p {{örnek/dosya}}`

- Bir dosyayı etkileşimli olarak sahnele:

`git stage -i`
