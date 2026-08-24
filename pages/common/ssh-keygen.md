# ssh-keygen

> Generate SSH keys used for authentication, password-less logins, and other things.
> See also: `ssh-copy-id`.
> More information: <https://man.openbsd.org/ssh-keygen>.

- Generate a key interactively:

`ssh-keygen`

- Generate an ed25519 key with 32 key derivation function rounds and save the key to a specific file:

`ssh-keygen -f {{~/.ssh/filename}} -t ed25519 -a 32`

- Generate an RSA 4096-bit key with email as a comment:

`ssh-keygen -t rsa -b 4096 -C "{{comment|email}}"`

- Remove the keys of a host from the `known_hosts` file (useful when a known host has a new key):

`ssh-keygen -R {{remote_host}}`

- Retrieve the fingerprint of a key in MD5 Hex:

`ssh-keygen -f {{~/.ssh/filename}} -l -E md5`

- Change the password of a key:

`ssh-keygen -f {{~/.ssh/filename}} -p`

- Change the type of the key format (for example from OPENSSH format to PEM), the file will be rewritten in-place:

`ssh-keygen -f {{~/.ssh/OpenSSH_private_key}} -p -m PEM`

- Retrieve public key from private key:

`ssh-keygen -f {{~/.ssh/OpenSSH_private_key}} -y`
