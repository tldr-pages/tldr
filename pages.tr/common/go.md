# go

> Go kaynak kodunu yönetmeye yarayan bir araç.
> `go build` gibi bazı alt komutların kendı kullanım dokümentasyonları mevcut.
> Daha fazla bilgi için: <https://golang.org>.

- İçe aktarım yolunda belirtilen şekilde bir paketi indir ve yükle:

`go get {{paket_yolu}}`

- Bir kaynak dosyasını derle ve çalıştır (bir `main` paketine sahip olmalı):

`go run {{dosya}}.go`

- Bir kaynak dosyasını belirtilen çalıştırılabilir dosyaya derle:

`go build -o {{çalıştırılabilir}} {{dosya}}.go`

- Mevcut dizinde bulunan paketi derle:

`go build`

- Mevcut paket için tüm test durumlarını çalıştır (bahsi geçen dosyalar `_test.go` ifadesi ile bitmeli):

`go test`

- Mevcut paketi derle ve indir:

`go install`

- Mevcut diizinde yeni bir modül başlat:

`go mod init {{modül_ismi}}`
