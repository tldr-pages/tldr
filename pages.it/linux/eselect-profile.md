# eselect profile

> Un modulo `eselect` per la gestione del collegamento simbolico `/etc/portage/make.profile`, che imposta il profilo di sistema.
> Maggiori informazioni: <https://wiki.gentoo.org/wiki/Eselect#Profile>.

- Elenca i target del collegamento simbolico del profilo disponibili con i loro numeri:

`eselect profile list`

- Imposta il collegamento simbolico `/etc/portage/make.profile` per nome o numero dal comando `list`:

`eselect profile set {{nome|numero}}`

- Mostra il profilo di sistema corrente:

`eselect profile show`
