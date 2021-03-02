# git check-ref-format

> Girilen refname kabul edilebilir mi yoksa değil mi diye kontrol eder, ve eğer kabul edilemezse sıfır olmayan bir çıktı verir.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-check-ref-format>.

- Belirtilen refname'in biçimini kontrol et:

`git check-ref-format {{refs/head/refname}}`

- Son kontrol edilen dalın ismini göster:

`git check-ref-format --branch @{-1}`

- Bir refname dosyasını normalleştir:

`git check-ref-format --normalize {{refs/head/refname}}`
