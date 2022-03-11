# docker network

> Docker ağları oluştur ve yönet.
> Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/network/>.

- docker daemon'daki tüm müsait ve düzenlenmiş ağları sırala:

`docker network ls`

- Kullanıcı tarafından belirtilmiş bir ağ oluştur:

`docker network create --driver {{driver_name}} {{ağ_ismi}}`

- Boşluk ile ayrılmış bir ağ listesinin detaylı bilgisini görüntüle:

`docker network inspect {{ağ_ismi}}`

- Bir konteyneri isim veya ID kullanarak bir ağa bağla:

`docker network connect {{ağ_ismi}} {{konteyner_ismi|ID}}`

- Bir konteyneri bir ağdan çıkar:

`docker network disconnect {{ağ_ismi}} {{konteyner_ismi|ID}}`

- Tüm kullanılmayan (hiçbir konteyner tarafından belirtilmeyen) ağları sil:

`docker network prune`

- Kullanılmayan ağların boşluk ile ayrılmış bir listesini sil:

`docker network rm {{ağ_ismi}}`
