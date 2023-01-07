# git reset

> Mevcut Git HEAD'ini belirtilen duruma sıfırlayarak commit'leri veya değişiklikleri geri al.
> Eğer bir konum verildiye o konumdaki değişiklikler "geri alınır"; eğer bir commit değeri veya dal verildiyse o commit/dal "geri alınır".
> Daha fazla bilgi için: <https://git-scm.com/docs/git-reset>.

- Her şeyi geri al:

`git reset`

- Belirtilen dosya(lar)ı geri al:

`git reset {{dosya(ların)/konumu}}`

- Bir dosyanın kısımlarını geri al::

`git reset -p {{dosya/konumu}}`

- Son commit'i, dosya sisteminde yapılan değişiklikleri geri almadan geri al:

`git reset HEAD~`

- Son iki commit'i onların indeks'e yaptığı değişiklikleri ekleyerek geri al:

`git reset --soft HEAD~2`

- Commit'lenmemiş değişiklikleri sahnelenip sahnelenmediklerine bakmaksızın iptal et (sadece sahnelenmemiş değişiklikleri iptal etmek için `git checkout` kullanılır):

`git reset --hard`

- Depoyu belirtilen commit'e o zamana kadar yapılan değişiklikleri iptal ederek sıfırla:

`git reset --hard {{commit}}`
