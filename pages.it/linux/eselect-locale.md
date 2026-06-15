# eselect locale

> Un modulo `eselect` per la gestione della variabile d'ambiente `$LANG`, che imposta la lingua di sistema.
> Maggiori informazioni: <https://wiki.gentoo.org/wiki/Eselect#Locale>.

- Elenca le impostazioni locali disponibili:

`eselect locale list`

- Imposta la variabile d'ambiente `$LANG` in `/etc/profile.env` per nome o indice dal comando `list`:

`eselect locale set {{nome|indice}}`

- Mostra il valore di `$LANG` in `/etc/profile.env`:

`eselect locale show`
