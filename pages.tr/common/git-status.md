# git status

> Bir git deposundaki dosyalara yapılan değişiklikleri göster.
> Mevcut commit'e kıyasla değiştirilen, eklenen ve silinen dosyaları sıralar.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-status>.

- İzlenmeyen ve henüz commit'e eklenmemiş değiştirilen dosyaları göster:

`git status`

- Çıktıyı özetlenmiş şekilde göster:

`git status {{[-s|--short]}}`

- Çıktıyı özetlenmiş şekilde dal bilgisiyle beraber göster:

`git status {{[-sb|--short --branch]}}`

- Sahnelenmiş dosyalardaki değişiklikleri göster (`git diff --cached` gibi):

`git status {{[-v|--verbose]}}`

- İzlenen tüm dosyalardaki değişiklikleri göster (`git diff HEAD` gibi):

`git status {{[-vv|--verbose --verbose]}}`

- Şu anda saklanmış (stash) girdilerin sayısını göster:

`git status --show-stash`

- Çıktıda izlenmeyen dosyaları gösterme:

`git status {{[-uno|--untracked-files=no]}}`
