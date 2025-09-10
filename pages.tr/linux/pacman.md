# pacman

> Arch Linux paket yönetim aracı.
> Ayrıca bakınız: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Daha fazla bilgi için: <https://manned.org/pacman.8>.

- Tüm paketleri senkronize et ve güncelle:

`sudo pacman -Syu`

- Yeni bir paket indir:

`sudo pacman -S {{paket_ismi}}`

- Bir paket ve bağlılıklarını sil:

`sudo pacman -Rs {{paket_ismi}}`

- Paket veritabanında `regex` veya anahter kelime ile ara:

`pacman -Ss "{{search_pattern}}"`

- Belirli bir dosyayı içeren paketleri veritabanında ara:

`pacman -F "{{file_name}}"`

- Sadece özellikle belirtilen paket ve sürümleri sırala:

`pacman -Qe`

- Orphan paketleri listele (bağımlılık olarak kurulmuş ama aslında hiçbir paket tarafından gerekmeyenler):

`pacman -Qtdq`

- Paket çerezlerini boş alan açmak için temizle:

`sudo pacman -Scc`
