# bitcoind

> Daemon de Bitcoin Core.
> Utiliza la configuración definida en `bitcoin.conf`.
> Más información: <https://manned.org/bitcoind>.

- Inicia el daemon Bitcoin Core (en primer plano):

`bitcoind`

- Inicia el daemon Bitcoin Core en segundo plano (usa `bitcoin-cli stop` para detenerlo):

`bitcoind -daemon`

- Inicia el daemon Bitcoin Core en una red específica:

`bitcoind -chain={{main|test|signet|regtest}}`

- Inicia el daemon Bitcoin Core usando un archivo de configuración y directorio de datos específicos:

`bitcoind -conf={{ruta/a/bitcoin.conf}} -datadir={{ruta/a/directorio}}`
