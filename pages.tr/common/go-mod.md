# go mod

> Modül yönetimi.
> Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Module_maintenance>.

- Mevcut dizinde yeni modül başlat:

`go mod init {{modülİsmi}}`

- Modülleri yerel önbelleğe yükle:

`go mod download`

- Kaybolan modülleri ekle ve kullanılmayanları sil:

`go mod tidy`

- Bağlılıkların beklenen içeriğe sahip olduklarını doğrula:

`go mod verify`

- Tüm bağlılıkların kaynaklarını satıcı dizine kopyala:

`go mod vendor`
