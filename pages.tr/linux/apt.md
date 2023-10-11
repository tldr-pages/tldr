# apt

> Debian tabanlı dağıtımlar için paket yönetim aracı.
> Ubuntu 16.04 ve sonraki sürümlerde interaktif kullanıldığında `apt-get` için önerilen değiştirme.
> Daha fazla bilgi için: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Kullanılabilir paket ve versiyonların listesini yenile (Bu komutu diğer `apt` komutlarından önce kullanmanız önerilir):

`apt update`

- Belirli bir paketi arayın:

`apt search {{paket}}`

- Bir paketin bilgilerini gösterin:

`apt show {{paket}}`

- Bir paket kurun veya mevcut en son sürüme güncelleyin:

`apt install {{paket}}`

- Bir paketi kaldırın (bunun için "purge" kullanmak, yapılandırma dosyalarını da kaldırır):

`apt remove {{paket}}`

- Kurulu tüm paketleri mevcut en yeni sürümlerine yükseltin:

`apt upgrade`

- Tüm paketleri listeleyin:

`apt list`

- Kurulu paketleri listeleyin:

`apt list --installed`
