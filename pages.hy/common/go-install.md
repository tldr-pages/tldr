# գնացեք տեղադրեք

> Կազմել և տեղադրել ներմուծման ուղիներով անվանված փաթեթներ:.
> Լրացուցիչ տեղեկություններ. <https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies>:.

- Կազմել և տեղադրել ընթացիկ փաթեթը.:

`go install`

- Կազմել և տեղադրել հատուկ տեղական փաթեթ.:

`go install {{path/to/package}}`

- Տեղադրեք ծրագրի վերջին տարբերակը՝ անտեսելով `go.mod`-ն ընթացիկ գրացուցակում.:

`go install {{golang.org/x/tools/gopls}}@{{latest}}`

- Տեղադրեք ծրագիր ընթացիկ գրացուցակում `go.mod`-ի կողմից ընտրված տարբերակով.:

`go install {{golang.org/x/tools/gopls}}`
