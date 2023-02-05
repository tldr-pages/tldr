# write

> Üzenet írása a megadott bejelentkezett felhasználó termináljára (ctrl-C az üzenetírás leállításához).
> A `who` parancs segítségével megtudhatja a rendszerben aktív összes aktív felhasználó összes terminal_id-jét.
> Lásd még: `mesg`.
> További információ: <https://manned.org/write>.

- Üzenet küldése egy adott felhasználónak egy adott terminálazonosítón:

`write {{username}} {{terminal_id}}`

- Üzenet küldése "testuser"-nek a `/dev/tty/5` terminálon:

`write {{testuser}} {{tty/5}}`

- Üzenet küldése "johndoe"-nak az álterminálon `/dev/pts/5`:

`write {{johndoe}} {{pts/5}}`
