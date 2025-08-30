# service

> Başlatma betiklerini çalıştırarak hizmetleri/servisleri yönetin.
> Tam betik yolu atlanmalıdır (`/etc/init.d/` varsayılır).
> Daha fazla bilgi için: <https://manned.org/service>.

- Tüm servisleri ve durumlarını görüntüleyin:

`service --status-all`

- Bir servisi Başlatın/Durdurun/Yeniden başlatın/Yeniden yükleyin (başlat/durdur her zaman mevcut olmalıdır):

`service {{servis_adı}} {{start|stop|restart|reload}}`

- Tam yeniden başlatma yapın (betiği başlat ve durdur seçenekleriyle iki kez çalıştırır):

`service {{servis_adı}} --full-restart`

- Servisin şuanki durumunu görüntüleyin:

`service {{servis_adı}} status`
