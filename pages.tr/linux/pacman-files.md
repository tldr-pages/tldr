# pacman --files

> Arch Linux paket yöneticisi aracı.
> Ayrıca bakınız: `pacman`, `pkgfile`.
> Daha fazla bilgi için: <https://manned.org/pacman.8>.

- Paket veritabanını güncelle:

`sudo pacman -Fy`

- Belirli bir Dosya'ya sahip paketi bul:

`pacman -F {{dosya_adi}}`

- Belirli bir Dosya'ya sahip paketi, bir `rege[x]` kullanarak bul:

`pacman -Fx '{{regex}}'`

- Sadece paket adlarını listele:

`pacman -Fq {{dosya_adi}}`

- Belirli bir pakete ait Dosyaları \[l]istele:

`pacman -Fl {{paket}}`

- Yardımı görüntüle:

`pacman -Fh`
