# docker exec

> Halihazırda çalışan bir Docker konteyneri üstünde komut çalıştır.
> Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/container/exec/>.

- Halihazırda çalışan bir konteynerin üstünde interaktif bir kabuk oturumunu çalıştır:

`docker exec {{[-it|--interactive --tty]}} {{konteyner_ismi}} {{/bin/bash}}`

- Halihazırda çalışan bir konteynerin üstüne arkaplanda çalışmak üzere (ayrılmış) bir komut çalıştır:

`docker exec {{[-d|--detach]}} {{konteyner_ismi}} {{komut}}`

- Belirtilen bir komutu üstünde çalıştırmak adına çalışan dizini seç:

`docker exec {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{örnek/dizin}} {{konteyner_ismi}} {{komut}}`

- Varolan konteyner üstünde arkaplanda çalışmak üzere bir komut çalıştır ancak `stdin`'i açık tut:

`docker exec {{[-i|--interactive]}} {{[-d|--detach]}} {{konteyner_ismi}} {{komut}}`

- Çalışmakta olan bir Bash oturumu içinde bir çevre değişkeni belirle:

`docker exec {{[-it|--interactive --tty]}} {{[-e|--env]}} {{değişken_ismi}}={{value}} {{konteyner_ismi}} {{/bin/bash}}`

- Belirtilmiş bir kullanıcı olarak komut çalıştır:

`docker exec {{[-u|--user]}} {{kullanıcı}} {{konteyner_ismi}} {{komut}}`
