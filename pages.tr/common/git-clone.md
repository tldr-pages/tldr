# git clone

> Varolan bir depoyu klonla.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-clone>.

- Varolan bir depoyu yeni bir dizine klonla (varsayılan dizin, deponun adıdır):

`git clone {{uzak_bağlantıdaki_depo}} {{yol/dizin}}`

- Varolan bir depo ve onun alt modüllerini klonla:

`git clone --recursive {{uzak_bağlantıdaki_depo}}`

- Varolan bir deponun yalnızca `.git` dizinini klonla:

`git clone {{[-n|--no-checkout]}} {{uzak_bağlantıdaki_depo}}`

- Yerel bir depoyu klonla:

`git clone {{[-l|--local]}} {{yol/yerel_depo}}`

- Sessizce klonla:

`git clone {{[-q|--quiet]}} {{uzak_bağlantıdaki_depo}}`

- Varsayılan daldaki yalnızca en yeni 10 commit'i çekerek varolan bir depoyu klonla (zaman tasarrufu açısından yararlıdır):

`git clone --depth 10 {{uzak_bağlantıdaki_depo}}`

- Yalnızca belirtilen bir dalı çekerek varolan bir depoyu klonla:

`git clone {{[-b|--branch]}} {{isim}} --single-branch {{uzak_bağlantıdaki_depo}}`

- Belirtilen bir SSH komutunu kullanarak varolan bir depoyu klonla:

`git clone {{[-c|--config]}} core.sshCommand="{{ssh -i yol/özel_ssh_anahtarı}}" {{uzak_bağlantıdaki_depo}}`
