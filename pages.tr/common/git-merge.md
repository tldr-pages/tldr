# git merge

> Dalları birleştir.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-merge>.

- Mevcut dal ile belirtilen dalları birleştir:

`git merge {{dal_ismi1 dal_ismi2 ...}}`

- Birleştirme mesajını düzenle:

`git merge {{[-e|--edit]}} {{dal_ismi}}`

- Bir dalı birleştir ve birleştirme commit'i oluştur:

`git merge --no-ff {{dal_ismi}}`

- Bir dalı birleştirmenin sonucunu commit oluşturmadan sahnele:

`git merge --squash {{dal_ismi}}`

- Çakışma durumunda birleştirme işlemini iptal et:

`git merge --abort`

- Belirli bir stratejiyi kullanarak birleştir:

`git merge {{[-s|--strategy]}} {{strateji}} {{[-X|--strategy-option]}} {{strateji_seçeneği}} {{dal_ismi}}`
