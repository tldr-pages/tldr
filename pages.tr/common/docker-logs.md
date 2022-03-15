# docker logs

> Konteyner kaydını yazdırır.
> Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/logs>.

- Bir konteyner içindeki kayıtları yazdır:

`docker logs {{konteyner_ismi}}`

- Kayıtları yazdır ve izle:

`docker logs -f {{konteyner_ismi}}`

- Son 5 kaydı yazdır:

`docker logs {{konteyner_ismi}} --tail {{5}}`

- Kayıtları yazdır ve zaman damgaları ile iliştir:

`docker logs -t {{konteyner_ismi}}`

- Belli bir konteyner çalışma zamanındaki (i.e. 23m, 10s, 2013-01-02T13:23:37) kayıtları yazdır:

`docker logs {{konteyner_ismi}} --until {{zaman}}`
