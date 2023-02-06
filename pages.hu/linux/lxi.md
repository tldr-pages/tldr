# lxi

> LXI-kompatibilis műszerek, például oszcilloszkópok vezérlése. További információ: <https://github.com/lxi-tools/lxi-tools>.

- LXI eszközök felfedezése a rendelkezésre álló hálózatokon:

`lxi discover`

- Képernyőkép készítése, a plugin automatikus felismerése:

`lxi screenshot --address {{ip_address}}`

- Képernyőkép készítése egy megadott bővítmény használatával:

`lxi screenshot --address {{ip_address}} --plugin {{rigol-1000z}}`

- SCPI-parancs küldése egy műszernek:

`lxi scpi --address {{ip_address}} "{{*IDN?}}"`

- Benchmark futtatása a kérés és a válasz teljesítményének mérésére:

`lxi benchmark --address {{ip_address}}`
