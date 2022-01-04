# docker build

> Bir Dockerfile'dan imge yaratın.
> Daha fazla bilgi: <https://docs.docker.com/engine/reference/commandline/build/>.

- Mevcut dizindeki Dockerfile'dan bir docker imgesi oluşturun:

`docker build .`

- Belirtilen URL'deki Dockerfile'dan bir docker imgesi oluşturun:

`docker build {{ornekadres.com/ornek-dizin/ornek-docker-projesi}}`

- Bir docker imgesi oluşturun ve etiketleyin:

`docker build --tag {{isim:etiket}} .`

- İmge oluştururken çerez kullanımını etkisizleştirin:

`docker build --no-cache --tag {{isim:etiket}} .`

- Belirtilen Dockerfile ile bir docker imgesi oluşturun:

`docker build --file {{Dockerfile}} .`

- Kişiselleştirilmiş yapım-zaman değerleriyle oluşturun:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
