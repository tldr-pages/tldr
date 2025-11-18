# apt-get

> Debian ve Ubuntu paket yönetim aracı.
> Paket aramak için `apt-cache` komutunu kullanın.
> Daha fazla bilgi için: <https://manned.org/apt-get.8>.

- Kullanılabilir paket ve versiyon listesini güncelleyin (diğer `apt-get` komutlarını çalıştırmadan önce kullanmanız önerilir):

`sudo apt-get update`

- Bir paket yükleyin veya son sürüme güncelleyin:

`sudo apt-get install {{paket}}`

- Bir paketi silin:

`sudo apt-get remove {{paket}}`

- Bir paketi ve konfigürasyon dosyalarını silin:

`sudo apt-get purge {{paket}}`

- Yüklü paketlerin hepsini son sürümlerine yükseltin:

`sudo apt-get upgrade`

- Yerel depoyu temizleyin - kullanılmayan gereksiz paket dosyalarını (.deb) silin:

`apt-get autoclean`

- Artık gerekmeyen paketleri silin:

`sudo apt-get autoremove`

- Yüklenmiş paketleri yükseltin (`upgrade` gibi), ancak gereksiz paketleri silin ve yeni bağımlılıkları memnun edecek ek paketler kurun:

`sudo apt-get dist-upgrade`
