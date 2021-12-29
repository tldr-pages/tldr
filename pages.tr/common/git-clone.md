# git clone

> Varolan bir dizini klonla.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-clone>.

- Varolan bir depoyu klonla:

`git clone {{uzak_bağlantıdaki_depo}}`

- Varolan bir depoyu velirtilen dizine klonla:

`git clone {{uzak_bağlantıdaki_depo}} {{örnek/dizin}}`

- Varolan bir depo ve onun alt modüllerini klonla:

`git clone --recursive {{uzak_bağlantıdaki_depo}}`

- Yerel bir depoyu klonla:

`git clone -l {{örnek/yerel/depo}}`

- Sessizce klonla:

`git clone -q {{uzak_bağlantıdaki_depo}}`

- Yalnızca en yeni 10 commit'i çekerek varolan bir depoyu klonla (zaman tasarrufu açısından yararlıdır):

`git clone --depth {{10}} {{uzak_bağlantıdaki_depo}}`

- Yalnızca belirtilen bir dalı çekerek varolan bir depoyu klonla:

`git clone --branch {{isim}} --single-branch {{uzak_bağlantıdaki_depo}}`
