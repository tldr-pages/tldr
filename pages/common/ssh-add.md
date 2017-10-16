# ssh-add

> Manage loaded RSA or DSA keys in the ssh-agent.

- Add a new key to the ssh-agent:

`ssh-add {{path/to/private_key}}`

- List fingerprints of currently loaded keys:

`ssh-add -l`

- Delete a key from the ssh-agent:

`ssh-add -d {{path/to/private_key}}`

- Delete all currently loaded keys from the ssh-agent:

`ssh-add -D`

- For MacOS: Add a key to the ssh-agent and the keychain:

`ssh-add -K {{path/to/private_key}}`
