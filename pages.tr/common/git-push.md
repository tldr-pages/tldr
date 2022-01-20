# git push

> Commit'leri uzak depoya yolla.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-push>.

- Mevcut daldaki yerel değişiklikleri onun uzak eşine gönder:

`git push`

- Belirtilen daldaki yerel değişiklikleri onun uzak eşine gönder:

`git push {{uzak_bağlantı}} {{yerel_dal}}`

- Mevcut dalı bir uzak dal ismi ayarlayarak uzak depoda yayınla:

`git push {{uzak_bağlantı}} -u {{uzak_dal}}`

- Yerel dallardaki tüm değişiklikleri onların belirtilen uzak depodaki uzak eşlerine gönder:

`git push --all {{uzak_bağlantı}}`

- Uzak depodaki bir dalı sil:

`git push {{uzak_bağlantı}} --delete {{uzak_dal}}`

- Yerel eşi olmayan uzak dalları sil:

`git push --prune {{uzak_bağlantı}}`

- Daha yzak depoda olmayan etiketleri yayınla:

`git push --tags`
