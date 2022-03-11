# docker-machine

> Docker çalıştıran makineler oluştur ve onları yönet.
> Daha fazla bilgi: <https://docs.docker.com/machine/reference/>.

- Halihazırda çalışan docker makinelerini sırala:

`docker-machine ls`

- Belirli bir isim ile docker makinesi oluştur:

`docker-machine create {{isim}}`

- Bir makinenin durumunu öğren:

`docker-machine status {{isim}}`

- Bir makineyi başlat:

`docker-machine start {{isim}}`

- Bir makineyi durdur:

`docker-machine stop {{isim}}`

- Bir makine hakkındaki bilgileri incele:

`docker-machine inspect {{isim}}`
