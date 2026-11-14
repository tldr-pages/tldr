# pkgtool

> Strumento interattivo a menu per la gestione dei pacchetti Slackware.
> Vedi anche: `installpkg`, `removepkg`, `upgradepkg`, `makepkg`.
> Maggiori informazioni: <https://www.slackbook.org/html/book.html#PACKAGE-MANAGEMENT-PACKAGE-UTILITIES-PKGTOOL>.

- Avvia lo strumento interattivo per pacchetti:

`sudo pkgtool`

- Rimuovi pacchetti interattivamente:

`sudo pkgtool --remove_menu`

- Visualizza i pacchetti installati:

`pkgtool --view_menu`

- Installa pacchetti dalla directory corrente:

`sudo pkgtool --install_menu`

- Configura pacchetti interattivamente (esegue script `doinst.sh`):

`sudo pkgtool --setup_menu`
