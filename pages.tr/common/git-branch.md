# git branch

> Dallar ile çalışmak için kullanılan ana Git komutu.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-branch>.

- Tüm dalları (yerel ve uzak bağlantıda olan) göster:

`git branch {{[-a|--all]}}`

- Mevcut dalın ismini göster:

`git branch --show-current`

- Mevcut commit'e dayanarak yeni bir dal oluştur:

`git branch {{dal_ismi}}`

- Belirtilen commit'e dayanarak yeni bir dal oluştur:

`git branch {{dal_ismi}} {{commit_değeri}}`

- Bir dalı yeniden adlandır:

`git branch {{[-m|--move]}} {{eski_dal_ismi}} {{yeni_dal_ismi}}`

- Yerel bir dalı sil:

`git branch {{[-d|--delete]}} {{dal_ismi}}`

- Uzaktaki bir dalı sil:

`git push {{uzak_bağlantı}} {{[-d|--delete]}} {{uzak_dal_ismi}}`
