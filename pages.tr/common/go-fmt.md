# go fmt

> Go kaynak dosyalarını formatla.
> Değiştirilen dosya isimlerini yazdırır.
> Daha fazla bilgi için: <https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources>.

- Mevcut dizindeki Go kaynak dosyalarını formatla:

`go fmt`

- Belirtilen Go paketini içe aktarım yolunda formatla (`$GOPATH/src`):

`go fmt {{örnek/konum/paket}}`

- Paketi mevcut dizinde ve tüm öbür alt dizinlerde formatla (`...` ifadesine dikkat):

`go fmt {{./...}}`

- Hiçbir şeyi düzenlemeden format komutlarının ne yapacağını yazdır:

`go fmt -n`

- Komut çalışırken arkaplanda hangi komutların çalıştığını yazdır:

`go fmt -x`
