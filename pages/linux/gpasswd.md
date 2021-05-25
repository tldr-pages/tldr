# gpasswd

> Administer `/etc/group` and `/etc/gshadow`.

- Define group administrators:

`sudo gpasswd -A {{user1,user2}} {{group}}`

- Set the list of group members:

`sudo gpasswd -M {{user1,user2}} {{group}}`

- Create a password for the named group:

`gpasswd {{group}}`

- Add a user to the named group:

`gpasswd -a {{user}} {{group}}`

- Remove a user from the named group:

`gpasswd -d {{user}} {{group}}`
