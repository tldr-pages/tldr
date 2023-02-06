# chroot

> Parancs vagy interaktív shell futtatása speciális gyökérkönyvtárral. További információ: <https://www.gnu.org/software/coreutils/chroot>.

- Parancs futtatása új gyökérkönyvtárként:

`chroot {{path/to/new/root}} {{command}}`

- Adja meg a használni kívánt felhasználót és csoportot (azonosító vagy név):

`chroot --userspec={{user:group}}`
