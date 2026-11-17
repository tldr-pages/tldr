# git init

> Yeni bir yerel Git deposu başlat.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-init>.

- Yeni bir yerel depo başlat:

`git init`

- İlk dal için belirtilen ismi kullanarak bir depo başlat:

`git init {{[-b|--initial-branch]}} {{dal_ismi}}`

- Nesne verileri için SHA256 formatı kullanan bir depo başlat (Git versiyonu 2.29 veya üstü olmalıdır):

`git init --object-format sha256`

- SSH üzerinden uzak depo olarak kullanıma uygun, yalın bir depo başlat:

`git init --bare`
