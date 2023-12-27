# aurvote

> Vote for packages in the Arch User Repository.
> To be able to vote, the file `~/.config/aurvote` must exist and contain your AUR credentials.
> More information: <https://github.com/archlinuxfr/aurvote>.

- Interactively create the file `~/.config/aurvote` containing your AUR username and password:

`aurvote --configure`

- Vote for one or more AUR packages:

`aurvote {{package1 package2 ...}}`

- Unvote one or more AUR packages:

`aurvote --unvote {{package1 package2 ...}}`

- Check if one or more AUR packages have already been voted:

`aurvote --check {{package1 package2 ...}}`

- Display help:

`aurvote --help`
