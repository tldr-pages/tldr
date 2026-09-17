# modinfo

> Estrae le informazioni riguardarti un modulo del kernel Linux.
> Vedi anche: `kmod`.
> Maggiori informazioni: <https://manned.org/modinfo>.

- Elenca tutti gli attributi di un modulo del kernel:

`modinfo {{modulo_del_kernel}}`

- Elenca solamente gli attributi specificati:

`modinfo {{[-F|--field]}} {{author|description|license|parm|filename|version|...}} {{modulo_del_kernel}}`
