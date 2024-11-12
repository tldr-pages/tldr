# eselect profile

> An `eselect` module for managing the `/etc/portage/make.profile` symlink, which sets the system profile.
> More information: <https://wiki.gentoo.org/wiki/Eselect#Profile>.

- List available profile symlink targets with their numbers:

`eselect profile list`

- Set the `/etc/portage/make.profile` symlink by name or number from the `list` command:

`eselect profile set {{name|number}}`

- Show the current system profile:

`eselect profile show`
