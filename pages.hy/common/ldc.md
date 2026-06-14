# ldc

> D կոմպիլյատոր, որն օգտագործում է LLVM որպես հետին պլան:.
> Լրացուցիչ տեղեկություններ. <https://wiki.dlang.org/Using_LDC>:.

- Կազմել աղբյուրի կոդի ֆայլը գործարկվող երկուականի մեջ.:

`ldc2 {{path/to/source.d}} -of={{path/to/output_executable}}`

- Կազմել աղբյուրի կոդը ֆայլը առանց կապելու.:

`ldc2 -c {{path/to/source.d}}`

- Ընտրեք թիրախային ճարտարապետությունը և ՕՀ.:

`ldc -mtriple={{architecture_os}} -c {{path/to/source.d}}`

- Ցուցադրել օգնությունը.:

`ldc2 -h`

- Ցուցադրել ամբողջական օգնությունը.:

`ldc2 -help-hidden`
