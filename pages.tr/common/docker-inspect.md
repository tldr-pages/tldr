# docker inspect

> Docker objelerinde bulunan düşük seviye bilgiyi gösterir.
> Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/inspect/>.

- Yardım içeriğini göster:

`docker inspect`

- Bir konteyner, imge veya hacim ile ilgili bilgiyi ismini veya ID'sini girerek görüntüle:

`docker inspect {{konteyner|imge|ID}}`

- Bir konteynerin IP adresini görüntüle:

`docker inspect {{[-f|--format]}} '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{konteyner}}`

- Konteynerin log dosyasının yolunu görüntüle:

`docker inspect {{[-f|--format]}} '\{\{.LogPath\}\}' {{konteyner}}`

- Konteynerin imge ismini görüntüle:

`docker inspect {{[-f|--format]}} '\{\{.Config.Image\}\}' {{konteyner}}`

- Konfigürasyon bilgisini JSON olarak görüntüle:

`docker inspect {{[-f|--format]}} '\{\{json .Config\}\}' {{konteyner}}`

- Tüm port limanlayıcıları görüntüle:

`docker inspect {{[-f|--format]}} '\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{konteyner}}`
