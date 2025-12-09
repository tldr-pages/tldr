# electrum

> Ergonomic Bitcoin wallet and private key management.
> More information: <https://manned.org/electrum>.

- Create a new wallet:

`electrum {{[-w|--wallet]}} {{path/to/new_wallet.dat}} create`

- Restore an existing wallet from seed offline:

`electrum {{[-w|--wallet]}} {{path/to/recovery_wallet.dat}} restore {{[-o|--offline]}}`

- Create a signed transaction offline:

`electrum mktx {{recipient}} {{amount}} {{[-f|--fee]}} 0.0000001 {{[-F|--from-addr]}} {{from}} {{[-o|--offline]}}`

- Display all wallet receiving addresses:

`electrum listaddresses -a`

- Sign a message:

`electrum signmessage {{address}} {{message}}`

- Verify a message:

`electrum verifymessage {{address}} {{signature}} {{message}}`

- Connect only to a specific electrum-server instance:

`electrum {{[-p|--proxy]}} socks5:{{127.0.0.1}}:9050 {{[-s|--server]}} {{56ckl5obj37gypcu.onion}}:50001:t {{[-1|--oneserver]}}`
