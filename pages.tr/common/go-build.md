# go build

> Go kaynaklarını derle.
> Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>.

- Bir 'package main' dosyasını derle (çıktı uzantısız bir dosya ismi olacak):

`go build {{örnek/konum/main.go}}`

- Çıktı dosya ismini belirterek derle:

`go build -o {{örnek/konum/binary}} {{örnek/konum/kaynak.go}}`

- Bir paket yarat:

`go build -o {{örnek/konum/binary}} {{örnek/konum/paket}}`

- Bir ana paketi veri yarış tanımlayıcısını etkinleştirerek çalıştırılabilir olarak derle:

`go build -race -o {{örnek/konum/çalıştırılabilir}} {{örnek/konum/ana_paket}}`
