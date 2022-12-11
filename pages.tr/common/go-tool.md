# go tool

> Belirtilen bir Go aracını veya komutunu çalıştır.
> Bir Go komutunu tipik olarak hata ayıklamak için tek başına bir binary olarak çalıştır.
> Daha fazla bilgi için: <https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>.

- Erişilebilir araçları sırala:

`go tool`

- Go bağ aracını çalıştır:

`go tool link {{örnek/konum/main.o}}`

- Çalıştırılacak komutu çalıştırmadan yazdır (`whereis`'e benzer):

`go tool -n {{komut}} {{argümanları}}`

- Belirtilen araç için resmi dokümentasyonu göster:

`go tool {{komut}} --help`
