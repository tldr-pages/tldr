# pacman-key

> pacman'ın anahtar zincirini yönetmek için kullanılan GnuPG sarmalayıcı betiği.
> Ayrıca bakınız: `pacman`.
> Daha fazla bilgi için: <https://manned.org/pacman-key>.

- `pacman` anahtar zincirini başlat:

`sudo pacman-key --init`

- Varsayılan Arch Linux anahtarlarını ekle:

`sudo pacman-key --populate`

- Açık anahtar zincirindeki anahtarları listele:

`pacman-key {{[-l|--list-keys]}}`

- Belirtilen anahtarları ekle:

`sudo pacman-key {{[-a|--add]}} {{yol/anahtar_dosyasi.gpg}}`

- Bir anahtarı anahtar sunucusundan al:

`sudo pacman-key {{[-r|--recv-keys]}} "{{uid|isim|email}}"`

- Belirli bir anahtarın parmak izini yazdır:

`pacman-key {{[-f|--finger]}} "{{uid|isim|email}}"`

- İçe aktarılan anahtarı yerel olarak imzala:

`sudo pacman-key --lsign-key "{{uid|isim|email}}"`

- Belirli bir anahtarı kaldır:

`sudo pacman-key {{[-d|--delete]}} "{{uid|isim|email}}"`
