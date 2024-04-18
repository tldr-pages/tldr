# docker system

> Docker verilerini yönet ve sistem bilgisi görüntüle.
> Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/system/>.

- Yardım göster:

`docker system`

- Docker disk kullanımını göster:

`docker system df`

- Disk kullanımı üzerine detaylı bilgi göster:

`docker system df --verbose`

- Kullanılmayan veriyi sil:

`docker system prune`

- Kullanılmayan ve geçmişte birden çok kez oluşturulan veriyi sil:

`docker system prune --filter "until={{saat}}h{{dakika}}m"`

- Docker deamon'dan tam-zamanlı eylemleri görüntüle:

`docker system events`

- Geçerli JSON satırları olarak yayınlanan konteynerleden tam-zamanlı eylemleri göster:

`docker system events --filter 'type=container' --format '{{json .}}'`

- Sistem bilgisi göster:

`docker system info`
