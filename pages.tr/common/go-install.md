# go install

> İçe aktarım yollarıyla isimlendirilen paketleri derle ve indir.
> Daha fazla bilgi için: <https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies>.

- Mevcut paketi derle ve indir:

`go install`

- Belirtilen yerel paketi derle ve indir:

`go install {{örnek/konum/paket}}`

- Bir programın son sürümünü mevcut dizindeki `go.mod`'u yoksayarak indir:

`go install {{golang.org/x/tools/gopls}}@{{latest}}`

- Bir programın mevcut dizindeki `go.mod`'da belirtilen sürümünü indir:

`go install {{golang.org/x/tools/gopls}}`
