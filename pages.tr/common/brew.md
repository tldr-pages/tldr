# brew

> Homebrew - macOS ve Linux için bir paket yöneticisi.
> `install` gibi bazı alt komutların kendi kullanım dokümantasyonu vardır.
> Daha fazla bilgi için: <https://docs.brew.sh/Manpage>.

- Bir formülün (formula) ya da cask'in en son kararlı sürümünü kur:

`brew install {{formül|cask}}`

- Kurulu tüm formülleri ve cask'leri listele:

`brew list`

- Kurulu bir formülü ya da cask'i yükselt (hiçbiri belirtilmezse kurulu tüm formüller/cask'ler yükseltilir):

`brew upgrade {{formül|cask}}`

- Homebrew'un ve tüm formül ve cask'lerin en yeni sürümünü Homebrew kaynak deposundan getir:

`brew update`

- Daha yeni bir sürümü bulunan formülleri ve cask'leri göster:

`brew outdated`

- Mevcut formülleri (yani paketleri) ve cask'leri (yani macOS'un yerel `.app` paketlerini) ara:

`brew search {{metin}}`

- Bir formül ya da cask hakkında bilgi göster (sürüm, kurulum yolu, bağımlılıklar vb.):

`brew info {{formül|cask}}`

- Yerel Homebrew kurulumunda olası sorunları kontrol et:

`brew doctor`
