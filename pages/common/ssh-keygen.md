# ssh-keygen

> Generate SSH keys used for authentication, password-less logins, and other things.
> More information: <https://man.openbsd.org/ssh-keygen>.

- Generate a key interactively:

`ssh-keygen`

- Generate an ed25519 key with 32 key derivation function rounds and save the key to a specific file:

`ssh-keygen -t {{ed25519}} -a {{32}} -f {{~/.ssh/filename}}`

- Generate an RSA 4096-bit key with email as a comment:

`ssh-keygen -t {{rsa}} -b {{4096}} -C "{{comment|email}}"`

- Remove the keys of a host from the known_hosts file (useful when a known host has a new key):

`ssh-keygen -R {{remote_host}}`

- Retrieve the fingerprint of a key in MD5 Hex:

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/filename}}`

- Change the password of a key:

`ssh-keygen -p -f {{~/.ssh/filename}}`

- Change the type of the key format (for example from OPENSSH format to PEM), the file will be rewritten in-place:

`ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/OpenSSH_private_key}}`

- Retrieve public key from secret key:

`ssh-keygen -y -f {{~/.ssh/OpenSSH_private_key}}`
