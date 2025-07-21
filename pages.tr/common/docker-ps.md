# docker ps

> Docker konteynerlerini sırala.
> Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Halihazırda çalışan Docker konteynerlerini listele:

`docker ps`

- Tüm (durmuş veya çalışan) Docker konteynerlerini listele:

`docker ps {{[-a|--all]}}`

- En son oluşturulan (durmuş veya çalışan) konteynerleri listele:

`docker ps {{[-l|--latest]}}`

- İsimlerinde belirtilen dizeleri içeren konteynerleri filtrele:

`docker ps {{[-f|--filter]}} "name={{isim}}"`

- Belirtilen imge ile akrabalık taşıyan konteynerleri filtrele:

`docker ps {{[-f|--filter]}} "ancestor={{imge}}:{{tag}}"`

- Konteynerleri çıkış durum koduna göre filtrele:

`docker ps {{[-a|--all]}} {{[-f|--filter]}} "exited={{kod}}"`

- Konteynerleri mevcut durumlarına (oluşturulma, çalışma, silinme, durma, çıkma ve ölme) göre sırala:

`docker ps {{[-f|--filter]}} "status={{mevcut_durum}}"`

- Belirtilmiş bir hacmi gömen veya belirtilmiş bir yola gömülmüş hacmi içeren konteynerleri filtrele:

`docker ps {{[-f|--filter]}} "volume={{örnek/dizin}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
