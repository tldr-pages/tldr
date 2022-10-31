# pacman --query

> Arch Linux paket yönetim aracı.
> Daha fazla bilgi için: <https://man.archlinux.org/man/pacman.8>.

- Yüklenmiş paket ve sürümleri sırala:

`pacman --query`

- Sadece özellikle indirilmiş paket ve sürümleri sırala:

`pacman --query --explicit`

- Hangi paketin belirtilen dosyaya sahip olduğunu bul:

`pacman --query --owns {{dosya_ismi}}`

- İndirilmiş bir pakete dair bilgiyi görüntüle:

`pacman --query --info {{paket_ismi}}`

- Bir paketin içerdiği dosyaları sırala:

`pacman --query --list {{paket_ismi}}`

- Yetim (başka bir pakete bağlılık olarak indirilmiş ancak herhangi bir paket tarafından gerektirilmeyen) paketleri sırala:

`pacman --query --unrequired --deps --quiet`

- Mevcut depolarda bulunmayan, indirilmiş paketleri sırala:

`pacman --query --foreign`

- Miadı dolmuş paketleri sırala:

`pacman --query --upgrades`
