# bitcoind

> Bitcoin Core daemon.
> Uses the configuration defined in `bitcoin.conf`.
> More information: <https://manned.org/bitcoind>.

- Start the Bitcoin Core daemon (in the foreground):

`bitcoind`

- Start the Bitcoin Core daemon in the background (use `bitcoin-cli stop` to stop):

`bitcoind -daemon`

- Start the Bitcoin Core daemon on a specific network:

`bitcoind -chain={{main|test|signet|regtest}}`

- Start the Bitcoin Core daemon using specific config file and data directory:

`bitcoind -conf={{path/to/bitcoin.conf}} -datadir={{path/to/directory}}`
