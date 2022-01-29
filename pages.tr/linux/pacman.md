# pacman

> Arch Linux paket yönetim aracı.
> Daha fazla bilgi: <https://man.archlinux.org/man/pacman.8>.

- Tüm paketleri senkronize et ve güncelle:

`sudo pacman --sync --refresh --sysupgrade`

- Yeni bir paket indir:

`sudo pacman --sync {{paket_ismi}}`

- Bir paket ve bağlılıklarını sil:

`sudo pacman --remove --recursive {{paket_ismi}}`

- Paket veritabanını girilen ifade ile arat:

`pacman --sync --search "{{arama_şablonu}}"`

- İndirilmiş paket ve sürümleri sırala:

`pacman --query`

- Sadece özellikle belirtilen paket ve sürümleri sırala:

`pacman --query --explicit`

- Hangi paketin belirtilen dosyaya sahip olduğunu bul:

`pacman --query --owns {{dosya_ismi}}`

- Paket çerezlerini boş alan açmak için temizle:

`sudo pacman --sync --clean --clean`
