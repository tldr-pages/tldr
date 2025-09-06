# git send-email

> Bir yama koleksiyonunu e-posta olarak gönder.
> Yamalar dosya, dizin veya sürüm listesi olarak tanımlanabilir.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-send-email>.

- Mevcut dizindeki son commit'i gönder:

`git send-email -1`

- Belirtilen commit'i gönder:

`git send-email -1 {{commit}}`

- Mevcut dizindeki belirtilen sayı kadar (örneğin 10) commit'i gönder:

`git send-email {{-10}}`

- Gönderilecek yama serisi için bir giriş e-posta mesajı gönder:

`git send-email -{{commits_sayı}} --compose`

- Gönderilecek her bir yama için e-posta mesajını görüntüle ve düzenle:

`git send-email -{{commits_sayı}} --annotate`
