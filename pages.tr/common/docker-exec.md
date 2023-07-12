# docker exec

> Halihazırda çalışan bir Docker konteyneri üstünde komut çalıştır.
> Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Halihazırda çalışan bir konteynerin üstünde interaktif bir kabuk oturumunu çalıştır:

`docker exec --interactive --tty {{konteyner_ismi}} {{/bin/bash}}`

- Halihazırda çalışan bir konteynerin üstüne arkaplanda çalışmak üzere (ayrılmış) bir komut çalıştır:

`docker exec --detach {{konteyner_ismi}} {{komut}}`

- Belirtilen bir komutu üstünde çalıştırmak adına çalışan dizini seç:

`docker exec --interactive -tty --workdir {{örnek/dizin}} {{konteyner_ismi}} {{komut}}`

- Varolan konteyner üstünde arkaplanda çalışmak üzere bir komut çalıştır ancak `stdin`'i açık tut:

`docker exec --interactive --detach {{konteyner_ismi}} {{komut}}`

- Çalışmakta olan bir bash oturumu içinde bir çevre değişkeni belirle:

`docker exec --interactive --tty --env {{değişken_ismi}}={{value}} {{konteyner_ismi}} {{/bin/bash}}`

- Belirtilmiş bir kullanıcı olarak komut çalıştır:

`docker exec --user {{kullanıcı}} {{konteyner_ismi}} {{komut}}`
