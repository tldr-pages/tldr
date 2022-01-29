# docker

> Docker konteyner ve imgelerini yönetir.
> `docker run` gibi bazı alt komutların kendi dökümantasyonu bulunmaktadır.
> Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Şuan çalışan docker konteynerlerini listele:

`docker ps`

- Tüm (çalışan veya duran) docker konteynerlerini listele:

`docker ps -a`

- Bir imgeden özel bir isimle konteyner başlat:

`docker run --name {{konteyner_ismi}} {{imge}}`

- Varolan bir konteyneri başlat veya durdur:

`docker {{start|stop}} {{konteyner_ismi}}`

- Bir docker kaydından imge çek:

`docker pull {{imge}}`

- Halihazırda çalışan bir konteyner içinde komut istemcisi aç:

`docker exec -it {{konteyner_ismi}} {{sh}}`

- Durmuş bir konteyneri sil:

`docker rm {{konteyner_ismi}}`

- Bir konteynerin kaydını çek ve takip et:

`docker logs -f {{konteyner_ismi}}`
