# aa-update-browser

> Update AppArmor browser profiles to use supported abstractions.
> Part of the AppArmor suite.
> Requires root privileges.
> More information: <https://manpages.ubuntu.com/manpages/questing/en/man8/aa-update-browser.8.html>.

- List available browser abstraction profiles:

`sudo aa-update-browser -l`

- Show what changes would be made to a profile without applying them (dry-run):

`sudo aa-update-browser -d {{/path/to/profile}}`

- Update a profile with specific abstractions:

`sudo aa-update-browser -u {{abstraction1,abstraction2}} {{/path/to/profile}}`

- Remove all abstractions from a profile:

`sudo aa-update-browser -u '' {{/path/to/profile}}`

- Display help:

`aa-update-browser -h`
