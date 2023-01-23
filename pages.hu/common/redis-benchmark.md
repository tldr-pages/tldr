# redis-benchmark

> Egy eszköz a Redis szerver benchmarkolására. További információ: <https://redis.io/docs/reference/optimization/benchmarks/>.

- Teljes benchmark futtatása:

`redis-benchmark`

- Benchmark futtatása egy adott Redis szerveren:

`redis-benchmark -h {{host}} -p {{port}} -a {{password}}`

- A tesztek egy részhalmazának futtatása alapértelmezett 100000 kéréssel:

`redis-benchmark -h {{host}} -p {{port}} -t {{set,lpush}} -n {{100000}}`

- Futtatás egy adott szkripttel:

`redis-benchmark -n {{100000}} script load "{{redis.call('set', 'foo', 'bar')}}"`

- Benchmark futtatása 100000 \[r\]andom kulcs használatával:

`redis-benchmark -t {{set}} -r {{100000}}`

- A benchmark futtatása 16 parancsból álló \[P\]ipelining használatával:

`redis-benchmark -n {{1000000}} -t {{set,get}} -P {{16}}`

- A benchmark \[q\]uietly futtatása és csak a másodpercenkénti lekérdezés eredményének megjelenítése:

`redis-benchmark -q`
