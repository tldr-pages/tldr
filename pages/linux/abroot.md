# abroot

> Utility providing full immutability and atomicity by transacting between 2 root partition states (A⟺B).
> Updates are performed using OCI images, to ensure that the system is always in a consistent state.
> More information: <https://github.com/Vanilla-OS/ABRoot>.

- Add packages to the local image (Note: after executing this command, you need to apply these changes.):

`sudo abroot pkg add {{package}}`

- Remove packages from the local image (Note: after executing this command, you need to apply these changes.):

`sudo abroot pkg remove {{package}}`

- List packages in the local image:

`sudo abroot pkg list`

- Apply changes in the local image (Note: you need to reboot your system for these changes to be applied):

`sudo abroot pkg apply`

- Rollback your system to previous state:

`sudo abroot rollback`

- Edit/View kernel parameters:

`sudo abroot kargs {{edit|show}}`

- Display status:

`sudo abroot status`

- Display help:

`abroot --help`
