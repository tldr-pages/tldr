# ssh-keyscan

> Get the public SSH keys of remote hosts.
> More information: <https://man.openbsd.org/ssh-keyscan>.

- Retrieve all public SSH keys of a remote host:

`ssh-keyscan {{hostname}}`

- Retrieve all public SSH keys of a remote host listening on a specific port:

`ssh-keyscan -p {{port}} {{hostname}}`

- Retrieve certain types of public SSH keys of a remote host:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{hostname}}`

- Manually update the SSH known_hosts file with the fingerprint of a given host:

`ssh-keyscan -H {{hostname}} >> ~/.ssh/known_hosts`
