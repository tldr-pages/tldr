# gpasswd

> Administer `/etc/group` and `/etc/gshadow`.
> More information: <https://manned.org/gpasswd>.

- Define group administrators:

`sudo gpasswd {{[-A|--administrators]}} {{user1,user2}} {{group}}`

- Set the list of group members:

`sudo gpasswd {{[-M|--members]}} {{user1,user2}} {{group}}`

- Create a password for the named group:

`gpasswd {{group}}`

- Add a user to the named group:

`gpasswd {{[-a|--add]}} {{user}} {{group}}`

- Remove a user from the named group:

`gpasswd {{[-d|--delete]}} {{user}} {{group}}`
