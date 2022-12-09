# abroot

> ABRoot Utility provides full immutability and atomicity by transacting between 2 root partition states (A<->B).
> It also allows on-demand transactions via a transactional shell.
> More information: <https://github.com/Vanilla-OS/ABRoot>.

- Output the present root partition state:

`sudo abroot get present`

- Output the future root partition state:

`sudo abroot get future`

- Enter a transactional shell in the future root partition and switch root on the next boot:

`sudo abroot shell`

- Execute a command in a transactional shell in the future root partition and switch to it on the next boot:

`sudo abroot exec {{command}}`

- Install a package in the host inside a transactional shell in the future root partition and switch to it on the next boot:

`sudo abroot exec apt install {{package}}`

- Update the root partition (For advanced users only):

`sudo abroot _update-boot`

- Display help:

`sudo abroot --help`

- Display version:

`abroot --version`
