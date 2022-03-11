# git check-ref-format

> Girilen referans isminin kabul edilebilir olup olmadığını kontrol eder, ve eğer kabul edilemezse sıfır olmayan bir çıktı verir.
> Daha fazla bilgi: <https://git-scm.com/docs/git-check-ref-format>.

- Belirtilen referans ismini biçimini kontrol et:

`git check-ref-format {{refs/head/referans_ismi}}`

- Son kontrol edilen dalın ismini göster:

`git check-ref-format --branch @{-1}`

- Bir referans ismi dosyasını normalleştir:

`git check-ref-format --normalize {{refs/head/referans_ismi}}`
