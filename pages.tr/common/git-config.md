# git config

> Git depoları için yazılan kişisel konfigürasyon seçeneklerini yönet.
> Bu konfigürasyonlar lokal (mevcut depo için) veya evrensel (mevcut kullanıcı için) olabilir.
> Daha fazla bilgi: <https://git-scm.com/docs/git-config>.

- Yalnızca (mevcut depodaki `.git/config`'de saklanan) yerel konfigürasyon kayıtlarını sırala:

`git config --list --local`

- Yalnızca (bilgisayardaki `~/.gitconfig`'de saklanan) evrensel konfigürasyon kayıtlarını sırala:

`git config --list --global`

- Yerel veya evrensel olarak tanımlanan tüm konfigürasyon kayıtlarını sırala:

`git config --list`

- Belirtilen bir konfigürasyon kaydının değerini öğren:

`git config alias.unstage`

- Belirtilen bir konfigürasyon kaydının evrensel değerini belirle:

`git config --global alias.unstage "reset HEAD --"`

- Evrensel bir konfigürasyon kaydını varsayılan değerine geri al:

`git config --global --unset alias.unstage`

- Mevcut depodaki Git konfigürasyonunu varsayılan metin düzenleyici ile düzenle:

`git config --edit`

- Evrensel Git konfigürasyonunu varsayılan metin düzenleyici ile düzenle:

`git config --global --edit`
