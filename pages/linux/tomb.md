# tomb

> Manage the creation and access of encrypted storage files

- Create a 100Mb tomb, lock it with a key, and mount it at /media/secret

`tomb dig -s 100 {{secret.tomb}}`
`tomb forge {{secret.tomb.key}}`
`tomb lock {{secret.tomb}} -k {{secret.tomb.key}}`
`tomb open {{secret.tomb}} -k {{secret.tomb.key}}`

- List all open tombs

`tomb list`

- Close a tomb.

`tomb close {{secret.tomb}}`

- Open a local tomb using a remote key

`ssh {{user@server.net}} 'cat {{secret.tomb.key}}' | tomb open {{secret.tomb}} -k -`

- Open a remote tomb with a local key

`gpd -d {{secret.tomb.key}} | ssh {{user@server.net}} tomb open {{secret.tomb}} -k cleartext --unsafe`
