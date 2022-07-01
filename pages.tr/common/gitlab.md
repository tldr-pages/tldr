# gitlab

> GitLab API'si için Ruby sarıcı ve CLI aracı.
> `gitlab ctl` gibi bazı alt komutların kendi kullanım kılavuzları vardır.
> Daha fazla bilgi: <https://narkoz.github.io/gitlab/>.

- Yeni bir proje oluştur:

`gitlab create_project {{proje_ismi}}`

- Belirtilen commit ile ilgili bilgi al:

`gitlab commit {{proje_ismi}} {{commit_değeri}}`

- Bit CI pipeline'ındaki işler ile ilgili bilgi al:

`gitlab pipeline_jobs {{proje_ismi}} {{pipeline_id'si}}`

- Belirtilen CI işini başlat:

`gitlab job_play {{proje_ismi}} {{iş_id'si}}`
