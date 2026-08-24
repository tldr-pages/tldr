# pacman --remove

> Arch Linux paket yönetim aracı.
> Ayrıca bakınız: `pacman`.
> Daha fazla bilgi için: <https://manned.org/pacman.8>.

- Bir paket ve bağlılıklarını sil:

`sudo pacman -Rs {{paket_ismi}}`

- Bir paketi ve onun hem bağlılıklarını, hem de konfigürasyon dosyalarını sil:

`sudo pacman -Rsn {{paket_ismi}}`

- Bir paketi telkin olmaksızın sil:

`sudo pacman -R --noconfirm {{paket_ismi}}`

- Yetim (başka bir pakete bağlılık olarak indirilmiş ancak herhangi bir paket tarafından gerektirilmeyen) paketleri sil:

`sudo pacman -Rsn $(pacman -Qdtq)`

- Bir paketi ve ona bağlı olan tüm öbür paketleri sil:

`sudo pacman -Rc {{paket_ismi}}`

- (Bir paketin silinme durumunda) Etkilenecek paketleri (silmeden) listele:

`pacman -Rp {{paket_ismi}}`

- Bu alt komut için yardım göster:

`pacman -Rh`
