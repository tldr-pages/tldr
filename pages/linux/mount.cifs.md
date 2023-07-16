# mount.cifs

> Mount SMB (Server Message Block) or CIFS (Common Internet File System) shares.
> Note: you can also do the same thing by passing the `-t cifs` option to `mount`.
> More information: <https://manned.org/mount.cifs>.

- Connect using the specified username or `$USER` by default (you will be prompted for a password):

`mount.cifs -o user={{username}} //{{server}}/{{share_name}} {{mountpoint}}`

- Connect as the guest user (without a password):

`mount.cifs -o guest //{{server}}/{{share_name}} {{mountpoint}}`

- Set ownership information for the mounted directory:

`mount.cifs -o uid={{user_id|username}},gid={{group_id|groupname}} //{{server}}/{{share_name}} {{mountpoint}}`
