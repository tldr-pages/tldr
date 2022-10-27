# transmission-edit

> Modify announce URLs from torrent files.
> See also: `transmission`.
> More information: <https://manned.org/transmission-edit>.

- Add or remove a URL from a torrent's announce list:

`transmission-edit --{{add|delete}} {{http://example.com}} {{path/to/file.torrent}}`

- Update a tracker's passcode in a torrent file:

`transmission-edit --replace {{old-passcode}} {{new-passcode}} {{path/to/file.torrent}}`
