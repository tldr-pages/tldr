#գնա կառուցիր

> Կազմել Go աղբյուրները:.
> Լրացուցիչ տեղեկություններ. <https://pkg.go.dev/cmd/go#hdr-Compile_packages_and_dependencies>:.

- Կազմեք «փաթեթի հիմնական» ֆայլ (արդյունքը կլինի ֆայլի անունը առանց ընդլայնման).:

`go build {{path/to/main.go}}`

- Կազմել՝ նշելով ելքային ֆայլի անունը.:

`go build -o {{path/to/binary}} {{path/to/source.go}}`

- Կազմել փաթեթ.:

`go build -o {{path/to/binary}} {{path/to/package}}`

- Կազմեք հիմնական փաթեթը գործարկվողի մեջ՝ հնարավորություն տալով տվյալների մրցավազքի հայտնաբերումը.:

`go build -race -o {{path/to/executable}} {{path/to/main_package}}`
