# modinfo

> Estrae le informazioni riguardarti un modulo del kernel Linux.

- Elenca tutti gli attributi di un modulo del kernel:

`modinfo {{modulo_del_kernel}}`

- Elenca solamente gli attributi specificati:

`modinfo -F {{author|description|license|parm|filename}} {{modulo_del_kernel}}`
