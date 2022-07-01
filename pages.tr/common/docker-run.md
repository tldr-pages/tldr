# docker run

> Yeni bir Docker konteynerinde bir komut çalıştır.
> Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/run/>.

- Yeni bir konteynerde, etiketlenmiş bir imgeden komut çalıştır:

`docker run {{imge:etiket}} {{komut}}`

- Yeni bir konteynerde arkaplanda çalışacak şekilde komut çalıştır ve ID'sini göster:

`docker run -d {{imge}} {{komut}}`

- İnteraktif mod ve pseudo-TTY'deki bir açık-kapalı konteynerde komut çalıştır:

`docker run --rm -it {{imge}} {{komut}}`

- Yeni bir konteynerde geçebilmiş çevresel değişkenler ile komut çalıştır:

`docker run -e '{{değişken}}={{değer}}' -e {{değişken}} {{imge}} {{komut}}`

- Yeni bir konteynerde bağlama takılı hacimlerle komut çalıştır:

`docker run -v {{örnek/host}}:{{örnek/konteyner}} {{imge}} {{komut}}`

- Yayınlanmış portları içeren yeni bir konteynerde komut çalıştır:

`docker run -p {{host_portu}}:{{konteyner_portu}} {{imge}} {{komut}}`
