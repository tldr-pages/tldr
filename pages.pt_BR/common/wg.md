# wg

> Gerencia a configuração de interfaces WireGuard.
> Mais informações: <https://www.wireguard.com/quickstart/>.

- Verifica o status das interfaces atualmente ativas:

`sudo wg`

- Verifica o status da interface especificada:

`sudo wg show {{interface}}`

- Gera uma nova chave privada e a exibe em `stdout`:

`wg genkey`

- Gera uma chave pública a partir de uma chave privada e a exibe em `stdout`:

`wg <{{caminho/para/chave_privada}} pubkey`

- Gera uma chave pública e uma privada e as salva em arquivos:

`wg genkey | tee {{caminho/para/chave_privada}} | wg pubkey >{{caminho/para/chave_publica}}`

- Gera uma chave pré-compartilhada e a exibe em `stdout`:

`wg genpsk`

- Mostra a configuração ativa de uma interface:

`sudo wg showconf {{interface}}`
