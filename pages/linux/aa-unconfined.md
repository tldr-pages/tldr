# aa-unconfined

> List processes with open TCP/UDP ports that do not have AppArmor profiles loaded.
> More information: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-unconfined.8>.

- List unconfined processes using the `ss` command (default):

`sudo aa-unconfined`

- Use `netstat` instead of `ss` to detect open network sockets:

`sudo aa-unconfined --with-netstat`

- Show all processes from /proc with TCP/UDP ports and no AppArmor profiles (more detailed):

`sudo aa-unconfined --paranoid`

- Display help:

`aa-unconfined {{[-h|--help]}}`
