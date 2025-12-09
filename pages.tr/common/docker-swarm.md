# docker swarm

> Bir konteyner orkestrasyon aracı.
> Daha fazla bilgi için: <https://docs.docker.com/engine/swarm/>.

- Bir bataklık dizisi oluştur:

`docker swarm init`

- Bir yönetici veya işçiye takılmak için token göster:

`docker swarm join-token {{işçi|yönetici}}`

- Diziye yeni bir düğüm ekle:

`docker swarm join --token {{token}} {{manager_node_url:2377}}`

- Bir işçiyi bataklıktan sil (işçi düğümünün içinde çalıştır):

`docker swarm leave`

- Mevcut CA sertifikasını PEM formatında görüntüle:

`docker swarm ca`

- Mevcut CA sertifikasını döndür ve yeni sertifikayı görüntüle:

`docker swarm ca --rotate`

- Düğüm sertifikaları için geçerli periyodu değiştir:

`docker swarm update --cert-expiry {{saat}}h{{dakika}}m{{saniye}}s`
