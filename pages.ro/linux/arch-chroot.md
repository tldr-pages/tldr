# arch-chroot

> Comandă îmbunătățită `chroot` pentru a ajuta la procesul de instalare Arch Linux.
> Mai multe informaţii: <https://man.archlinux.org/man/arch-chroot.8>

- Porniți un shell interactiv (`bash`, implicit) într-un director rădăcină nou:

`arch-chroot {{path/to/new/root}}`

- Specificați utilizatorul (altul decât utilizatorul curent) pentru a rula shell-ul ca:

`arch-chroot -u {{user}} {{path/to/new/root}}`

- Rulați o comandă personalizată (în loc de `bash` implicit) în noul director rădăcină:

`arch-chroot {{path/to/new/root}} {{command}} {{command_arguments}}`

- Specificați carcasa, alta decât cea implicită `bash` (în acest caz, pachetul `zsh` ar fi trebuit instalat în sistemul țintă):

`arch-chroot {{path/to/new/root}} {{zsh}}`
