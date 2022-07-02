# git update-ref

> Git referanslarını yaratmak, güncellemek ve silmeye yarayan bir Git komutu.
> Daha fazla bilgi: <https://git-scm.com/docs/git-update-ref>.

- Bir referansı sil (ilk commit'i hafifçe sıfırlamaya yarar):

`git update-ref -d {{HEAD}}`

- Referansı bir mesaj ile güncelle:

`git update-ref -m {{mesaj}} {{HEAD}} {{4e95e05}}`
