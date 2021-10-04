# ssh-keygen

> Generate ssh keys used for authentication, password-less logins, and other things.
> More information: <https://man.openbsd.org/ssh-keygen>.

- Generate a key interactively:

`ssh-keygen`

- Specify file in which to save the key:

`ssh-keygen -f {{~/.ssh/filename}}`

- Generate an ed25519 key with 100 key derivation function rounds:

`ssh-keygen -t {{ed25519}} -a {{100}}`

- Generate an RSA 4096-bit key with email as a comment:

`ssh-keygen -t {{dsa|ecdsa|ed25519|rsa}} -b {{4096}} -C "{{comment|email}}"`

- Remove the keys of a host from the known_hosts file (useful when a known host has a new key):

`ssh-keygen -R {{remote_host}}`

- Retrieve the fingerprint of a key in MD5 Hex:

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/filename}}`

- Change the password of a key:

`ssh-keygen -p -f {{~/.ssh/filename}}`

- Change the type of the key format (for example from OPENSSH format to PEM), the file will be rewritten in-place:

`ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/OpenSSH_private_key}}`
