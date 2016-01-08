# salt-key

> Manages salt minion keys on the salt master.
> Needs to be run on the salt master, likely as root or with sudo.

- List all accepted, unaccepted and rejected minion keys:

`salt-key -L`

- Accept or reject a minion key by name:

`salt-key -a {{MINION_ID}}`
`salt-key -r {{MINION_ID}}`

- Print fingerprints of all public keys:

`salt-key -F`
