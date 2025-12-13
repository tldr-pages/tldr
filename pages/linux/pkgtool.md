# pkgtool

> Interactive menu-driven tool for managing Slackware packages.
> See also: `installpkg`, `removepkg`, `upgradepkg`, `makepkg`.
> More information: <https://www.slackbook.org/html/book.html#PACKAGE-MANAGEMENT-PACKAGE-UTILITIES-PKGTOOL>.

- Launch the interactive package tool:

`sudo pkgtool`

- Remove packages interactively:

`sudo pkgtool --remove_menu`

- View installed packages:

`pkgtool --view_menu`

- Install packages from the current directory:

`sudo pkgtool --install_menu`

- Set up packages interactively (run doinst.sh scripts):

`sudo pkgtool --setup_menu`
