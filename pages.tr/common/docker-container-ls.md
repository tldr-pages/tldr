# docker container ls

> Docker konteynerlerini sırala.
> Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Halihazırda çalışan Docker konteynerlerini listele:

`docker {{[ps|container ls]}}`

- Tüm (durmuş veya çalışan) Docker konteynerlerini listele:

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- En son oluşturulan (durmuş veya çalışan) konteynerleri listele:

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- İsimlerinde belirtilen dizeleri içeren konteynerleri filtrele:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{isim}}"`

- Belirtilen imge ile akrabalık taşıyan konteynerleri filtrele:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{imge}}:{{tag}}"`

- Konteynerleri çıkış durum koduna göre filtrele:

`docker {{[ps|container ls]}} {{[-a|--all]}} {{[-f|--filter]}} "exited={{kod}}"`

- Konteynerleri mevcut durumlarına (oluşturulma, çalışma, silinme, durma, çıkma ve ölme) göre sırala:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{mevcut_durum}}"`

- Belirtilmiş bir hacmi gömen veya belirtilmiş bir yola gömülmüş hacmi içeren konteynerleri filtrele:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{örnek/dizin}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
