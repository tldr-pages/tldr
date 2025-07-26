# docker logs

> Konteyner kaydını yazdırır.
> Daha fazla bilgi için: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Bir konteyner içindeki kayıtları yazdır:

`docker logs {{konteyner_ismi}}`

- Kayıtları yazdır ve izle:

`docker logs {{[-f|--follow]}} {{konteyner_ismi}}`

- Son 5 kaydı yazdır:

`docker logs {{konteyner_ismi}} {{[-n|--tail]}} {{5}}`

- Kayıtları yazdır ve zaman damgaları ile iliştir:

`docker logs {{[-t|--timestamps]}} {{konteyner_ismi}}`

- Belli bir konteyner çalışma zamanındaki (i.e. 23m, 10s, 2013-01-02T13:23:37) kayıtları yazdır:

`docker logs {{konteyner_ismi}} --until {{zaman}}`
