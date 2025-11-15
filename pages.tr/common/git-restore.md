# git restore

> Çalışan ağaç dosyalarını onar. Git sürümü 2.23+ olmalıdır.
> `git checkout` ve `git reset` komutlarına da ayrıca bakılması tavsiye edilir.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-restore>.

- Sahnelenmemiş bir dosyayı mevcut commit'in sürümüne kavuştur:

`git restore {{dosya/konumu}}`

- Sahnelenmemiş bir dosyayı belirtilen commit'in sürümüne kavuştur:

`git restore {{[-s|--source]}} {{commit}} {{dosya/konumu}}`

- İzlenen dosyalardaki sahnelenmemiş tüm değişiklikleri iptal et:

`git restore :/`

- Bir dosyayı sahnelenmemiş hale getir:

`git restore {{[-S|--staged]}} {{dosya/konumu}}`

- Tüm dosyaları sahnelenmemiş hale getir:

`git restore {{[-S|--staged]}} :/`

- Dosyalara yapılan sahnelenmiş veya sahnelenmemiş tüm değişiklikleri iptal et:

`git restore {{[-W|--worktree]}} {{[-S|--staged]}} :/`

- Onarılacak dosya parçalarını etkileşimli olarak seç:

`git restore {{[-p|--patch]}}`
