#գնա վերցրու

> Ավելացրեք կախվածության փաթեթ կամ ներբեռնեք փաթեթներ հին GOPATH ռեժիմում:.
> Լրացուցիչ տեղեկություններ. <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>:.

- Ավելացրեք նշված փաթեթ `go.mod`-ին մոդուլային ռեժիմում կամ տեղադրեք փաթեթը GOPATH ռեժիմում.:

`go get {{example.com/pkg}}`

- Փոփոխեք փաթեթը տվյալ տարբերակով մոդուլի տեղեկացված ռեժիմով.:

`go get {{example.com/pkg}}@{{v1.2.3}}`

- Հեռացնել նշված փաթեթը.:

`go get {{example.com/pkg}}@{{none}}`
