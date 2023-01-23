# ssh-copy-id

> Telepítse nyilvános kulcsát egy távoli gép authorized_keys-ébe. További információ: <https://manned.org/ssh-copy-id>.

- Másolja a kulcsokat a távoli gépre:

`ssh-copy-id {{username@remote_host}}`

- Másolja a megadott nyilvános kulcsot a távoli gépre:

`ssh-copy-id -i {{path/to/certificate}} {{username}}@{{remote_host}}`

- Másolja az adott nyilvános kulcsot a távoli gépre adott porttal:

`ssh-copy-id -i {{path/to/certificate}} -p {{port}} {{username}}@{{remote_host}}`
