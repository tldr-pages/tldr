# docker volume

> Docker birimlerini (volume) yönet.
> Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/volume/>.

- Bir birim oluştur:

`docker volume create {{birim_ismi}}`

- Belirli bir etiketle birim oluştur:

`docker volume create --label {{etiket}} {{birim_ismi}}`

- Boyutu 100 MiB ve uid değeri 1000 olan bir `tmpfs` birimi oluştur:

`docker volume create {{[-o|--opt]}} {{type}}={{tmpfs}} {{[-o|--opt]}} {{device}}={{tmpfs}} {{[-o|--opt]}} {{o}}={{size=100m,uid=1000}} {{birim_ismi}}`

- Tüm birimleri listele:

`docker volume ls`

- Bir birimi sil:

`docker volume rm {{birim_ismi}}`

- Bir birim hakkında bilgi görüntüle:

`docker volume inspect {{birim_ismi}}`

- Kullanılmayan tüm yerel birimleri sil:

`docker volume prune`

- Bir alt komut için yardım görüntüle:

`docker volume {{alt_komut}} --help`
