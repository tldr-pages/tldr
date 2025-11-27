# pveum

> Manage proxmox users.
> More information: <https://pve.proxmox.com/pve-docs/pveum.1.html>.

- List users:

`pveum {{[u|user]}} {{[l|list]}}`

- Add a user:

`pveum {{[u|user]}} {{[a|add]}} {{username}}@pve`

- Add a user with an email, description, and password:

`pveum {{[u|user]}} {{[a|add]}} {{username}}@pve --email {{email_address}} --comment {{description}} --password {{password}}`

- Change user password:

`pveum {{[pa|passwd]}} {{[username}}@pve`

- Delete a user:

`pveum {{[u|user]}} {{[d|delete]}} {{username}}@pve`
