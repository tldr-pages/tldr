# git restore

> Çalışan ağaç dosyalarını onar. Git sürümü 2.23+ olmalıdır.
> Ayrıca bakınız: `git checkout`, `git reset`.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-restore>.

- Sahnelenmemiş bir dosyayı mevcut commit'in sürümüne kavuştur:

`git restore {{yol/dosya}}`

- Sahnelenmemiş bir dosyayı belirtilen commit'in sürümüne kavuştur:

`git restore {{[-s|--source]}} {{commit}} {{yol/dosya}}`

- İzlenen dosyalardaki sahnelenmemiş tüm değişiklikleri iptal et:

`git restore :/`

- Bir dosyayı sahnelenmemiş hale getir:

`git restore {{[-S|--staged]}} {{yol/dosya}}`

- Tüm dosyaları sahnelenmemiş hale getir:

`git restore {{[-S|--staged]}} :/`

- Dosyalara yapılan sahnelenmiş veya sahnelenmemiş tüm değişiklikleri iptal et:

`git restore {{[-W|--worktree]}} {{[-S|--staged]}} :/`

- Onarılacak dosya parçalarını etkileşimli olarak seç:

`git restore {{[-p|--patch]}}`
