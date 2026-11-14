# gh issue

> GitHub sorunlarını (issue) yönet.
> Daha fazla bilgi için: <https://cli.github.com/manual/gh_issue>.

- Belirli bir sorunu görüntüle:

`gh issue view {{sorun_numarası}}`

- Belirli bir sorunu varsayılan web tarayıcısında görüntüle:

`gh issue view {{sorun_numarası}} {{[-w|--web]}}`

- Varsayılan web tarayıcısında yeni bir sorun oluştur:

`gh issue {{[new|create]}} {{[-w|--web]}}`

- Son 10 `bug` etiketli sorunu listele:

`gh issue {{[ls|list]}} {{[-L|--limit]}} 10 {{[-l|--label]}} "bug"`

- Belirli bir kullanıcının açtığı kapalı sorunları listele:

`gh issue {{[ls|list]}} {{[-s|--state]}} closed {{[-A|--author]}} {{kullanıcı_adı}}`

- Belirli bir depoda, kullanıcıyla ilgili sorunların durumunu görüntüle:

`gh issue status {{[-R|--repo]}} {{sahip}}/{{depo}}`

- Belirli bir sorunu yeniden aç:

`gh issue reopen {{sorun_numarası}}`
