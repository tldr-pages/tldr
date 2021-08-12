# chroot

> Executați comanda sau shell-ul interactiv cu directorul rădăcină special.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/chroot>

- Rulați comanda ca director rădăcină nou:

`chroot {{path/to/new/root}} {{command}}`

- Specificați utilizatorul și grupul (ID sau nume) pentru a utiliza:

`chroot --userspec={{user:group}}`
