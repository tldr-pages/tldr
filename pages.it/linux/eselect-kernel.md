# eselect kernel

> Un modulo `eselect` per la gestione del collegamento simbolico `/usr/src/linux`.
> Maggiori informazioni: <https://wiki.gentoo.org/wiki/Eselect#Kernel>.

- Elenca i target del collegamento simbolico del kernel disponibili con i loro numeri:

`eselect kernel list`

- Imposta il collegamento simbolico `/usr/src/linux` per nome o numero dal comando `list`:

`eselect kernel set {{nome|numero}}`

- Mostra a cosa punta attualmente il collegamento simbolico del kernel:

`eselect kernel show`

- Imposta il collegamento simbolico del kernel al kernel attualmente in esecuzione:

`eselect kernel update`
