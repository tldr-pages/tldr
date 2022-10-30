# go test

> Go paketlerini test et (dosyalar `_test.go` ifadesiyle bitmeli).
> Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Testing_flags>.

- Mevcut dizinde bulunan paketleri test et:

`go test`

- Mevcut dizindeki paketleri ayrıntılı şekilde test et:

`go test -v`

- Mevcut dizindeki ve tüm alt dizinlerdeki paketleri test et (`...` ifadesine dikkat):

`go test -v ./...`

- Mevcut dzindeki paketleri test et ve tüm kalite testlerini çalıştır:

`go test -v -bench .`

- Mevcut dizindeki paketleri test et ve 50 saniye içinde tüm kalite testlerini çalıştır:

`go test -v -bench . -benchtime {{50s}}`

- Paketleri kapsamlı bir analiz ile test et:

`go test -cover`
