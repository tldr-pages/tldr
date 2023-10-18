# docker secret

> Docker swarm sırlarını yönet.
> Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/secret/>.

- `stdin`'den yeni bir sır yarat:

`{{komut}} | docker secret create {{sır_ismi}} -`

- Bir dosyadan yeni sır oluşturun:

`docker secret create {{sır_ismi}} {{örnek/dosya}}`

- Tüm sırları sırala:

`docker secret ls`

- Bir veya daha fazla sırra dair detaylı bilgiyi insan dostu bir formatta göster:

`docker secret inspect --pretty {{sır_ismi1 sır_ismi2 ...}}`

- Bir veya daha fazla sırrı sil:

`docker secret rm {{sır_ismi1 sır_ismi2 ...}}`
