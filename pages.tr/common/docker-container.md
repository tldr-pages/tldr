# docker container

> Docker konteynerlerini yönetin.
> Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/container/>.

- Şuan çalışan docker konteynerlerini listeleyin:

`docker container ls`

- Bir veya daha fazla durmuş olan konteyneri çalıştırın:

`docker container start {{konteyner_ismi1}} {{konteyner_ismi2}}`

- Bir veya daha fazla çalışan konteyneri öldürün:

`docker container kill {{konteyner_ismi}}`

- Bir veya daha fazla konteyneri durdurun:

`docker container stop {{konteyner_ismi}}`

- Bir veya daha fazla konteynerdeki tüm işlemleri beklemeye alın:

`docker container pause {{konteyner_ismi}}`

- Bir veya daha fazla konteynerle ilgili detaylı bilgi gösterin:

`docker container inspect {{konteyner_ismi}}`

- Bir konteynerin dosya sistemini tar arşivi olarak dışa aktarın:

`docker container export {{konteyner_ismi}}`

- Bir konteynerdeki değişikliklerden yeni imge yaratın:

`docker container commit {{konteyner_ismi}}`
