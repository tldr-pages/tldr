# docker stats

> Konteynerler için kaynak kullanım istatistiklerinin canlı yayınını görüntüle.
> Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/stats/>.

- Çalışan tüm konteynerlerin aynak kullanım istatistiklerinin canlı yayınını görüntüle:

`docker stats`

- Boşluk ile ayrılmış bir listedeki konteynerlerin canlı yayınını görüntüle:

`docker stats {{container_ismi}}`

- Konteyner'in CPU kullanım yüzdesini göstermek için sütun formatını değiştir:

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- Tüm (çalışan veya durmuş) konteynerler için istatistikleri görüntüle:

`docker stats --all`

- İstatistikleri canlı yayınlamayı durdur ve yalnızca mevcut durumdaki istatistikleri görüntüle:

`docker stats --no-stream`
