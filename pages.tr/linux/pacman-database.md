# pacman --database

> Arch Linux paket veritabanında işlem yapmak için kullanılır.
> Kurulu paketlerin belirli özelliklerini değiştirir.
> Ayrıca bakınız: `pacman`.
> Daha fazla bilgi için: <https://manned.org/pacman.8>.

- Bir paketi dolaylı olarak kurulu olarak işaretle:

`sudo pacman -D --asdeps {{paket}}`

- Bir paketi açıkça kurulu olarak işaretle:

`sudo pacman -D --asexplicit {{paket}}`

- Tüm paket bağımlılıklarının kurulu olduğunu kontrol et:

`pacman -Dk`

- Senkronizasyon veritabanını kontrol et ve indirilebilir paketlerin tüm belirtilen bağımlılıklarının mevcut olduğundan emin ol:

`pacman -Dkk`

- Sessiz modda kontrol et ve görüntüle (sadece hata mesajları gösterilir):

`pacman -Dkq`

- Yardımı görüntüle:

`pacman -Dh`
