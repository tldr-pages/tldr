# encfs

> Տեղադրեք կամ ստեղծեք կոդավորված վիրտուալ ֆայլային համակարգեր:.
> Տես նաև՝ `fusermount`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/encfs>:.

- Նախաձեռնել կամ տեղադրել կոդավորված ֆայլային համակարգ.:

`encfs /{{path/to/cipher_directory}} /{{path/to/mount_point}}`

- Նախաձեռնեք գաղտնագրված ֆայլային համակարգը ստանդարտ պարամետրերով.:

`encfs --standard /{{path/to/cipher_directory}} /{{path/to/mount_point}}`

- Գործարկեք encfs-ը առաջին պլանում՝ դեյմոն ստեղծելու փոխարեն.:

`encfs -f /{{path/to/cipher_directory}} /{{path/to/mount_point}}`

- Տեղադրեք պարզ գրացուցակի կոդավորված պատկերը.:

`encfs --reverse {{path/to/plain_directory}} {{path/to/cipher_directory}}`
