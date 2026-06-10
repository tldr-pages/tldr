# gocryptfs

> Գոյում գրված ծածկագրված ծածկույթի ֆայլային համակարգ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/rfjakob/gocryptfs#use>:.

- Նախաձեռնեք կոդավորված ֆայլային համակարգը.:

`gocryptfs -init {{path/to/cipher_directory}}`

- Տեղադրեք կոդավորված ֆայլային համակարգ.:

`gocryptfs {{path/to/cipher_directory}} {{path/to/mount_point}}`

- Տեղադրեք գաղտնաբառի փոխարեն բացահայտ հիմնական բանալիով.:

`gocryptfs --masterkey {{path/to/cipher_directory}} {{path/to/mount_point}}`

- Փոխել գաղտնաբառը.:

`gocryptfs --passwd {{path/to/cipher_directory}}`

- Կազմեք պարզ գրացուցակի կոդավորված պատկեր.:

`gocryptfs --reverse {{path/to/plain_directory}} {{path/to/cipher_directory}}`
