# git flow

> Üst seviye depo işlemleri için Git uzantı koleksiyonu.
> Daha fazla bilgi için: <https://github.com/nvie/gitflow>.

- Varolan bir git deposu içinde başlat:

`git flow init`

- `develop` tabanlı bir özellik dalı üzerinde geliştirmeye başla:

`git flow feature start {{özellik}}`

- Özellik dalı üzerinde geliştirmeyi bitir, `develop` dalı ile birleştir ve dalı sil:

`git flow feature finish {{özellik}}`

- Özelliği uzak sunucuya yayınla:

`git flow feature publish {{özellik}}`

- Başka bir kullanıcı tarafından yayınlanan özelliği al:

`git flow feature pull origin {{özellik}}`
