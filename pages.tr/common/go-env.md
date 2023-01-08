# go env

> Go toolchain'in kullandığı ortam değişkenlerini yönet.
> Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Print_Go_environment_information>.

- Tüm ortam değişkenlerini göster:

`go env`

- Belirtilen ortam değişkenlerini göster:

`go env {{GOPATH}}`

- Bir değere ortam değişkeni ata:

`go env -w {{GOBIN}}={{örnek/konum/dizin}}`

- Ortam değişkeninin değerini sıfırla:

`go env -u {{GOBIN}}`
