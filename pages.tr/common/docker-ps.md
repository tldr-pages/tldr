# docker ps

> Docker konteynerlerini sırala.
> Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/ps/>.

- Halihazırda çalışan docker konteynerlerini listele:

`docker ps`

- Tüm (durmuş veya çalışan) docker konteynerlerini listele:

`docker ps --all`

- En son oluşturulan (durmuş veya çalışan) konteynerleri listele:

`docker ps --latest`

- İsimlerinde belirtilen dizeleri içeren konteynerleri filtrele:

`docker ps --filter="name={{isim}}"`

- Belirtilen imge ile akrabalık taşıyan konteynerleri filtrele:

`docker ps --filter "ancestor={{imge}}:{{tag}}"`

- Konteynerleri çıkış durum koduna göre filtrele:

`docker ps --all --filter="exited={{kod}}"`

- Konteynerleri mevcut durumlarına (oluşturulma, çalışma, silinme, durma, çıkma ve ölme) göre sırala:

`docker ps --filter="status={{mevcut_durum}}"`

- Belirtilmiş bir hacmi gömen veya belirtilmiş bir yola gömülmüş hacmi içeren konteynerleri filtrele:

`docker ps --filter="volume={{örnek/dizin}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
