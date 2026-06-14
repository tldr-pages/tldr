# objdump

> Դիտեք տեղեկատվությունը օբյեկտի ֆայլերի մասին:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/objdump>:.

- Ցուցադրել ֆայլի վերնագրի տեղեկատվությունը.:

`objdump {{[-f|--file-headers]}} {{path/to/binary}}`

- Ցուցադրել վերնագրի բոլոր տեղեկությունները.:

`objdump {{[-x|--all-headers]}} {{path/to/binary}}`

- Ցուցադրել գործարկվող հատվածների ապամոնտաժված ելքը.:

`objdump {{[-d|--disassemble]}} {{path/to/binary}}`

- Ցուցադրել ապամոնտաժված գործարկվող բաժինները Intel-ի շարահյուսությամբ.:

`objdump {{[-d|--disassemble]}} {{path/to/binary}} {{[-M|--disassembler-options]}} intel`

- Ցուցադրել ապամոնտաժված գործարկվող հատվածները՝ թռիչքային պատկերացումներով և շարահյուսական ընդգծմամբ.:

`objdump {{[-d|--disassemble]}} {{path/to/binary}} --visualize-jumps={{color|extended-color}} --disassembler-color={{color|extended-color}}`

- Ցուցադրել [t]able նշանը.:

`objdump {{[-t|--syms]}} {{path/to/binary}}`

- Ցուցադրել բոլոր բաժինների ամբողջական երկուական վեցանկյուն աղբանոցը.:

`objdump {{[-s|--full-contents]}} {{path/to/binary}}`
