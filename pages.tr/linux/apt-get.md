# apt-get

> Debian ve Ubuntu paket yönetim aracı.
> Paket aramak için `apt-cache` komutunu kullanın.
> Daha fazla bilgi için: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Kullanılabilir paket ve versiyon listesini güncelleyin (diğer `apt-get` komutlarını çalıştırmadan önce kullanmanız önerilir):

`apt-get update`

- Bir paket yükleyin veya son sürüme güncelleyin:

`apt-get install {{paket}}`

- Bir paketi silin:

`apt-get remove {{paket}}`

- Bir paketi ve konfigürasyon dosyalarını silin:

`apt-get purge {{paket}}`

- Yüklü paketlerin hepsini son sürümlerine yükseltin:

`apt-get upgrade`

- Yerel depoyu temizleyin - kullanılmayan gereksiz paket dosyalarını (.deb) silin:

`apt-get autoclean`

- Artık gerekmeyen paketleri silin:

`apt-get autoremove`

- Yüklenmiş paketleri yükseltin (`upgrade` gibi), ancak gereksiz paketleri silin ve yeni bağımlılıkları memnun edecek ek paketler kurun:

`apt-get dist-upgrade`
