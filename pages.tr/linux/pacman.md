# pacman

> Arch Linux paket yönetim aracı.
> Ayrıca bakınız: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Daha fazla bilgi için: <https://man.archlinux.org/man/pacman.8>.

- Tüm paketleri senkronize et ve güncelle:

`sudo pacman -Syu`

- Yeni bir paket indir:

`sudo pacman -S {{paket_ismi}}`

- Bir paket ve bağlılıklarını sil:

`sudo pacman -Rs {{paket_ismi}}`

- Paket veritabanını girilen ifade ile arat:

`pacman -Ss "{{arama_şablonu}}"`

- İndirilmiş paket ve sürümleri sırala:

`pacman -Q`

- Sadece özellikle belirtilen paket ve sürümleri sırala:

`pacman -Qe`

- Hangi paketin belirtilen dosyaya sahip olduğunu bul:

`pacman -Qo {{dosya_ismi}}`

- Paket çerezlerini boş alan açmak için temizle:

`sudo pacman -Scc`
