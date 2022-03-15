# git branch

> Dallar ile çalışmak için kullanılan ana Git komutu.
> Daha fazla bilgi: <https://git-scm.com/docs/git-branch>.

- Yerel dalları göster. Mevctu dal `*` ile vurgulanır:

`git branch`

- Tüm dalları (yerel ve uzak bağlantıda olan) göster:

`git branch -a`

- Mevcut dalın ismini göster:

`git branch --show-current`

- Mevcut commit'e dayanarak yeni bir dal oluştur:

`git branch {{dal_ismi}}`

- Belirtilen commit'e dayanarak yeni bir dal oluştur:

`git branch {{dal_ismi}} {{commit_değeri}}`

- Bir dalı yeniden adlandır:

`git branch -m {{eski_dal_ismi}} {{yeni_dal_ismi}}`

- Yerel bir dalı sil:

`git branch -d {{dal_ismi}}`

- Uzaktaki bir dalı sil:

`git push {{uzak_bağlantı}} --delete {{uzak_dal_ismi}}`
