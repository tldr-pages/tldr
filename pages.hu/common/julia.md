# julia

> Magas szintű, nagy teljesítményű dinamikus programozási nyelv a műszaki számítástechnikához. További információ: <https://docs.julialang.org/en/v1/manual/getting-started/>.

- Indítson el egy REPL-t (interaktív héj):

`julia`

- Egy Julia program végrehajtása és kilépés:

`julia {{program.jl}}`

- Olyan Julia program végrehajtása, amely argumentumokat fogad el:

`julia {{program.jl}} {{arguments}}`

- Julia kódot tartalmazó karakterlánc kiértékelése:

`julia -e '{{julia_code}}'`

- Julia kódot tartalmazó karakterlánc kiértékelése, argumentumok átadásával:

`julia -e '{{for x in ARGS; println(x); end}}' {{arguments}}`

- Egy kifejezés kiértékelése és az eredmény kiírása:

`julia -E '{{(1 - cos(pi/4))/2}}'`

- A Julia indítása párhuzamos üzemmódban, N munkafolyamat használatával:

`julia -p {{N}}`
