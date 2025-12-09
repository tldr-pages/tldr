# git show-branch

> Dalları ve içerdikleri commit'leri göster.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-show-branch>.

- Bir daldaki son commit'lerin bir özetini göster:

`git show-branch {{dal_ismi|referans|commit}}`

- Çeşitli commit veya daldaki commit'lerin geçmişini karşılaştır:

`git show-branch {{dal_ismi|referans|commit}}`

- Tüm uzak takip dallarını karşılaştır:

`git show-branch --remotes`

- Hem yerel, hem de uzak takip dallarını karşılaştır:

`git show-branch --all`

- Tüm dallardaki son commit'leri sırala:

`git show-branch --all --list`

- Belirtilen dalı mevcut dal ile karşılaştır:

`git show-branch --current {{commit|dal_ismi|referans}}`

- Bağlı isim yerine commit ismini görüntüle:

`git show-branch --sha1-name --current {{current|dal_ismi|referans}}`

- Commit'lerin ortak atasından sonraki commit'leri belirtilen sayı kadar görüntüle:

`git show-branch --more {{5}} {{commit|dal_ismi|referans}} {{commit|dal_ismi|referans}} {{...}}`
