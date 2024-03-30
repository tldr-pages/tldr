# git check-attr

> `gitattributes` içeriği görüntüleme aracı.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-check-attr>.

- Bir dosyadaki tüm atıfları kontrol et:

`git check-attr --all {{örnek/dosya}}`

- Bir dosyadaki belirtilmiş atıfın değerini kontrol et:

`git check-attr {{atıf}} {{örnek/dosya}}`

- Birden fazla dosyadaki belirtilmiş atıfın değerini kontrol et:

`git check-attr --all {{örnek/dosya1 örnek/dosya2 ...}}`

- Bir veya birden fazla dosyadaki belirtilmiş atıfın değerini kontrol et:

`git check-attr {{atıf}} {{örnek/dosya1 örnek/dosya2 ...}}`
