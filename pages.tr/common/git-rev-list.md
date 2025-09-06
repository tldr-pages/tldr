# git rev-list

> Değişiklikleri (commit'leri) ters kronolojik sırada sırala.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-rev-list>.

- Mevcut daldaki tüm commit'leri sırala:

`git rev-list {{HEAD}}`

- Belirtilen daldaki belirtilen tarihten daha yakın olan commit'leri sırala:

`git rev-list --since={{'2019-12-01 00:00:00'}} {{dal_ismi}}`

- Belirtilen commit'deki tüm birleştirme commit'lerini sırala:

`git rev-list --merges {{commit}}`

- Belirtilen etiketten itibaren olan commit sayılarını çıkar:

`git rev-list {{tag_name}}..HEAD --count`
