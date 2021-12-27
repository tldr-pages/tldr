# git stage

> Dosya içeriklerini sahnelenen alana ekle.
> `git add` komutunun eş anlamlısı.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-stage>.

- İndekse bir dosya ekle:

`git stage {{dosya/konumu}}`

- Tüm dosyaları (izlenen ve izlenmeyen) ekle:

`git stage -A`

- Yalnızca halihazırda izlenen dosyaları ekle:

`git stage -u`

- Görmezden gelinen dosyaları da ekle:

`git stage -f`

- Dosyaların parçalarını etkileşimli şekilde sahnele:

`git stage -p`

- Belirtilen dosyanın parçalarını etkileşimli şekilde sahnele:

`git stage -p {{dosya/konumu}}`

- Bir dosyayı etkileşimli şekilde sahnele:

`git stage -i`
