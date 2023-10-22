# pacman --remove

> Arch Linux paket yönetim aracı.
> Ayrıca bakınız: `pacman`.
> Daha fazla bilgi için: <https://man.archlinux.org/man/pacman.8>.

- Bir paket ve bağlılıklarını sil:

`sudo pacman --remove --recursive {{paket_ismi}}`

- Bir paketi ve onun hem bağlılıklarını, hem de konfigürasyon dosyalarını sil:

`sudo pacman --remove --recursive --nosave {{paket_ismi}}`

- Bir paketi telkin olmaksızın sil:

`sudo pacman --remove --noconfirm {{paket_ismi}}`

- Yetim (başka bir pakete bağlılık olarak indirilmiş ancak herhangi bir paket tarafından gerektirilmeyen) paketleri sil:

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Bir paketi ve ona bağlı olan tüm öbür paketleri sil:

`sudo pacman --remove --cascade {{paket_ismi}}`

- (Bir paketin silinme durumunda) Etkilenecek paketleri (silmeden) listele:

`pacman --remove --print {{paket_ismi}}`

- Bu alt komut için yardım göster:

`pacman --remove --help`
