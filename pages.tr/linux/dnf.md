# dnf

> RHEL, Fedora ve CentOS için paket yönetim aracı (yum'un yerini alır).
> Daha fazla bilgi için: <https://dnf.readthedocs.io>.

- Kurulu paketleri kullanılabilir en yeni sürümlere yükselt:

`sudo dnf upgrade`

- Anahtar kelimeler kullanarak paket ara:

`dnf search {{anahtar_kelimeler}}`

- Bir paketin ayrıntılarını göster:

`dnf info {{paket}}`

- Yeni bir paket kur:

`sudo dnf install {{paket}}`

- Yeni bir paket kur ve tüm soruları otomatik evet olarak yanıtla:

`sudo dnf -y install {{paket}}`

- Bir paketi kaldır:

`sudo dnf remove {{paket}}`

- Kurulu paketleri listele:

`dnf list --installed`

- Verilen dosyayı hangi paketlerin sağladığını bul:

`dnf provides {{dosya}}`
