# chroot

> Voer commando of interactieve shell uit met een speciale hoofdmap.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Voer commando uit met gegeven hoofdmap:

`sudo chroot {{pad/naar/nieuwe/hoofdmap}} {{commando}}`

- Specificeer gebruiker en groep (ID of naam) om te gebruiken:

`sudo chroot --userspec={{gebruiker:groep}}`
