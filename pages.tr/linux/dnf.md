# dnf

> RHEL, Fedora ve CentOS için paket yönetim aracı (yum'un yerini alır).
> `group` ve `config-manager` gibi bazı alt komutların kendi kullanım dökümantasyonu vardır.
> Diğer paket yöneticilerindeki eşdeğer komutlar için bkz: <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Daha fazla bilgi için: <https://dnf.readthedocs.io>.

- Kurulu paketleri mevcut en yeni sürümlere yükselt:

`sudo dnf {{[up|upgrade]}}`

- Paketleri anahtar kelimelerle ara:

`dnf {{[se|search]}} {{anahtar_kelime1 anahtar_kelime2 ...}}`

- Bir paket hakkında detaylı bilgi göster:

`dnf {{[if|info]}} {{paket}}`

- Yeni bir paket kur (`--assumeyes` ile tüm onayları otomatik kabul edebilirsin):

`sudo dnf {{[in|install]}} {{paket1 paket2 ...}}`

- Bir paketi kaldır:

`sudo dnf {{[rm|remove]}} {{paket1 paket2 ...}}`

- Kurulu paketleri listele:

`dnf {{[ls|list]}} --installed`

- Belirli bir komutu sağlayan paketleri bul:

`dnf {{[wp|provides]}} {{komut}}`

- Geçmiş tüm işlemleri görüntüle:

`dnf {{[hist|history]}}`
