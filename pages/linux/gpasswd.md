# gpasswd

> Administer /etc/group and /etc/gshadow. Administer linux group.

- Define group administrotor(s), only for system administrotor:

`gpasswd -A {{user1[,user2]}} {{group}}`

- Set the list of group member, only for system administrotor:

`gpasswd -M {{user1[,user2]}} {{group}}`

- Create password for the named group:

`gpasswd {{group}}`

- Add the user to the named group:

`gpasswd -a {{user}} {{group}}`

- Remove the user to the named group:

`gpasswd -d {{user}} {{group}}`
