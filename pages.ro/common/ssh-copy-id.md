# ssh-copy-id

> Instalați cheia publică în key_authorized_keys de la distanță.

- Copiați cheile la mașina de la distanță:

`ssh-copy-id {{username@remote_host}}`

- Copiați cheia publică dată la telecomandă:

`ssh-copy-id -i {{path/to/certificate}} {{username}}@{{remote_host}}`

- Copiați cheia publică dată la telecomandă cu port specific:

`ssh-copy-id -i {{path/to/certificate}} -p {{port}} {{username}}@{{remote_host}}`
