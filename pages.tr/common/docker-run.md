# docker run

> Yeni bir Docker konteynerinde bir komut çalıştır.
> Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/container/run/>.

- Yeni bir konteynerde, etiketlenmiş bir imgeden komut çalıştır:

`docker run {{imge:etiket}} {{komut}}`

- Yeni bir konteynerde arkaplanda çalışacak şekilde komut çalıştır ve ID'sini göster:

`docker run {{[-d|--detach]}} {{imge}} {{komut}}`

- İnteraktif mod ve pseudo-TTY'deki bir açık-kapalı konteynerde komut çalıştır:

`docker run --rm {{[-it|--interactive --tty]}} {{imge}} {{komut}}`

- Yeni bir konteynerde geçebilmiş çevresel değişkenler ile komut çalıştır:

`docker run {{[-e|--env]}} '{{değişken}}={{değer}}' {{[-e|--env]}} {{değişken}} {{imge}} {{komut}}`

- Yeni bir konteynerde bağlama takılı hacimlerle komut çalıştır:

`docker run {{[-v|--volume]}} {{örnek/host}}:{{örnek/konteyner}} {{imge}} {{komut}}`

- Yayınlanmış portları içeren yeni bir konteynerde komut çalıştır:

`docker run {{[-p|--publish]}} {{host_portu}}:{{konteyner_portu}} {{imge}} {{komut}}`
