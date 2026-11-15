# git config

> Git depoları için yazılan kişisel konfigürasyon seçeneklerini yönet.
> Bu konfigürasyonlar lokal (mevcut depo için) veya evrensel (mevcut kullanıcı için) olabilir.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-config>.

- İsmini veya e-postanı evrensel olarak belirle (bu bilgi bir depoya commit'lemek için gereklidir ve tüm commit'lere eklenir):

`git config --global {{user.name|user.email}} "{{Adınız Soyadınız|eposta@ornek.com}}"`

- Lokal, evrensel veya sistem konfigürasyon kayıtlarını sırala ve bulundukları dosyayı göster:

`git config --{{local|global|system}} {{[-l|--list]}} --show-origin`

- Belirtilen bir konfigürasyon kaydının evrensel değerini belirle (bu örnekte bir takma ad):

`git config --global {{alias.unstage}} "reset HEAD --"`

- Belirtilen bir konfigürasyon kaydının değerini öğren:

`git config {{alias.unstage}}`

- Bir takma adı kullan:

`git {{unstage}}`

- Evrensel bir konfigürasyon kaydını varsayılan değerine geri al:

`git config --global --unset {{alias.unstage}}`

- Mevcut depodaki Git konfigürasyonunu (`.git/config`) varsayılan metin düzenleyici ile düzenle:

`git config {{[-e|--edit]}}`

- Evrensel Git konfigürasyonunu (varsayılan olarak `~/.gitconfig`, böyle bir dosya varsa `$XDG_CONFIG_HOME/git/config`) varsayılan metin düzenleyici ile düzenle:

`git config --global {{[-e|--edit]}}`
