# ssh-keyscan

> Get the public SSH keys of remote hosts.
> More information: <https://man.openbsd.org/ssh-keyscan>.

- Retrieve all public SSH keys of a remote host:

`ssh-keyscan {{host}}`

- Retrieve all public SSH keys of a remote host listening on a specific port:

`ssh-keyscan -p {{port}} {{host}}`

- Retrieve certain types of public SSH keys of a remote host:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{host}}`

- Manually update the SSH known_hosts file with the fingerprint of a given host:

`ssh-keyscan -H {{host}} >> ~/.ssh/known_hosts`
