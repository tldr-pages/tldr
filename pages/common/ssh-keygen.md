# ssh-keygen

> Generate ssh keys user for authentication, password-less logins, and other things.

- Generate a key interactivel:

`ssh-keygen`

- Generate a DSA 2048 bit (default) ke:

`ssh-keygen -t dsa`

- Generate an RSA 4096 bit key with your email as a commen:

`ssh-keygen -t rsa -b 4096 -C "{{email}}"`

- Retrieve the key fingerprint from a host (useful for confirming the authenticity of the host when first connecting to it via SSH:

`ssh-keygen -l -F {{remote_host}}`
