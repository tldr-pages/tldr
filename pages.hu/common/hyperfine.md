# hyperfine

> Parancssori benchmarking eszköz. További információ: <https://github.com/sharkdp/hyperfine/>.

- Futtasson le egy alapvető benchmarkot, legalább 10 futtatást végezve:

`hyperfine '{{make}}'`

- Összehasonlító benchmark futtatása:

`hyperfine '{{make target1}}' '{{make target2}}'`

- Változtassa meg a teljesítményértékelési futtatások minimális számát:

`hyperfine --min-runs {{7}} '{{make}}'`

- Benchmark elvégzése bemelegítéssel:

`hyperfine --warmup {{5}} '{{make}}'`

- Futtasson egy parancsot minden egyes benchmark-futtatás előtt (gyorsítótárak törlése stb.):

`hyperfine --prepare '{{make clean}}' '{{make}}'`

- Futtasson olyan benchmarkot, ahol egyetlen paraméter változik minden egyes futtatásnál:

`hyperfine --prepare '{{make clean}}' --parameter-scan {{num_threads}} {{1}} {{10}} '{{make -j {num_threads}}}'`
