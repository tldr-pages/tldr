# git commit

> Depoya dosya commit'le.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-commit>.

- Sahnelenmiş dosyaları belirtilen mesaj ile commit'le:

`git commit -m {{mesaj}}`

- Değişiklikleri otomatik olarak sahnele ve mesaj ile commit'le:

`git commit -a -m {{mesaj}}`

- Değerini değiştirecek şekilde son commit'i yeni sahnelenmiş değişiklikleri ekleyerek güncelle:

`git commit --amend`

- Yalnızca belirtilmiş (halihazırda sahnelenmiş) dosyaları commit'le:

`git commit {{örnek/dosya1}} {{örnek/dosya2}}`
