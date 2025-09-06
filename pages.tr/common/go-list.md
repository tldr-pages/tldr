# go list

> Paket ve modülleri sırala.
> Daha fazla bilgi için: <https://pkg.go.dev/cmd/go#hdr-List_packages_or_modules>.

- Paketleri sırala:

`go list ./...`

- Standart paketleri sırala:

`go list std`

- Paketleri JSON formatında sırala:

`go list -json time net/http`

- Modül bağımlılıklarını ve erişilebilir güncellemeleri sırala:

`go list -m -u all`
