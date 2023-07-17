# pacman --sync

> Arch Linux paket yönetim aracı.
> Ayrıca bakınız: `pacman`.
> Daha fazla bilgi için: <https://man.archlinux.org/man/pacman.8>.

- Yeni bir paket indir::

`sudo pacman --sync {{paket_ismi}}`

- Tüm paketleri senkronize et ve güncelle (bahsi geçen paketleri güncellemeden indirmek için `--downloadonly` eki gereklidir):

`sudo pacman --sync --refresh --sysupgrade`

- Tüm paketleri güncelle ve telkin olmaksızın yeni bir tane indir:

`sudo pacman --sync --refresh --sysupgrade --noconfirm {{paket_ismi}}`

- Paket veritabanını girilen ifade ile arat:

`pacman --sync --search "{{arama_şablonu}}"`

- Bir paket hakkında bilgi görüntüle:

`pacman --sync --info {{paket_ismi}}`

- Bir paket güncellemesi sırasında çakışan dosyaların üstüne yaz:

`sudo pacman --sync --refresh --sysupgrade --overwrite {{örnek_dosya}}`

- Tüm paketleri senkronize et ve güncelle, ancak belli bir paketi yoksay:

`sudo pacman --sync --refresh --sysupgrade --ignore {{paket_ismi}}`

- Kullanılmayan paket ve kullanılmamış depoları çerezlerden sil (tüm paketlerin çerezlerini temizlemek için `--clean` eki iki kez kullanılmalıdır):

`sudo pacman --sync --clean`
