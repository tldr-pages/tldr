# go get

> Bir bağımlılık paketi ekle veya eski GOPATH modunda paket indir.
> Daha fazla bilgi için: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- `go.mod`'a modül modunda (module-mode) belirtilen bir paket ekle veya paketi GOPATH modunda indir:

`go get {{ornek.com/pkg}}`

- Paketi module-aware modunda belirtilen sürümde düzenle:

`go get {{ornek.com/pkg}}@{{v1.2.3}}`

- Belirtilen paketi sil:

`go get {{ornek.com/pkg}}@{{none}}`
