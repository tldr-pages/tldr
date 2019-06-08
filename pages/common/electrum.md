# electrum

> Ergonomic Bitcoin wallet and private key management.
> More information: <https://electrum.org>.

- Create a new wallet:

`electrum -w {{new_wallet.dat}} create`

- Restore an existing wallet from seed offline:

`electrum -w {{recovery_wallet.dat}} restore -o`

- Create a signed transaction offline:

`electrum mktx {{recipient}} {{amount}} -f 0.0000001 -F {{from}} -o`

- Display all wallet receiving addresses:

`electrum listaddresses -a`

- Sign a message:

`electrum signmessage {{address}} {{message}}`

- Verify a message:

`electrum verifymessage {{address}} {{signature}} {{message}}`

- Connect only to a specific electrum-server instance:

`electrum -p socks5:{{127.0.0.1}}:9050 -s {{56ckl5obj37gypcu.onion}}:50001:t -1`
