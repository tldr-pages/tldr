# docker compose

> Çoklu konteynerli Docker uygulamalarını çalıştırın ve yönetin.
> Daha fazla bilgi için: <https://docs.docker.com/compose/reference/>.

- Tüm konteynerleri listele:

`docker compose ps`

- Mevcut dizinde bir `docker-compose.yml` dosyası çalıştırarak arkaplandaki tüm konteynerleri çalıştırın ve başlatın:

`docker compose up --detach`

- Tüm konteynerleri çalıştırın ve gerekiyorsa yeniden oluşturun:

`docker compose up --build`

- Tüm konteynerleri alternatif bir beste dosyasıyla başlatın:

`docker compose -p {{proje Adı}} --file {{yoldan/dosyaya}} up`

- Çalışan tüm konteynerleri durdurun:

`docker compose stop`

- Tüm konteynerleri, ağları, imgeleri ve alanları durdurun ve silin:

`docker compose down --rmi all --volumes`

- Tüm konteynerler için logları takip edin:

`docker compose logs --follow`

- Belirtilmiş bir konteyner için logları takip edin:

`docker compose logs --follow {{konteyner_ismi}}`
