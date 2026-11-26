# git add

> Değiştirilmiş dosyaları indekse ekle.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-add>.

- İndekse bir dosya ekle:

`git add {{yol/dosya}}`

- Dosyaların parçalarını etkileşimli olarak sahnele:

`git add {{[-p|--patch]}}`

- Tüm (izlenen veya izlenmeyen) dosyaları ekle:

`git add {{[-A|--all]}}`

- Geçerli klasörden başlayarak tüm dosyaları özyinelemeli olarak ekle:

`git add .`

- Yalnızca izlenen dosyaları ekle:

`git add {{[-u|--update]}}`

- Yoksayılan bir dosyayı ekle:

`git add {{[-f|--force]}} {{yol/dosya}}`

- Belirtilen dosyanın parçalarını etkileşimli olarak sahnele:

`git add {{[-p|--patch]}} {{yol/dosya}}`

- Bir dosyayı etkileşimli olarak sahnele:

`git add {{[-i|--interactive]}}`
