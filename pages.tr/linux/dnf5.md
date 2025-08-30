# dnf5

> RHEL, Fedora ve CentOS için paket yönetim aracı (dnf'in yerini alır, dnf ise yum'un yerini almıştır).
> DNF5, DNF paket yöneticisinin C++ ile yeniden yazılmış halidir; daha iyi performans ve daha küçük boyut sunar.
> Diğer paket yöneticilerindeki eşdeğer komutlar için bkz: <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Daha fazla bilgi için: <https://dnf5.readthedocs.io>.

- Kurulu paketleri mevcut en yeni sürümlere yükselt:

`sudo dnf5 upgrade`

- Paketleri anahtar kelimelerle ara:

`dnf5 search {{anahtar_kelime1 anahtar_kelime2 ...}}`

- Bir paket hakkında detaylı bilgi göster:

`dnf5 info {{paket}}`

- Yeni paketler kur (Not: Tüm onayları otomatik kabul etmek için `-y` kullan):

`sudo dnf5 install {{paket1 paket2 ...}}`

- 1 Paketleri kaldır:

`sudo dnf5 remove {{paket1 paket2 ...}}`

- Kurulu paketleri listele:

`dnf5 list --installed`

- Belirli bir komutu sağlayan paketleri bul:

`dnf5 provides {{komut}}`

- Önbelleğe alınmış verileri kaldır veya geçersiz kıl:

`sudo dnf5 clean all`
