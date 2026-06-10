# բիթքոիդ

> Bitcoin Core daemon.
> Օգտագործում է `bitcoin.conf`-ում սահմանված կոնֆիգուրացիան:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/bitcoind>:.

- Սկսեք Bitcoin Core դաեմոնը (առաջին պլանում).:

`bitcoind`

- Գործարկեք Bitcoin Core դեյմոնը հետին պլանում (դադարեցնելու համար օգտագործեք `bitcoin-cli stop`):

`bitcoind -daemon`

- Սկսեք Bitcoin Core դաեմոնը որոշակի ցանցում.:

`bitcoind -chain={{main|test|signet|regtest}}`

- Սկսեք Bitcoin Core դաեմոնը՝ օգտագործելով հատուկ կազմաձևման ֆայլ և տվյալների գրացուցակ.:

`bitcoind -conf={{path/to/bitcoin.conf}} -datadir={{path/to/directory}}`
