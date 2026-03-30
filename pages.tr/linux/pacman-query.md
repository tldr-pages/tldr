# pacman --query

> Arch Linux paket yönetim aracı.
> Ayrıca bakınız: `pacman`.
> Daha fazla bilgi için: <https://manned.org/pacman.8>.

- Yüklenmiş paket ve sürümleri sırala:

`pacman -Q`

- Sadece özellikle indirilmiş paket ve sürümleri sırala:

`pacman -Qe`

- Hangi paketin belirtilen dosyaya sahip olduğunu bul:

`pacman -Qo {{dosya_ismi}}`

- İndirilmiş bir pakete dair bilgiyi görüntüle:

`pacman -Qi {{paket_ismi}}`

- Bir paketin içerdiği dosyaları sırala:

`pacman -Ql {{paket_ismi}}`

- Yetim (başka bir pakete bağlılık olarak indirilmiş ancak herhangi bir paket tarafından gerektirilmeyen) paketleri sırala:

`pacman -Qdtq`

- Mevcut depolarda bulunmayan, indirilmiş paketleri sırala:

`pacman -Qm`

- Miadı dolmuş paketleri sırala:

`pacman -Qu`
