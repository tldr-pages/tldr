# docker service

> Bir Docker daemon'unun üzerindeki servisleri yönet.
> Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/service/>.

- Bir Docker daeomon'unun üzerindeki servisleri listele:

`docker service ls`

- Yeni bir servis yarat:

`docker service create --name {{servis_ismi}} {{imge}}:{{etiket}}`

- Boşluk ile ayrılmış bir servis listesinin detaylı bilgisini görüntüle:

`docker service inspect {{servis_ismi|ID}}`

- Boşluk ile ayrılmış bir servis listesinin görevlerini sırala:

`docker service ps {{servis_ismi|ID}}`

- Boşluk ile ayrılmış bir servis listesi için belirli bir replika miktarına yüksel:

`docker service scale {{servis_ismi}}={{replika_miktarı}}`

- Boşluk ile ayrılmış bir servis listesini sil:

`docker service rm {{servis_ismi|ID}}`
