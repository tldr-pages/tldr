# aa-update-browser

> Update AppArmor browser profiles to use supported abstractions.
> Part of the AppArmor suite.
> More information: <https://manned.org/aa-update-browser>.

- [l]ist available browser abstraction profiles:

`sudo aa-update-browser -l`

- Show what changes would be made to a profile without applying them ([d]ry-run):

`sudo aa-update-browser -d {{path/to/profile}}`

- [u]pdate a profile with specific abstractions:

`sudo aa-update-browser -u {{abstraction1,abstraction2,...}} {{path/to/profile}}`

- Remove all abstractions from a profile:

`sudo aa-update-browser -u '' {{path/to/profile}}`

- Display help:

`aa-update-browser -h`
