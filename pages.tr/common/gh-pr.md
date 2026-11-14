# gh pr

> GitHub çekme isteklerini (pull request) yönet.
> `create` gibi bazı alt komutların kendi kullanım dokümantasyonu vardır.
> Daha fazla bilgi için: <https://cli.github.com/manual/gh_pr>.

- Çekme isteği oluştur:

`gh pr {{[new|create]}}`

- Belirli bir çekme isteğine yerelde geç:

`gh {{[co|pr checkout]}} {{pr_numarası|url|dal}}`

- Mevcut dal için çekme isteğinde yapılan değişiklikleri görüntüle:

`gh pr diff`

- Mevcut dal için çekme isteğini onayla:

`gh pr review {{[-a|--approve]}}`

- Mevcut dalla ilişkili çekme isteğini etkileşimli olarak birleştir:

`gh pr merge`

- Bir çekme isteğini etkileşimli olarak düzenle:

`gh pr edit`

- Bir çekme isteğinin taban dalını düzenle:

`gh pr edit {{[-B|--base]}} {{dal_ismi}}`

- Mevcut deponun çekme isteklerinin durumunu kontrol et:

`gh pr status`
