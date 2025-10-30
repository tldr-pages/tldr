# arch-chroot

> Enhanced `chroot` command to help in the Arch Linux installation process.
> More information: <https://manned.org/arch-chroot.8>.

- Start an interactive shell (Bash, by default) in a new root directory:

`arch-chroot {{path/to/new_root}}`

- Specify the user (other than the current user) to run the shell as:

`arch-chroot -u {{user}} {{path/to/new_root}}`

- Run a custom command (instead of the default Bash) in the new root directory:

`arch-chroot {{path/to/new_root}} {{command}} {{command_arguments}}`

- Specify the shell, other than the default Bash (in this case, the `zsh` package should have been installed in the target system):

`arch-chroot {{path/to/new_root}} {{zsh}}`
