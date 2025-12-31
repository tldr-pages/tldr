# pacman --upgrade

> Arch Linux paket yöneticisi aracı.
> Ayrıca bakınız: `pacman`.
> Daha fazla bilgi için: <https://manned.org/pacman.8>.

- Dosyalardan bir veya daha fazla paket kur:

`sudo pacman -U {{yol/paket1.pkg.tar.zst yol/paket2.pkg.tar.zst ...}}`

- Paketi sorunsuz kur (onay istemeden):

`sudo pacman -U --noconfirm {{yol/paket.pkg.tar.zst}}`

- Paket kurulumu sırasında çakışan dosyaların üzerine yaz:

`sudo pacman -U --overwrite {{yol/dosya}} {{yol/paket.pkg.tar.zst}}`

- Paket kurulumunda bağımlılık sürüm kontrollerini atla:

`sudo pacman -Ud {{yol/paket.pkg.tar.zst}}`

- Yükseltme sırasında etkilenecek paketleri getir ve yazdır (paketleri kurmaz):

`pacman -Up {{yol/paket.pkg.tar.zst}}`

- Yardımı görüntüle:

`pacman -Uh`
