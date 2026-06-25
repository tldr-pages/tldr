# salt-key

> Manage salt minion keys on the salt master.
> Needs to be run on the salt master, likely as root or with sudo.
> More information: <https://docs.saltproject.io/en/latest/ref/cli/salt-key.html>.

- List all accepted, unaccepted, and rejected minion keys:

`salt-key {{[-L|--list-all]}}`

- Accept a minion key by name:

`salt-key {{[-a|--accept-all]}} {{minion_id}}`

- Reject a minion key by name:

`salt-key {{[-r|--reject]}} {{minion_id}}`

- Print fingerprints of all public keys:

`salt-key {{[-F|--finger-all]}}`
