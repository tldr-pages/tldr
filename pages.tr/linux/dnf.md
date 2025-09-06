# dnf

> RHEL, Fedora ve CentOS için paket yönetim aracı (yum'un yerini alır).
> Daha fazla bilgi için: <https://dnf.readthedocs.io>.

- Kurulu paketleri kullanılabilir en yeni sürümlere yükselt:

`sudo dnf upgrade`

- Anahtar kelimeler kullanarak paket ara:

`dnf search {{anahtar_kelimeler1 anahtar_kelimeler2 ...}}`

- Bir paketin ayrıntılarını göster:

`dnf info {{paket}}`

- Yeni bir paket kur:

`sudo dnf install {{paket1 paket2 ...}}`

- Bir paketi kaldır:

`sudo dnf remove {{paket1 paket2 ...}}`

- Kurulu paketleri listele:

`dnf list --installed`

- Verilen dosyayı hangi paketlerin sağladığını bul:

`dnf provides {{dosya}}`
